# pip install bitarray
import hashlib

# ブルームフィルター
class bfindex:
    # 初期化
    def __init__(self, m=64, k=3):
        # ビット長の長さ
        self.m = m
        # 登録するインデックス数
        self.k = k
        # いくつ登録したかを保存
        self.count = 0
        # ビット列
        self.bit = 0b0

    # キーワードの追加
    def add(self, key):
        # k以上登録しないようにする
        if self.count < self.k:
            # ハッシュを求め、ビット列に登録
            self._set(self._hash(key))
            # 登録した数
            self.count += 1

    # ビット列の中に登録されているかどうか
    def check(self, key):
        # keyからハッシュ値を求める
        value = self._hash(key)
        # 保存されているビット列とkeyのハッシュが存在するかを求める
        for v, b in zip(bin(value)[2:], bin(self.bit)[2:]):
            # keyが1の場合に登録されているビット列も1なのかどうかを確認
            # 違ったら登録されていない。なので、Falseを返す
            if v == '1' and v != b:
                return False
        else:
            # 最後までループが回ったら、二つのビット形式を表示して、Trueを返す
            print(bin(self.bit)[2:], bin(value)[2:])
            return True

    # ビット列の加算（OR）
    def _set(self, value):
        self.bit |= value

    # ハッシュ値の計算
    def _hash(self, key):
        # sha256でハッシュを求め、10進数に変換し2進数に変換する。
        # その後、m個分のビット列を返す
        value = int(bin(int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16))[:self.m + 2], 2)
        return value


# 実行テスト
if __name__ == "__main__":
    b = bfindex(m=254)
    # b.add('start')
    # b.add('stop')
    # b.add('ky')
    # print(bin(b.bit))
    b.add('gagasg')
    b.add('babasa')
    b.add('basag3e4')
    print(bin(b.bit))


    # b.add('aba3a')
    # b.add('asdba')
    # b.add('hwer')
    # print(bin(b.bit))

    # b.add('starhshfsdht')
    # b.add('j6jrdjhdf')
    # b.add('uytkuytr')
    # print(bin(b.bit))


    print(b.check('start'))
    print(b.check('kaishi'))
    print(b.check('stop'))
    print(b.check('ky'))
    print(b.check('kasy'))
    print(b.check('baka'))