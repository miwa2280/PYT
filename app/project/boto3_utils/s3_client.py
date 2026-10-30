import boto3
from pathlib import Path
from pprint import pprint

import config

s3client = boto3.client(
    service_name='s3',
    region_name=config.AWS_REGION_NAME,
    endpoint_url=config.AWS_ENDPOINT_URL,
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY,
)

target_file_name = 'images/audi_2.jpg'

# Формируем абсолютный путь к файлу относительно текущего файла
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / 'Audi_A6_2.jpg'  # настройте количество .parent, если файл лежит в другом месте

s3client.upload_file(str(file_path), config.AWS_BUCKET_NAME, target_file_name)

# READ - выводим публичную ссылку в терминал
public_url = f"{config.AWS_PUBLIC_URL}/{target_file_name}"
print(public_url)

# response = s3client.list_objects_v2(Bucket=config.AWS_BUCKET_NAME)
# pprint(response)

# s3client.download_file(config.AWS_BUCKET_NAME, target_file_name, "555.jpg")

# s3client.delete_object(Bucket=config.AWS_BUCKET_NAME, Key=target_file_name)