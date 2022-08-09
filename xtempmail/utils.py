import logging
from enum import Enum
from .error import (
    InvalidPIN
)
logging.basicConfig(format='%(asctime)s  %(message)s', level=logging.INFO)
log = logging.getLogger('xtempmail')
log.setLevel(logging.WARNING)


def err_code(c: int):
    if c == 1021:
        return InvalidPIN


class EMAIL(Enum):
    MAILTO_PLUS = 'mailto.plus'
    FEXPOST_COM = 'fexpost.com'
    FEXBOX_ORG = 'fexbox.org'
    FEXBOX_RU = 'fexbox.ru'
    MAILBOX_IN_UA = 'mailbok.in.ua'
    ROVER_INFO = 'rover.info'
    INPWA_COM = 'inpwa.com'
    INTOPWA_COM = 'intopwa.com'
    TOFEAT_COM = 'tofeat.com'
    CHITTHI_IN = 'chitthi.in'

    def apply(self, name: str) -> str:
        return name + '@' + self.value


class Extension:
    def __init__(self, ex: str):
        self.ex = '@' + ex

    def apply(self, text: str) -> str:
        return f"{text}{self.ex.__str__()}"

    def __repr__(self):
        return self.ex

    def __str__(self):
        return self.ex


extension = [Extension(i.value) for i in EMAIL.__members__.values()]