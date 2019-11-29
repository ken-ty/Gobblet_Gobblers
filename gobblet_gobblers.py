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
    
    # piecesizeの定義
    VOID   = 0
    SMALL  = 1
    MIDIUM = 2
    LARGE  = 3
    
    # 盤面に見えてる駒の状態(0|1|2|3), piecesize = 0, 1, 2, 3  (void, small, midium, large).
    my_toplayer_pieces    = [0] * 9
    enemy_toplayer_pieces = [0] * 9
    for plane_axis in range(9):
      for layer in range(3):
        pieces_size = layer + 1
        if self.my_pieces[plane_axis+9*layer] != VOID:
          my_toplayer_pieces[plane_axis]    = pieces_size
        elif self.enemy_pieces[plane_axis+9*layer] != VOID:
          enemy_toplayer_pieces[plane_axis] = pieces_size
    self.my_toplayer_pieces    = my_toplayer_pieces
    self.enemy_toplayer_pieces = enemy_toplayer_pieces
    
    # 手駒(1|2|3)のリスト.
    hand_my_pieces = []
    for layer in range(3):
      pieces_size = layer + 1
      use_my_pieces = my_pieces[9*layer : 9*layer + 9]
      num_not_use_my_pieces = 2 - use_my_pieces.count(pieces_size)
      for num in num_not_use_my_pieces:       
        hand_my_pieces.append(pieces_size)
    self.hand_my_pieces = hand_my_pieces
    
    # 盤上の動かせる駒(0~26, 手駒から出せるなら-1も加える.)
    # candidatesはtoplayerの1~3で駒情報を保持.
    # SMALLの駒は、移動先がないと動かせないが、ここでのmoveとは、toplayer or hand に属しているということである.
    can_move_my_pieces = None
    # 0(駒なし),2,3は、toplayerをコピーでOK.
    can_move_my_pieces_candidates = self.my_toplayer_pieces.copy()
    """
    # 1の駒のみ, 移動先のマスがあるか確認.
    for plane_axis in range(9):
      if can_move_my_pieces_candidates[plane_axis] == SMALL:
        not_put = 1
        for plane_axis_i in range(9):
          if self.my_toplayer_pieces[plane_axis_i] == VOID and self.enemy_toplayer_pieces[plane_axis_i] == VOID:
            not_put = 0
            break;
        if not_put:
          can_move_my_pieces_candidates[plane_axis] = 0:
    """
    # 候補を0~26のマスに直す.
    for plane_axis in range(9):
      if can_move_my_pieces_candidates[plane_axis] != VOID:
        pieces_size = can_move_my_pieces_candidates[plane_axis]
        layer = pieces_size -1
        can_move_my_pieces.append(plane_axis+9*layer)
    # 手駒を使い切ってなければ-1を加える.
    NUM_MAX_HAND_PIECES = 6
    if len(self.hand_my_pieces) < NUM_MAX_HAND_PIECES:
      """
      # small駒の判定はまだなし.後でここに実装.
      """
      can_move_my_pieces.append(-1)
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
        if y < 0 or 2 < y or x < 0 or 2 < x or self.enemy_toplayer_pieces[x+y*3] == VOID:
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
    for y in range(3):
      if is_comp(0, y, 1, 0):
        #デバッグ:
        #print("横まけ")
        return True
    for x in range(3):
      if is_comp(x, 0, 0, 1):
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
    
    現在の状態stateに選択した2つの行動actionを反映した、
    新しいStateを作成する。
    新しい局面では手番が入れ替わるため、
    my_piecesとenemy_piecesの返す順序を交換している。
    
    次のstateを作成するために使う。
    例: state = State(state.next( action ))
    Args:
      action (int, int): 第一引数で動かす駒の位置を指定する。手駒なら-1,盤上なら0~26、次に置くマスを0~26で指定.
    Returns:
      (enemy_pieces, my_pieces,player) (State): 行動を反映させたStateを返す.
    """
    
    # my_piecesの更新.
    my_pieces = self.my_pieces.copy() # リストだからcopyを使用.
    remove_action = action[0]
    put_action    = action[1]
    # 手駒からなら置くだけ.
    if remove_action == -1:
      my_pieces[put_action]    = 1
    # 盤上からなら取り除いてから置く.
    else:
      my_pieces[remove_action] = 0
      my_pieces[put_action]    = 1
      
    # enemy_piecesと更新したmy_piecesを入れ替えてStateを作成.
    # playerはマイナスをかけて交代している.
    return State(self.enemy_pieces, my_pieces, -self.player)

  def legal_actions(self):
    """合法手のリストの取得
    初めに、remove_actionsを作成する.
    そこから、remove_actionとput_actionという一連の単位actionを作成する.
    すべてのactionをリスト化し、actionsとして返す.
    Returns:
      actions: 合法手のリスト, list (remove_action, put_action)
    """
    """頑張る
    TODO: actionのさくせい
    action (int, int): 第一引数で動かす駒の位置を指定する。手駒なら-1,盤上なら0~26、次に置くマスを0~26で指定.
    # 全てのcan_move_my_piecesに対して駒を動かす合法手を考える.
    
    """
    # 全てのcan_move_my_piecesに対して駒を動かす合法手を考える.
    actions_cnt = 0
    for remove_action in can_move_my_pieces:
      # 手駒からでも、盤上の駒でも、置けるかの処理は変わらない。(動かすとき、自分のいたマスには行けないので、取り除いて比較する必要がない.)
      # 単純におけるかの確認.
      for plane_axis in range(9):
        for piece_size in range(SMALL, LARGE+1):
          if self.my_toplayer_pieces[plane_axis] < piece_size and self.enemy_toplayer_pieces[plane_axis] < piece_size:
            layer = piece_size - 1
            put_action = plane_axis + 9 * layer
            actions[actions_cnt] = remove_action, put_actions
            actions_cnt += 1
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
    
