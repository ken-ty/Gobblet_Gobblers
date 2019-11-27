import tictactoe as tic # クラスStateを定義.
imprt player_ai as ai  # ゲームAI.ミニマックスによる行動.ランダムな行動.
import random

# 3目並べの状態を保持するクラス"State"を初期化する。
state = tic.State()

# ファーストプレイヤーの抽選
player = pow(-1, random.randint(0,1) )

# ゲーム終了までループ。（Stateクラスのis_doneで確認）
while ( state.is_done() ) :
    # playerの入れ替え(playerは1,-1で切り替え)
    player *= -1
    
    # p1の行動選択
    if player = 1
        action = ai.action( state, mode="Random" )
    # p2の行動選択
    if player = -1
        action = ai.action( state, mode="MiniMax"   )
        
    # 行動を状態に反映させる。
    state = state.update( action )

    # 表示
    print( state )
    print("空白")
    
