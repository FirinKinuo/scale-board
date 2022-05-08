from typing import Union

import serial

from scale_board.board import BoardBase


class BoardSerial(BoardBase):
    def __init__(self,
                 port: str,
                 baudrate: int = 9600,
                 byte_size: int = 8,
                 parity: str = 'n',
                 stop_bits: int = 1,
                 timeout: float = 0,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = port
        self.baudrate = baudrate
        self.byte_size = byte_size
        self.parity = parity
        self.stop_bits = stop_bits
        self.serial: Union[serial.Serial, None] = None
        self.timeout = timeout

    def __repr__(self):
        return f"Serial board at {self.port} | Protocol: {self.protocol}"

    def connect(self):
        """Opens a port and makes it readable and writable"""
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=self.byte_size,
                parity=self.parity,
                stopbits=self.stop_bits,
                timeout=self.timeout
            )

            self.connected = True

        except serial.SerialException as err:
            raise SystemError(err) from err

    def disconnect(self):
        """Breaking connection with serial"""
        self.serial.close()
        self.connected = False
