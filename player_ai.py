import tictactoe as tic

def action( state, mode="Random" )
  """現在の状態から思考ルーチンに沿って行動を生成する.
  Arg:
  state (tic.State): 現在の局面.
  mode (str): 思考ルーチンの選択.
              整数か文字列で指定する.
              デフォルトはランダム.
              思考ルーチン:
              -  "Random"
              -  "MiniMax" 
  """
  
  if mode = "Random":
    # 合法手を取得し、その中からランダムに行動を選択する.
    legal_actions = state.legal_actions()
    random_action = legal_actions[random.randint(0, len(legal_actions)-1)]
    return random_action

  elif mode = "MiniMax:
    score       = -float( 'inf' ) #  行動の価値.
    best_score  = -float( 'inf' ) # 最も高い行動の価値.
    best_action = 0               # 最も価値の高い行動.

    # 全ての合法手に対して、価値を計算.
    for action in state.legal_actions():
        # 価値を取得
        score = mini_max( state.next( action ) )
        # 価値が高いなら更新
        if score > best_score:
            best_action = action
            best_score  = score
    mini_max_action = best_action
    return mini_max_action
  
  else:
    print("error: mode not found.\n")
