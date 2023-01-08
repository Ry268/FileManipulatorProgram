import sys

print(sys.argv)
argv_count = len(sys.argv)
print(f"argv count is {argv_count}")
command = sys.argv[1]
print(f"command is {command}")

# inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
if command == "reverse":
    if argv_count != 4:
        print("入力に間違いがあります")
        sys.exit()
    try:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        with open(inputpath) as f:
            inputpath_word = f.read()
            reverse_inputpath_word = inputpath_word[::-1]
        with open(outputpath, "w") as f:
            f.write(reverse_inputpath_word)
    except FileNotFoundError as e:
        print(f"{inputpath} not found.")
# inputpath にあるファイルのコピーを作成し、outputpath として保存します。
elif command == "copy":
    if argv_count != 4:
        print("入力に間違いがあります")
        sys.exit()
    try:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        with open(inputpath) as f:
            inputpath_word = f.read()
        with open(outputpath, "w") as f:
            f.write(inputpath_word)
    except FileNotFoundError as e:
        print(f"{inputpath} not found.")
# inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
elif command == "duplicate-contents":
    if argv_count != 4:
        print("入力に間違いがあります")
        sys.exit()
    try:
        inputpath = sys.argv[2]
        n = int(sys.argv[3])
        if n <= 0:
            print("0よりも大きい値を入力してください")
            sys.exit()
        with open(inputpath) as f:
            inputpath_word = f.read()
        with open(inputpath, "w") as f:
            f.write(inputpath_word * n)
    except ValueError:
        print("数字を入力してください")
    except FileNotFoundError as e:
        print(f"{inputpath} not found.")
# inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
elif command == "replace-string":
    if argv_count != 5:
        print("入力に間違いがあります")
        sys.exit()
    try:
        inputpath = sys.argv[2]
        needle = sys.argv[3]
        newstring = sys.argv[4]
        with open(inputpath) as f:
            inputpath_word = f.read()
            inputpath_word = inputpath_word.replace(needle, newstring)
        with open(inputpath, "w") as f:
            f.write(inputpath_word)
    except FileNotFoundError as e:
        print(f"{inputpath} not found.")
else:
    print("正しいコマンドを入力してください")