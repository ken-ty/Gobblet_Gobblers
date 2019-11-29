# Gobblet Gobblers
Gobblet GobblersのAiを作成.

## What's "Gobblet Gobblers" ?

日本国内の正規輸入代理店「すごろくや」の紹介ページ  
https://sgrk.blog.fc2.com/blog-entry-3687.html  

正規ルールと違う点として、
持ち上げた際にできる3並びについては考慮してないです。  
簡単のためです。今後対応します。  

## ファイル構成
├─ main.py              # シミュレーション.  
├─ player_ai.py         # ゲームAI.指定したアルゴリズムで行動を決定.  
├─ statevalue.py        # 指定したアルゴリズムで状態価値を決定.  
└─ gobblet_gobblers.py  # クラスStateを定義.  

## 推奨環境
Anaconda Prompt を推奨します。
ただし、Pythonが実行できる環境であれば、なんでも構いません。

## 実行方法
1. Anaconda https://www.anaconda.com/ をインストール.
1. Gobblet Gobblersをダウンロード.
1. Anaconda Prompt を実行
1. Promptに"python "と入力. (行末のスペースを忘れずに!)
1. ダウンロードしたGobblet Gobblersから、main.pyをAnaconda Promptにドラック&ドロップしてください.
1. Promptには、"phtyon [パス]/main.py"となっているはずです。そのままEnterで実行できます.

1. main.pyを書き換えることで、MiniMaxプレイヤー同士のゲームを見ることができます!  
※ 書き換え済みverは、"players_are_MiniMax"ブランチからダウンロードできます.

### 参考文献

布留川英一(2019) 『AlphaZero 深層学習・強化学習・探索 人工知能プログラミング実践入門』 ボーンデジタル.  
https://www.borndigital.co.jp/book/14383.html  
