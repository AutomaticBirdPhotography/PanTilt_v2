# Testing har vist at det trolig er bedre å ikke ha den i en egen thread da den ikke blokkerer blir det bedre synka 

import serial

class Arduino():
    def __init__(self, port: str, baudrate: int = 115200 , timeout: float = 1) -> None:
        """
        Run `ls /dev/tty*` to get the port of the Arduino.
        Initialize the Arduino object.

        Args:
            port (str): The port to connect to.
            baudrate (int, optional): The baudrate of the serial connection. Defaults to 115200.
            timeout (float, optional): The timeout for read operations. Defaults to 1.
        """
        self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def send(self, data: str) -> None:
        """
        Send data to the Arduino.

        Args:
            data (str): The data to send. If None, a blank string will be sent. Encodes the data to bytes.
        """
        if data is None:
            data = ""
        if self.serial.is_open:
            self.serial.write(data.encode())

    def read(self) -> str:
        """
        Read a line from the Arduino, returning the data as a string.

        Returns:
            str: The data read from the Arduino.
        """
        data = self.serial.readline()
        return data.decode()

    def close(self) -> None:
        """
        Close the serial port.

        This is equivalent to disconnecting the serial port from the host.
        Sends "0,0,0,0" to the Arduino to stop the motors.
        """
        self.send("0,0,0,0")
        self.serial.close()