# coding=utf-8
class State:
    """ステート
      listにする場合は、hoge_actionsと命名します。
    """

    def __init__(self, black, white):
        """
        Args:
          black (int): 動かす駒の元の位置.-1, 0~26で指定.手駒からは-1.
          white (int): 駒を動かす先の位置.0~26で指定.
        """
        self.black = black
        self.white = white

    def before_put_position(self):
        return self.before_put_position

    def _put_position(self):
        return self.put_position
