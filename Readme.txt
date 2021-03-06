Plot_seq.py

■更新履歴
16/10/08 初版作成

■構成
・Plot_seq.py				メインで使うスクリプト
・ScatterPlot2D.py			2次元の散布図を生成する関数オブジェクト
・ScatterPlot3D.py			3次元の散布図を生成する関数オブジェクト
・ParallelcoordsPlot.py		平行座標プロットを生成する関数オブジェクト
・実験データ(.datなど)		図を作成するための元データ

■概要
タブ区切りで書かれた実験データを読み込んでmatplotlibで図を自動生成するスクリプト
実験で得られた1回試行の解個体群の分布を見るときに使うことを想定して作成しました．
読み込んだファイルが2目的なら2次元，3目的なら3次元の散布図を作成します．
4目的以上なら平行座標プロットで出力されます．
空白行とかコメント行の読み飛ばしは作ってないのでどうなるか分かりません．
numpyとかmatplotlibが入ってないと動かないのでAnacondaとかpython(x,y)とか入れてください．

■用例
python Plot_seq.py -F ResultDTLZ3.dat -PF DTLZ3
ResultDTLZ3.datを読み込んで散布図/平行座標プロットを作成します．
-PFオプションはPF付近の解のみを抽出して作図してくれますが，散布図のときしか役に立ちません．

python Plot_seq.py -S Sample/DTLZ3 -PF DTLZ3
./Sample/DTLZ3ディレクトリを順に読み込んで*.datファイルから散布図/平行座標プロットを作成します．
該当するファイル数が多いと警告が出るかも
-PFオプションについては同上

■改善案
現在の仕様だと1目的目だけが大きな値を取ると2,3目的目が潰れて特徴が分かりづらい．各軸の目盛りの最大値を読み取って等しい長さに揃える改良はしたほうが良さそう．
