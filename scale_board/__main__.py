import time

from typing import Union
from logging import getLogger

from scale_board import scale_server, BoardProtocol
from scale_board.board import serial
from scale_board.settings import config

log = getLogger("main")


def start_loop(board: Union[serial.BoardSerial]):
    """
    Starting the main cycle for returning data to the board

    Args:
        board: Union[serial.BoardSerial] - Class for working with scoreboard
    """
    while True:
        if not board.connected:
            board.connect()

        weight = scale_server.get_weight(server=config.SCALE_SERVER_URL)

        board.send_weight(weight=weight)

        time.sleep(0.2)


if __name__ == "__main__":
    log.info(f"Start weight boarding from {config.SCALE_SERVER_URL} to {config.BOARD['port']}")
    start_loop(board=BoardProtocol[config.BOARD['protocol']].value(**config.BOARD))
