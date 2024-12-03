import oss2
import os

# 阿里云 OSS 配置信息
access_key_id = os.getenv('OSS_ACCESS_KEY_ID')
access_key_secret = os.getenv('OSS_ACCESS_KEY_SECRET')
bucket_name = 'your-bucket-name'
endpoint = 'your-oss-endpoint'

# 初始化 OSS 配置
auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

# 文件路径
file_path = 'example.txt'
object_name = 'example.txt'  # 上传到 OSS 后的文件名

# 上传文件
bucket.put_object_from_file(object_name, file_path)
print(f'File {file_path} uploaded to OSS as {object_name}')
