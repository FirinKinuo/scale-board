"""Module configuration"""
import sys
import logging

from typing import TypedDict
from os import environ
from enum import Enum

import serial

__all__ = [
    'DEBUG',
    'IS_TEST',
    'LOG_LEVEL',
    'SCALE_SERVER_URL',
    'BOARD'
]

log = logging.getLogger("Configuration")


class ParityEnum(Enum):
    """Parity enumeration"""
    PARITY_NONE = serial.PARITY_NONE
    PARITY_EVEN = serial.PARITY_EVEN
    PARITY_ODD = serial.PARITY_ODD
    PARITY_MARK = serial.PARITY_MARK
    PARITY_SPACE = serial.PARITY_SPACE


class BoardConfiguration(TypedDict):
    """Board configuration"""
    port: str
    baudrate: int
    byte_size: int
    parity: ParityEnum
    stop_bits: int


__required_envs = [
    'SCALE_SERVER_URL',
    'BOARD_PORT',
    'BOARD_BAUDRATE',
    'BOARD_BYTE_SIZE',
    'BOARD_PARITY',
    'BOARD_STOP_BITS'
]


def check_missing_environ() -> list:
    """
    Checking for the necessary ENVs
    Returns:
        list: List of missing ENVs
    """
    return [env for env in __required_envs if env not in environ]


__missing_envs = check_missing_environ()

if __missing_envs:
    log.critical(f"You must specify the following ENV:\n{', '.join(__missing_envs)}")
    sys.exit(1)

IS_TEST = any(map(lambda path: 'tests' in path, sys.path))  # If test paths are found, then go to test mode

DEBUG = bool(int(environ.get('DEBUG') or False))
LOG_LEVEL = logging.getLevelName((environ.get('LOG_LEVEL') or 'info' if not DEBUG else 'debug').upper())

SCALE_SERVER_URL = environ.get('SCALE_SERVER_URL')
BOARD = BoardConfiguration(
    port=environ.get('BOARD_PORT'),
    baudrate=int(environ.get('BOARD_BAUDRATE')),
    byte_size=int(environ.get('BOARD_BYTE_SIZE')),
    parity=ParityEnum(environ.get('BOARD_PARITY')).value,
    stop_bits=int(environ.get('BOARD_STOP_BITS'))
)

logging.basicConfig(level=LOG_LEVEL,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")
