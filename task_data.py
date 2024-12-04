tasks = [
     {
        "course": "Python基礎【3013】",
        "answer": "# 関数Ai_demyの中を作成してください\ndef Ai_demy(numbers):\n    # ここに処理を記述してください\n    for n in numbers:\n        if n % 5 == 0 and n % 7 == 0:\n            print(\"{}:Aidemy\".format(n))\n        elif n % 5 == 0:\n            print(\"{}:Ai\".format(n))\n        elif n % 7 == 0:\n            print(\"{}:demy\".format(n))\n        else:\n            print(n)\n    \n# データの定義\nnumbers = list(range(1,36))\n# 関数の実行\nAi_demy(numbers)",
        "correct_response": "Python基礎【3013】の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\nPython基礎【3013】の添削課題を返却いたします。\n正解です。\n\nご提出いただきましたコードを拝見しますと本講座の内容について\nしっかりと、ご理解いただいているように感じます。\n素晴らしいです。\n\n引き続きぜひこの調子で頑張ってください。\n次回の提出もお待ちしております。",
        "incorrect_response": "Python基礎【3013】 の添削問題のご提出ありがとうございます。\n添削結果を返却致します。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\nPython基礎【3013】 の添削課題のご提出お疲れさまでした。\n 残念ながら不正解です。\n\n{{修正コメント}}\n\n解答例を添付いたしますので、内容のご確認をお願いいたします。\n\n再提出の必要はございませんので、先に、お進みください。\n次回の提出もお待ちしております。"
    },
    
    {
        "course": "Python基礎【3013】_応用問題",
        "answer": "# バイナリーサーチを行う関数\ndef binary_search(numbers, target_number):\n    # 最小値を仮決め\n    low = 0\n    # 範囲内の最大値\n    high = len(numbers) - 1\n    # 目的地を探し出すまでループ\n    while low <= high:\n        # 中央値を求める（index）\n        middle = (low + high) // 2\n        # 中央値のnumbersの値とtarget_numberが等しい場合\n        if numbers[middle] == target_number:\n            # 出力\n            middle+=1\n            print(\"{1}は{0}番目にあります\".format(middle, target_number))\n            # 終了させる\n            break\n        # 中央値のnumbersの値がtarget_numberより小さい場合\n        elif numbers[middle] < target_number:\n            low = middle + 1\n        # 中央値のnumbersの値がtarget_numberより大きい場合\n        else:\n            high = middle - 1\n\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]\ntarget_number = 11\nbinary_search(numbers, target_number)",
        "correct_response": "{{コース}}の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\nPython基礎【3013】の応用添削課題を返却いたします。\n正解です。\n\n大変素晴らしいです。\nバイナリーサーチは、ソートされたリストからターゲット値を効率的に検索するアルゴリズムです。\n\n解答例を添付いたしますので、お手隙のときにご確認ください。\n\n次回の提出もお待ちしております。",
        "incorrect_response": "{{コース}}の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\nPython基礎【3013】の応用添削課題を返却いたします。\n 残念ながら不正解です。\n\n{{修正コメント}}\n\n解答例を添付いたしますので、内容のご確認をお願いいたします。\n\n再提出の必要はございませんので、先にお進みください。\n次回の提出もお待ちしております。"
    },

    {
        "course": "【新】ライブラリ「NumPy」基礎（数値計算）【4004】",
        "answer": "# 必要なライブラリをimport\nimport numpy as np\nimport time\nfrom numpy.random import rand\n\n# 行、列の大きさ\nN = 5000\n\n# 配列の初期化\nmat = rand(N, N)\n\n# Numpyの機能を使わずに計算\n\n# 開始時間の取得\nstart = time.time()\n\n# for文を使って、1番目の軸に沿って平均を計算\nmean_not_numpy = []\nfor i in range(N):\n    mean_not_numpy.append(sum(mat[i]) / len(mat[i]))\n\n# 出力形式を整えるため、numpy配列に変換\nprint(np.array(mean_not_numpy))\nprint(f'Total time when not using NumPy：{(time.time() - start):.2f}[sec]')\nprint()\n\n# NumPyを使って計算\n\n# 開始時間の取得\nstart = time.time()\n\n# NumPyの機能を使って、1番目の軸に沿って平均を計算\nmean_numpy = mat.mean(axis=1)\n\nprint(mean_numpy)\nprint(f'Total time when using NumPy：{(time.time() - start):.2f}[sec]')",
        "correct_response": "{{コース}}の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\n「NumPy」基礎（数値計算）【4004】の添削課題のご提出お疲れさまでした。\n正解です。\n\n今回の添削課題において、\nfor文とNumpyによる計算処理速度を比較いただいたことで、\nNumpyの計算処理性能の高さを実感いただけたと思います。\n\n引き続き、頑張っていきましょう。\n次回の課題提出をお待ちしております。",
        "incorrect_response": "{{コース}}の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\n「NumPy」基礎（数値計算）【4004】の添削課題のご提出お疲れさまでした。\n 残念ながら不正解です。\n\n{{修正コメント}}\n\n解答例を添付いたしますので、内容のご確認をお願いいたします。\n\n再提出の必要はございませんので、先に、お進みください。\n次回の提出もお待ちしております。"
    }
    ,
    {
        "course": "【新】ライブラリ「NumPy」基礎（数値計算）【4004】_応用問題",
        "answer": "#====応用課題=====\nimport numpy as np\n\n# 乱数の初期化\nnp.random.seed(0)\n\n# 指定された大きさの画像を乱数を用いて生成する関数\n# 仮引数mは画像の縦の大きさ、nは画像の横の大きさです\ndef make_image(m, n):\n    \n    # m×n行列の各成分を0~5の値でランダムに満たしてください\n    image = np.random.randint(0, 6, (m, n))\n        \n    return image\n\n\n# 渡された行列の一部を変更する関数\ndef change_matrix(matrix):\n    # 与えられた行列の形を取得し、shapeに代入してください\n    shape = matrix.shape\n    \n    # 行列の各成分について、変更するかしないかをランダムに決めた上で\n    # 変更する場合は0~5のいずれかの整数にランダムに入れ替えてください\n    for i in range(shape[0]):\n        for j in range(shape[1]):\n            if np.random.randint(0, 2)==1:\n                matrix[i][j] = np.random.randint(0, 6, 1)\n    return matrix\n\n# ランダムに画像を作成\nimage1 = make_image(3, 3)\nprint(image1)\nprint()\n\n# ランダムに変更を適用する\nimage2 = change_matrix(np.copy(image1))\nprint(image2)\nprint()\n\n# image1とimage2の差分を計算し、image3に代入してください\nimage3 = image2 - image1\nprint(image3)\nprint()\n\n# image3の各成分が絶対値である行列をもとめimage3に再代入してください\nimage3 = np.abs(image3)\n\n# image3を出力\nprint(image3)\n",
        "correct_response": "「NumPy」基礎（数値計算）【4004】の応用添削課題のご提出お疲れさまでした。\n正解です。\n\n適切にコードが書かれていて大変素晴らしいです\n解答例も添付いたしますので、お手すきの際にご確認いただけると幸いです。\n\n引き続き、頑張っていきましょう。\n次回の課題提出をお待ちしております。",
        "incorrect_response": "「NumPy」基礎（数値計算）【4004】の応用添削課題のご提出お疲れさまでした。\n 残念ながら不正解です。\n\n{{修正コメント}}\n\n解答例を添付いたしますので、内容のご確認をお願いいたします。\n\n再提出の必要はございませんので、先に、お進みください。\n次回の提出もお待ちしております。"
    },
    {
        "course": "〔新〕ライブラリ「Pandas」基礎（表計算）【4014】",
        "answer": "import pandas as pd\n\nstore_data = {\n    \"store\": [\"shibuya\", \"shinjuku\", \"yokohama\", \"meguro\", \"ikebukuro\"],\n    \"ID\": [1, 2, 3, 4, 5]\n}\nstore_df = pd.DataFrame(store_data)  # store_dfを作成\n\ndata = {\"ID\": [1, 2, 3, 3, 2, 1],\n        \"product\": [\"banana\", \"orange\", \"orange\", \"grape\", \"banana\", \"peach\"],\n        \"price\": [200, 1000, 800, 100, 250, 900],\n        \"quantity\": [1, 2, 1, 2, 3, 2]}\ndf = pd.DataFrame(data)  # dfを作成\n\nprint(df)  # DataFrame 、dfの出力\nprint()\nprint(store_df)  # DataFrame、store_dfの出力\nprint()\n\n# 問題1\n# dfのインデックスが０から４までの要素、カラム名を出力してください。\ndf_1 = df.head()\nprint(df_1)\nprint()\n\n# 問題2\n# df とstore_dfをkeyをIDとして完全外部結合してください。\ndf_2 = pd.merge(df, store_df, on='ID', how='outer')\nprint(df_2)\nprint()\n\n# 問題3\n# df とstore_dfをkeyをIDとして内部結合してください。\ndf_3 = pd.merge(df, store_df, on='ID', how='inner')\nprint(df_3)\nprint()\n\n# 問題4\n# 問題3の回答にて作成したdf_3とgroupbyメソッドを用いてstore毎のID、price、quantityの平均値を出力してください。\ndf_4 = df_3.loc[:,[\"price\", \"quantity\", \"store\"]].groupby('store').mean()\nprint(df_4)\nprint()\n\n# 問題5\n# 問題3の回答にて作成したdf_3とdescribeメソッドを用いてID、price、quantityの要約統計量を出力してください。\ndf_5 = df_3.describe()\nprint(df_5)",
        "correct_response": "{{コース}}の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\n{{コース}}の添削課題の提出お疲れ様でした。\n正解です。\n\nしっかりとデータの表示やデータフレーム同士の\n内部・外部結合、および要約統計量を出力できております。\n\n解答例をお送りいたしますので、お手隙の際にご確認のほど宜しくお願いいたします。\n\nPandasは実際のデータ分析でも多用される代表的なライブラリです。\nこの機会にしっかり覚えていただければと思います\n\nこの調子でがんばっていきましょう！\n次回の添削問題もお待ちしております。",
        "incorrect_response": "{{コース}}の添削課題のご提出ありがとうございます。\n添削結果を返却いたします。\nーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー\n\n{{コース}}の添削課題の提出お疲れ様でした。\n 残念ながら不正解です。\n\n{{修正コメント}}\n\n解答例を添付いたしますので、内容のご確認をお願いいたします。\n\n再提出の必要はございませんので、先に、お進みください。\n次回の提出もお待ちしております。"
    }
]