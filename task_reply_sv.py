from flask import Flask, request, Response
import json
import os

from task_data import tasks

app = Flask(__name__)

@app.route('/get-course-data', methods=['GET'])
def get_course_data():
    # クエリパラメータからコース名を取得
    course_name = request.args.get('course_name')
    
    # 該当するコース情報を検索
#    result = next((item for item in tasks if item["course"] == course_name), None) #--- タイトルが１個だけのときは動いた。

    # 該当するコース情報を検索
    result = None
    for item in tasks:
        # courseがリストの場合の判定
        if isinstance(item["course"], list):
            if course_name in item["course"]:
                # 指定されたコース名のみを返す（リストを単一の値に変換）
                result = item.copy()  # オリジナルデータを保持するためコピー
                result["course"] = course_name
                break
        # courseが文字列の場合の判定
        elif isinstance(item["course"], str):
            if course_name == item["course"]:
                result = item
                break  
    
    # 該当データを返却
    if result:
        # JSONデータをUTF-8形式でレスポンス
        return Response(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")
    else:
        # エラーの場合も同様に対応
        return Response(
            json.dumps({"error": "該当するコースが見つかりません。"}, ensure_ascii=False),
            content_type="application/json; charset=utf-8",
            status=404
        )

if __name__ == '__main__':
#    app.run(debug=True)        #--- Local host

    port = int(os.environ.get('PORT', 8080))        #--- for Render用
    app.run(host ='0.0.0.0',port = port)

#    app.run(host="0.0.0.0", port=5000)

