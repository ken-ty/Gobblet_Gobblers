# coding=utf-8
import numpy as np


class State:
    def __init__(self, black=None, white=None):
        self.black = black if black is not None else np.uint32(0x000000000)
        self.white = white if white is not None else np.uint32(0x000000000)

    def encode(self):
        return "hoge"
