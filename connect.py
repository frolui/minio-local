import s3fs

# connect to local mimio bucket
ms = s3fs.S3FileSystem(
    key="minioadmin",
    secret="minioadmin123",
    client_kwargs={"endpoint_url": "http://127.0.0.1:9025"},
    config_kwargs={"s3":{"addressing_style":"path"}}
)
print(ms.ls("mybucket"))