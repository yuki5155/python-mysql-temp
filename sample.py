import pymysql
import os

# 環境変数から接続情報を取得
host = os.environ.get('DB_HOST')
port = int(os.environ.get('DB_PORT'))  # 環境変数は文字列なので数値に変換
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_NAME')

# MySQLに接続
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# カーソルを取得
cursor = connection.cursor()

# SQLクエリを実行
cursor.execute('SELECT DATABASE();')

# 結果を取得
result = cursor.fetchone()
print(result)

# リソースを解放
cursor.close()
connection.close()
