import re

text = """キリンは__複数名刺__の中で一番背が高い。
長い__体の一部__をどうやって獲得したのか。キリンの
身長は__数値__ __単位__近くあり、その高さのほとん
どは__体の一部__によるものだ。"""

def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力してください".format(word)
            new = input(q)
            mls = mls.replace(word,new,1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)

    else:
        print("引数mlsが無効です。")

mad_libs(text)
