# はじめに
CNN等の画像分類タスクでモデルを作る際に学習データを作るためのプログラム群です．

# 動作確認済みライブラリ＆バージョン
- python 3.8.5
- tqdm 4.51
- numpy 1.19.1
- opencv 4.0.1

# ラベリング(アノテーション)
ラベリングは[VoTT](https://github.com/microsoft/VoTT)を使います．
[参考](https://sleepless-se.net/2019/06/21/how-to-use-vott/)

# 使い方
このリポジトリをクローンしたファイルに以下のフォルダを作ります．
- images(モデルに利用したい画像をディレクトリ直下に保存)
- json_files(VoTTで生成されたJSONを入れる)
- original_images(画像が階層構造になっている時のみ)
- training_images(この配下にディレクトリを切って学習データが保存される)

## 学習させたいデータがディレクトリ構造になっている人だけ
例えば(/01/hoge.bmp)になっている時
学習させたいデータをoriginal_imagesに入れてください
その後
rename_image_files.pyのIMAGE_EXTENSIONを自分が使いたい拡張子に変えてください． 
下記コマンドを実行
> python rename_image_files.py

imagesフォルダに画像が出来ていることを確認する.

## VoTTを使ったラベリング
VoTTの画像のディレクトリをimagesに設定し，JSONの掃き出し先をjson_filesに設定する．
[参考](https://sleepless-se.net/2019/06/21/how-to-use-vott/)を参考にし，ラベリングを行う．

## 教師データの作成
main.pyのIMAGE_FILE_EXTENSIONを設定してください(デフォルトはbmpになっています)．
下記コマンドを実行
> python main.py

training_imagesディレクトリの配下にラベルごとにディレクトリが出来ていて，その下にVoTTでバウンディングボックスを設定した範囲の画像が出来ていることを確認する．


# 各ファイルについて
* main.py  
VoTTで生成されたJSONとimagesに入っている画像を元にラベリングをし，training_imagesのディレクトリに教師データを保存します．
* rename_image_files.py  
元画像がディレクトリ直下に入っていない時に，ディレクトリ直下に画像を保存し，名前を整えるために使います．
