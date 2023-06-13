def translate_ascii_code(code):
    if code < 0 or code > 127:
        return "Invalid ASCII code"
    else:
        return chr(code)

# ASCIIコードを入力してください
code = int(input("ASCIIコードを入力してください: "))

# ASCIIコードを翻訳して文字に変換
character = translate_ascii_code(code)

# 結果を表示
print(f"ASCIIコード {code} は文字 '{character}' に翻訳されます。")
