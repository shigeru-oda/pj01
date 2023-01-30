# 1:単純なhello worldを出力する

sam init

sam build

sam deploy
https://xxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/Prod/hello


aws cloudformation describe-stack-resources --stack-name pj01-sam-app

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
aws lambda p --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --payload file://events/event.json --cli-binary-format raw-in-base64-out response.json; cat response.json


# 3:ローカルテスト
pip install pytest
pytest ./tests/unit/test_handler.py 

# 4:コンテナ化
REGION=$(aws configure get region)
ACCOUNTID=$(aws sts get-caller-identity --output text --query Account)

docker tag hello_world:latest ${ACCOUNTID}.dkr.ecr.${REGION}.amazonaws.com/hello_world:latest

aws ecr get-login-password | docker login --username AWS --password-stdin ${ACCOUNTID}.dkr.ecr.${REGION}.amazonaws.com

docker push ${ACCOUNTID}.dkr.ecr.${REGION}.amazonaws.com/hello_world:latest
DIGEST=$(aws ecr list-images --repository-name hello_world --out text --query 'imageIds[?imageTag==`latest`].imageDigest')
echo $DIGEST

sam deploy --image-repository ${ACCOUNTID}.dkr.ecr.${REGION}.amazonaws.com/hello_world@${DIGEST}

# 5:FastAPI
pip install mangum

