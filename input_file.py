from File import write

print("終了時は、CTRL+C Enter")
# データの入力を開始する
try:
    while True:
        # ファイル名を入力
        file_name = input('フィアルの名前を入力下さい：')
        # データを入力
        data = input('データを入力ください：')
        # 日付を入力
        date = input('日付を入力ください：')

        # ファイルに書き込む
        write(file_name, data, date)
except KeyboardInterrupt:
    pass