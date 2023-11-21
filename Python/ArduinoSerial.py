# Testing har vist at det trolig er bedre å ikke ha den i en egen thread da den ikke blokkerer blir det bedre synka 

import serial

class Arduino():
    def __init__(self, port: str, baudrate: int = 115200 , timeout: float = 1) -> None:
        """
        Kjør `ls /dev/tty*` for å finne porten
        """
        self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def send(self, data: str) -> None:
        """
         Send data to the Arduino.
         @param data - The data to send. If None a blank string will be sent. Encodes the data to bytes.
         
        """
        if data is None:
            data = ""
        if self.serial.is_open:
            self.serial.write(data.encode())

    def read(self) -> str:
        """
        BLOCKING!
        Read a line from the Arduino, returning the data as a string.
        """
        data = self.serial.readline()
        return data.decode()

    def close(self) -> None:
        """
         Close the serial port. This is equivalent to disconnecting the serial port from the host.
         Sends "0,0,0,0" to the Arduino, to stop the motors
        """
        self.send("0,0,0,0")
        self.serial.close()