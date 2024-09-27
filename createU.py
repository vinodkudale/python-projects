import boto3
import os

s3 = boto3.resource("s3")

def create_bucket(s3, bucket_name):
    try:
        # Create the bucket without LocationConstraint for us-east-1
        s3.create_bucket(Bucket="python-upload-create")
        print("Bucket successfully created")
    except Exception as e:
        print(f"Error: {e}")

def upload_backup(s3, file_name, bucket_name, key_name):
    try:
        # Check if the file exists
        if not os.path.exists(file_name):
            print(f"File {file_name} does not exist.")
            return
        
        # Upload the file to S3
        with open(file_name, 'rb') as data:
            s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
        print("Backup uploaded successfully")
    except Exception as e:
        print(f"Error: {e}")

bucket_name = "python-upload-create"
file_name = "/Users/vinod/OneDrive/Desktop/python-devops/backups/backeup_2024-09-27.tar.gz"
key_name = "vk-backup.tar.gz"

# Create the bucket (uncomment if you want to create it each time)
create_bucket(s3, bucket_name)

# Upload the backup
upload_backup(s3, file_name, bucket_name, key_name)
