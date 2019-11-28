import tictactoe as tic # クラスStateを定義.
import player_ai as ai  # ゲームAI.ミニマックスによる行動.ランダムな行動.
import random

# 3目並べの状態を保持するクラス"State"を初期化する。
state = tic.State()

# ファーストプレイヤーの抽選
player = pow(-1, random.randint(0,1) )

# ゲーム終了までループ。（Stateクラスのis_doneで確認）
while ( state.is_done() != True ) :
    # playerの入れ替え(playerは1,-1で切り替え)
    player *= -1
    
    # p1の行動選択
    if player == 1:
        print("Random Player\n" )
        action = ai.action( state, mode="Random" )
    # p2の行動選択
    if player == -1:
        print("MiniMax Player\n" )
        action = ai.action( state, mode="MiniMax"   )
        
    # 行動を状態に反映させた次の状態に更新する。
    state = state.next( action )

    # 表示
    print( state )
    print("空白")
    
