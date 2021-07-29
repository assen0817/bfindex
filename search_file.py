from File import check_file

print("終了時は、CTRL+C Enter")

# データの入力を開始する
try:
    while True:
        # 検索内容を入力
        search_data = input('検索内容：')
        # 検索内容が含まれているファイルを探す
        result = check_file(search_data)

        # 結果を出力
        print(f'検索内容が含まれているファイル:{result}')
except KeyboardInterrupt:
    pass