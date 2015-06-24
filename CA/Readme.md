Example
        初期様相の作成　引数100はセル数
	mkrnd.py 100 > rnd.n100
	ソースファイル　ルール番号 ステップ数 初期様相 時間発展した様相
	ECA.py 90 100 rnd.n100 > tmp.res
	時間発展した様相をGUI(tkinter)で表示
	CAV.py tmp.res