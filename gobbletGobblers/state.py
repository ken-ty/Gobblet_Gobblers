# coding=utf-8
import numpy as np
import gobbletGobblers.bitExpression as be


class State:
    """
    :arg
        - black(unit32) 00000 A1LA1MA1SB1LB1MB1S ... C3S 盤面のblackコマを表すビット。上位5桁は使用しない。
        - white(unit32) 00000 A1LA1MA1SB1LB1MB1S ... C3S 盤面のwhiteコマを表すビット。上位5桁は使用しない。

    """

    def __init__(self, black=None, white=None):
        self.black = black if black is not None else be.EMPTY
        self.white = white if white is not None else be.EMPTY

