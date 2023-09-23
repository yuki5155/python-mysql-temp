import boto3

# LocalStack の DynamoDB エンドポイントに接続
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localstack:4566',  # LocalStackのDynamoDBエンドポイント
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test',
)

# テーブルを作成
table_name = 'MyTable'
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {'AttributeName': 'Id', 'KeyType': 'HASH'},  # Partition key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'Id', 'AttributeType': 'N'},
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)

print(f"{table_name} has been created on local DynamoDB")
