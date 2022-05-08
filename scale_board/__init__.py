from enum import Enum

from scale_board.board.serial import microsim


class BoardProtocol(Enum):
    """Enumeration of communication protocols"""
    MICROSIM = microsim.MicrosimBoard
