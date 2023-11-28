from vidgear.gears import NetGear
from vidgear.gears.helper import reducer
import time, threading
import cv2
import numpy as np
import socket
import frame_handler as G
import time

TIME_DELAY = 0.1

options = {
    "request_timeout": 5,
    "max_retries": 35,
    "bidirectional_mode": True,
    "jpeg_compression": True,
    "jpeg_compression_quality": 95,
    "jpeg_compression_fastdct": True,
    "jpeg_compression_fastupsample": True,
}

class VideoStream():
    def __init__(self, logging : bool = True, clientAddress : str = "192.168.4.4", port : str = "5454", framePercentage : int = 20) -> None:
        """
        Initializes a video stream object.

        Parameters:
        - logging (bool): Whether to enable logging or not. Default is True.
        - clientAddress (str): The client address to connect to. Default is "192.168.4.4".
        - port (str): The port to connect to. Default is "5454".
        - framePercentage (int): The percentage of frames to send. Default is 20.
        """
        self.recv_data = None
        self.server = NetGear(logging=logging, address=clientAddress, port=port, **options)
        self.percentage = framePercentage

    def sendFrame(self, frame):
        """
        Sends a frame over the network.

        Parameters:
        - frame: The frame to send.
        """
        self.frame = G.ensure_valid_frame(frame)
        self.frame = reducer(self.frame, self.percentage)
        self.recv_data = self.server.send(self.frame)

        key = cv2.waitKey(10) & 0xFF
        if key == ord("q"):
            self.stop()
            cv2.destroyAllWindows()
            raise Exception("sendFrame ble stoppet av bruker")  # Når denne erroren kommer, vil koden i finally-blokken kjøres

    def getData(self):
        """
        Returns the received data.
        """
        return self.recv_data
    
    def stop(self):
        """
        Stops the video stream.
        """
        if self.server is not None:
            self.server.close()

    def __del__(self):
        self.stop()


class VideoClient():
    def __init__(self, logging : bool = True, clientAddress : str = "auto", port : str = "5454") -> None:
        """
        Initializes a video client object.

        Parameters:
        - logging (bool): Whether to enable logging or not. Default is True.
        - clientAddress (str): The client address to connect to. Default is "auto".
        - port (str): The port to connect to. Default is "5454".
        """
        self.logging = logging
        self.port = port
        self.is_connected = False
        self.client = None
        self.server_data = None
        self.establish_connection(clientAddress)
        
        
        self.stopped = False
        self.frame = self.errorImg = G.error_window(text="Waiting for connection")
        self.thread = threading.Thread(target=self._grabFrameLoop)
        self.thread.daemon = True
        self.thread.start()

    def establish_connection(self, clientAddress="auto"):
        """
        Establishes a connection with the server.

        Parameters:
        - clientAddress (str): The client address to connect to. Default is None.
        """
        if clientAddress == "auto":
            self.clientAddress = socket.gethostbyname(socket.gethostname())
        else:
            self.clientAddress = clientAddress
        self.client = NetGear(receive_mode=True, logging=self.logging, address=self.clientAddress, port=self.port, **options)
        self.target_data = None

    def sendData(self, data):
        """
        Sends data to the server.

        Parameters:
        - data: The data to send.
        """
        if self.is_connected:
            self.target_data = data
    

    def _grabFrameLoop(self):
        """
        Continuously grabs frames from the server.
        """
        while not self.stopped:
            if self.client is not None:
                self.data = self.client.recv(return_data=self.target_data)
                if self.data is not None:
                    self.is_connected = True
                    self.server_data, in_frame = self.data
                    frame = G.ensure_valid_frame(in_frame)
                else:
                    frame = self.errorImg
            else:
                frame = self.errorImg

            self.frame = frame

            # Introduce a delay to match the frame arrival frequency
            time.sleep(TIME_DELAY)
                           

    def grabFrame(self):
        """
        Returns the grabbed frame.
        """
        return self.frame
    
    def stop(self):
        """
        Stops the video client.
        """
        self.stopped = True
        if self.client is not None:
            if self.is_connected:  #hvis den ikke er tilkoblet vil det ikke gå å skulle sende "s"
                self.client.recv(return_data="s")
            self.client.close()

    def __del__(self):
        self.stop()