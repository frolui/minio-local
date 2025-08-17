# minio-local
Small repo with local minio cluster setup instruction

### Ports
127.0.0.1:9025 - S3 API
127.0.0.1:9026 - Web Console

1. run [install.sh](install.sh)
2. run [initiate.sh](initiate.sh)
3. run [initiate_bucket.sh](initiate_bucket.sh)
4. setup CORS configuration for MinIO if frontend will call MinIO API directly
```
mc admin config set local api cors="$(cat cors.json)"
mc admin service restart local
```
5. configure aws cli to use MinIO
```
aws configure --profile local-minio
<!-- AWS Access Key ID: minioadmin -->
<!-- AWS Secret Access Key: minioadmin123 -->
<!-- Default region name: us-east-1 -->
<!-- Default output format: json -->
```

### [how to connect from python](connect.py)

