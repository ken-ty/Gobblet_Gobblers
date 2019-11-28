"""Gobblet_Gobblersの作成
盤面は、my_toplayer_piecesとenemy_toplayer_piecesで管理.
また、my_piecesとenemy_piecesですべての駒の場所を管理している.
手番プレイヤーはplayerで管理.
"""
import random

class State:
  """盤面の状態
  Attributes:
    __init__(self, my_pieces, enemy_pieces)  : 初期化
    # delete piece_count(self, pieces): 石の数は数える必要がない.
    is_lose(self): 負けたかどうか
    # delete is_draw(self): 引き分けはない.
    is_done(self): ゲーム終了かどうか
    next(self, action): 次の状態の取得
    legal_actions(self): 合法手のリストの取得
    is_first_player(self): 先手かどうか
    __str__(self): 文字列表示
  """

  def __init__(self, my_pieces=None, enemy_pieces=None, player=1 ):
    """初期化
    引数で与えられた石から現在の局面を作成する.
    
    Args:
      my_pieces (list): 自分の石の場所
      enemy_pieces (list): 敵の駒の場所
      my_toplayer_pieces (list): 盤に見えてる自分の駒の場所 
      enemy_toplayer_pieces (list): 盤に見えてる敵の駒の場所 
      player (int): 先手は1, 後手は-1を入力
    """
    # 全ての駒の位置(0|1)
    self.my_pieces    = my_pieces    if my_pieces    != None else [0] * 27
    self.enemy_pieces = enemy_pieces if enemy_pieces != None else [0] * 27
    
    # 先手か後手か
    self.player = player
    
    # 盤面に見えてる駒の状態(0|1|2|3), 1から小さい順.
    my_toplayer_pieces    = [0] * 9
    enemy_toplayer_pieces = [0] * 9
    for i in range(9):
      for j in range(0, 3):
      if self.my_pieces[i+9*j] != 0:
        my_toplayer_pieces[i]    = j+1
      elif self.enemy_pieces[i+9*j] != 0:
        enemy_toplayer_pieces[i] = j+1
    self.my_toplayer_pieces    = my_toplayer_pieces
    self.enemy_toplayer_pieces = enemy_toplayer_pieces
    
    # 手駒(1|2|3)のリスト.
    hand_my_pieces = []
    for i in range(3):
      num_use_my_pieces = my_pieces[9*(i-1):9*i].count(i+1)
      num_not_use_my_pieces = 2 - num_use_my_pieces
      for num in num_not_use_my_pieces:       
        hand_my_pieces.append(i+1)
    self.hand_my_pieces = hand_my_pieces
    
    # 盤上の動かせる駒(0~26, 手駒から出せるなら-1も加える.)
    can_move_my_pieces = None
    # 0(駒なし),2,3は、toplayerをコピーでOK.
    can_move_my_pieces_candidates = self.my_toplayer_pieces.copy()
    # 1の駒のみ, 移動先のマスがあるか確認.
    for i in range(9):
      if can_move_my_pieces_candidates[i] == 1:
        not_put = 1
        for j in range(9):
          if self.my_toplayer_pieces[j] == 0 and self.enemy_toplayer_pieces[j] == 0:
            not_put = 0
            break;
        if not_put:
          can_move_my_pieces_candidates[i] = 0:
    # 候補を0~26のマスに直す.
    for i in range(9):
      if can_move_my_pieces_candidates[i] > 0:
        can_move_my_pieces.append(i+9*(can_move_my_pieces_candidates[i] -1))
    # 手駒を使い切ってなければ-1を加える.
    if len(self.hand_my_pieces) < 6
      can_move_my_pieces.append.append(-1)
    # ソートする.
    can_move_my_pieces.sort()
    
  def is_lose(self):
    """敗北判定
    Returns:
      bool: 負けているならTrue, そうでないならFalse.
    """
    def is_comp(x, y, dx, dy):
      """3並びかどうか
      x, y で指定したマスからdx,dy方向に合計3マスを調べる.
      x, yには、辺のマス(4以外)を指定.
      例：
        (x,y) = (0,3) のマス6から(dx,dy) = (1,-1)の方向、つまり、マス(6, 4, 2)を調べる.
      
      Args:
        x  (int): 探索開始座標x
        y  (int): 探索開始座標y
        dx (int): 探索方向dx
        dy (int): 探索方向dy
      Returns:
        bool: 3並びならTrue, そうでないならFalse.
      """
      for k in range(3):
        # 範囲外または敵の石がないなら負けてない
        if y < 0 or 2 < y or x < 0 or 2 < x or self.enemy_toplayer_pieces[x+y*3] == 0:
          return False
        # 次のマスの座標にする.
        x, y = x+dx, y+dy
      return True

    # 負けたかどうか
    # 斜めを確認
    if is_comp(0, 0, 1, 1) or is_comp(0, 2, 1, -1):
      #デバッグ:
      #print("斜めまけ")
      return True
    # 縦,横を確認
    for i in range(3):
      if is_comp(0, i, 1, 0):
        #デバッグ:
        #print("横まけ")
        return True
    for i in range(3):
      if is_comp(i, 0, 0, 1):
        #デバッグ:
        #print("縦まけ")
        return True

    # 負けてないならFalse
    return False
  
  def is_done(self):
    """ゲーム終了判定
    Returns:
      bool: ゲーム終了ならTrue, そうでないならFalse
    """
    return self.is_lose()
  
  def next(self, action):
    """次の状態の取得
    
    現在の状態stateに選択した行動actionを反映した、
    新しいStateを作成する。
    新しい局面では手番が入れ替わるため、
    my_piecesとenemy_piecesの返す順序を交換している。
    
    次のstateを作成するために使う。
    例: state = State(state.next( action ))
    Args:
      action ((int|None), int): 第一引数で動かす駒の位置を指定する。手駒ならNone,盤上なら0~26、次に置くマスを0~26で指定.
    Returns:
      (enemy_pieces, my_pieces, enemy_toplayer_pieces, my_toplayer_pieces, player) (State): 行動を反映させたStateを返す.
    """
    my_pieces = self.my_pieces.copy() # リストだからcopyを使用.
    # 手駒から
    if action[0] == None:
      my_pieces[action[1]] = 1
    # 盤上から
    else:
      my_pieces[action[0]] = 0
      my_pieces[action[1]] = 1
    
    # toplayerの更新.
    my_toplayer_pieces    = [0] * 9
    enemy_toplayer_pieces = [0] * 9
    for i in range(9):
      for j in range(0, 3):
      if self.my_pieces[i+9*j] != 0:
        self.my_toplayer_pieces[i]    = j+1
      elif self.enemy_pieces[i+9*j] != 0:
        self.enemy_toplayer_pieces[i] = j+1
      
    # enemy_piecesと更新したmy_piecesを入れ替えてStateを作成.
    # playerはマイナスをかけて交代している.
    return State(self.enemy_pieces, my_pieces, enemy_toplayer_pieces, my_toplayer_pieces, -player)

  def legal_actions(self):
    """合法手のリストの取得
    Returns:
      actions: 合法手のリスト
    """
    # 取り除く候補、0より大きいなら取り除ける。
    remove_candidates_actions = self.my_toplayer_pieces.copy()
    # 取り除けるのは自分のtoplayerかつ他のマスが動かすマスより小さいとき、これは1の駒のみ.
    for i in range(9)
      if remove_candidates_actions[i] == 1:
        not_put = 1
        for i in range(9):
          if self.my_toplayer_pieces[i] == 0 and self.enemy_toplayer_pieces[i] == 0:
            not_put = 0
            break;
        if not_put:
          remove_candidates_action[i] = 0:
            
    # 候補を0~26のマスに直す.
    remove_actions = []
    for i in range(9):
      if remove_candidates_actions[i] >= 1:
        remove_actions.append(i+9*(remove_candidates_actions[i]-1))

    # 手駒を使い切ってなければ-1を加える.
    num_hand_piece  = 6
    for my_piece in my_pieces:
      if my_piece != 0:
        num_hand_piece -= 1
    if num_hand_piece > 0:
      remove_actions.append(-1)
    
    remove_actions.sort()
    
    # actionを作成する.
    for remove_action in remove_actions:
      if remove_action == -1:
        手から動かすのを登録:
      else:
        盤で動かすのを登録:
        
      
  
    if self.my_toplayer_pieces[i] == 0 and self.enemy_toplayer_pieces[i] == 0:
      remove_actions.append(i)
    if self.my_toplayer_pieces[i] <= 1 and self.enemy_toplayer_pieces[i] <= 1:
      actions.append(i+9)
    if self.my_toplayer_pieces[i] <= 2 and self.enemy_toplayer_pieces[i] <= 2:
      actions.append(i+18)
    remove_actions.sort()
    return actions
  
    # 取り除けるのは自分のtoplayerかつ他のマスが動かすマスより小さいとき.
    remove_actions = []
    for i in range(9):
      if self.my_toplayer_pieces[i] == 0 and self.enemy_toplayer_pieces[i] == 0:
          actions.append(i)
      if self.my_toplayer_pieces[i] <= 1 and self.enemy_toplayer_pieces[i] <= 1:
          actions.append(i+9)
      if self.my_toplayer_pieces[i] <= 2 and self.enemy_toplayer_pieces[i] <= 2:
          actions.append(i+18)
    remove_actions.sort()
    return actions
  
  def is_first_player(self):
    """先手かどうか
    Returns:
      bool: 先手ならTrue, 後手ならFalse.
    """
    if self.player == 1:
      return True
    else:
      return False
  
  def __str__(self):
    """文字列表示
    このインスタンスをprint()やstr()で表示させるときのフォーマットを指定.
    現在の局面を文字列でグラフィカルに表示する.
    
      Todo:
        * unityなどを用いてGUIで出力させる.
      Returns
        str: 盤の状態を文字列表示で定義.
    """
    # is_first_player()で、今が自分の番か敵の番かを確認し、局面を正しく表示する.
    ox = ('o', 'x') if self.is_first_player() else ('x', 'o')
    str = ''
    for i in range(9):
      if self.my_toplayer_pieces[i] != 0:
        str += ox[0] + self.my_toplayer_pieces[i]
      elif self.enemy_toplayer_pieces[i] != 0:
        str += ox[1] + self.enemy_toplayer_pieces[i]
      else:
        str += '--'
      if i % 3 == 2:
        str += '\n'
    return str
    
