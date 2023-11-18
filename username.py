# クラス(データ型)の定義
class UserName:
    def __init__(self, name):
        #もしnameの文字数が4文字以上20文字以下でなければ
        if not (3 <= len(name) <= 20):
            # エラー文を表示して終了する
            raise ValueError(f"{name}はルール違反です")
        self.name = name

    def screen_name(self, new_name):
        # return self.name.upper()
        self.name = new_name.upper()
        return self.name

# UserNameクラスのインスタンス化
tanaka = UserName(name="tanaka")
bob = UserName(name="bob")
# 出力
print(tanaka.name)
print(bob.name)

# tanaka.screen_name("tanaka")
print(tanaka.screen_name("tanaka"))
