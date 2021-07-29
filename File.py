from BloomFilte import bfindex


# ブルームフィルターのビット列
m=64
# 登録可能キーワード数
k=3


# ファイルへの書き込み
# ファイル名、データ内容、日付
def write(file_name, data, date):
    # バイナリ登録用のファイル名と名前が被らないように避ける
    if file_name == 'binary_data':
        print('ファイル名を変えてください')
        return 'ファイル名を変えてください'

    # ファイル名がぶつからないように存在していたらエラーを取得
    # ファイルが存在することを返す
    try:
        # 入力したfile_nameでファイルを作成する
        with open(f'data/{file_name}.txt', mode='x') as f:
            # データ内容を記入
            f.write(f'{data}\n')
            # 日付の記入
            f.write(f'{date}\n')
    except FileExistsError:
        print('ファイルはもう存在します。')
        return 'ファイルはもう存在します。'
    # m個のビット列とk個の登録制限でブルームフィルターを作る
    b = bfindex(m=m, k=k)
    # ビット列にデータを登録
    b.add(file_name)
    b.add(data)
    b.add(date)

    # バイナリ管理用のファイルに計算したビット列とファイルの名前を登録
    with open(f'data/binary_data.txt', mode='a') as f:
        f.write(f'{b.bit}, {file_name}\n')


# バイナリファイルのバイナリにkeyのバイナリが登録されているかどうか
def check_file(key):
    # 見つかったファイル名を出力用に保存する
    result = {}
    # バイナリーファイルを検索
    with open('data/binary_data.txt') as f:
        # 一行ごとに読み込み
        ls = f.readlines()
        for l in ls:
            # ,での区切りでバイナリとファイル名を取得
            s = l.split(', ')
            # ブルームフィルターをセット
            b = bfindex(m=m, k=k)
            # ファイルのバイナリをブルームフィルターセットし、
            # 上限値を入れておく
            b._set(int(s[0]))
            b.count = k
            # バイナリにkeyの値が入っているかどうか
            if b.check(key):
                # 入っていれば、ファイル名を取得
                file_name = s[1].split('\n')[0]

                # keyとファイル名が一緒なら、それを記録
                # true positiveも記録し、次のデータを見る
                if file_name == key:
                    result[file_name] = 'true positive'
                    print('true positive')
                    continue


                # ファイルの中身を確認する
                with open(f'data/{file_name}.txt') as fn:
                    # 一行ずつ中身を見る
                    fls = fn.readlines()
                    for fl in fls:
                        # ファイルの中身のデータとkeyが一緒なら、そのファイル名を記録
                        # true positiveも記録し、次のデータを見る
                        if fl.split('\n')[0] == key:
                            print('true positive')
                            result[file_name] = 'true positive'
                            break
                    else:
                        # ファイルの中身とマッチングせずに、ループが終わったら、そのファイル名を記録
                        # false positiveも記録する
                        result[file_name] = 'false positive'
                        print('false positive')

    # 結果を返す
    return result