import random
import tictactoe as tic
    
  def mini_max( state ):
    """ミニマックスで状態の価値を計算する.
    """
    # 負けは状態価値-1
    if state.is_lose():
      return -1

    # 引き分けは状態価値0
    if state.is_draw():
      return 0

    # 合法手の状態価値の計算
    best_score = -float('inf')
    for action in state.legal_actions():
      # NegaMax法
      score = -mini_max(state.next(action))
      if score > best_score:
        best_score = score
    # 合法手の状態価値の最大値を返す
    return best_score

