# クラス(データ型)の定義
class UserName:
    def __init__(self, name):
        #もしnameの文字数が3文字以上20文字以下でなければ
        if not (3 <= len(name) <= 20):
            # エラー文を表示して終了する
            raise ValueError(f"{name}はルール違反です")
        if not name.islower():
            raise ValueError(f"{name}はアルファベットの小文字である必要があります")
        self.name = name

    def screen_name(self, new_name):
        # return self.name.upper()
        self.name = new_name.upper()
        return self.name


# UserNameクラスのインスタンス化
tanaka = UserName(name="tanaka")
bob = UserName(name="bob")
sato = UserName(name="sato")

# 出力
print(tanaka.name)
print(bob.name)
print(sato.name)


# tanaka.screen_name("tanaka")
print(tanaka.screen_name("tanaka"))
