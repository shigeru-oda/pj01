# 1:単純なhello worldを出力する

sam init

sam build

sam deploy
https://xxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/Prod/hello



# 2:ローカル実行
ローカルで関数を直接呼び出し
sam local invoke

ローカルで関数を直接呼び出し（Lambdaのリソース名を指定）
sam local invoke HelloWorldFunction

ローカルでAPI GATEWAY経由で実行
sam local start-api
http://127.0.0.1:3000/hello

エンドポイント経由で実行
sam local start-lambda
aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --payload file://events/event.json --cli-binary-format raw-in-base64-out response.json; cat response.json


# 3:ローカルテスト
pip install pytest
pytest ./tests/unit/test_handler.py 