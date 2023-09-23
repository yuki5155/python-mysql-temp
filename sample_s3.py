import boto3

# LocalStack の S3 サービスに接続
s3_client = boto3.client(
    's3',
    endpoint_url='http://localstack:4566',  # LocalStackのS3エンドポイント
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

def create_bucket(bucket_name):

    # バケット名
    bucket_name = 'my-bucket'

    # ローカルのS3にバケットを作成
    s3_client.create_bucket(Bucket=bucket_name)

    print(f"{bucket_name} has been created on local S3")

if __name__ == '__main__':
    create_bucket('my-bucket')