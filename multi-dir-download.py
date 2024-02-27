import boto3
import os
import configparser


def read_config():
    """Reads config.ini and returns the object

    Returns:
        object: config object
    """
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


def download_s3_directory(bucket_name, s3_directory, local_directory):
    paginator = s3.get_paginator("list_objects_v2")
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=s3_directory)

    for page in page_iterator:
        if "Contents" in page:
            for obj in page["Contents"]:
                key = obj["Key"]
                relative_path = key[len(s3_directory) :]
                file_path = os.path.join(local_directory, relative_path)

                # Create parent directories if needed
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                if obj["Key"].endswith("/"):
                    download_s3_directory(bucket_name, obj["Key"], file_path)
                else:
                    s3.download_file(bucket_name, obj["Key"], file_path)
                    print(f"Downloaded {key} to {file_path}")


config = read_config()

# AWS credentials and region
aws_access_key_id = config["AWS CREDENTIALS"]["ACCESS_KEY_ID"]
aws_secret_access_key = config["AWS CREDENTIALS"]["SECRET_ACCESS_KEY"]
aws_region = config["AWS CREDENTIALS"]["REGION"]

# Create an S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region,
)

# S3 bucket name and the subdirectory you want to download
bucket_name = config["AWS CREDENTIALS"]["BUCKET_NAME"]
s3_directory = config["AWS CREDENTIALS"]["S3_SUB_DIRECTORY"]

# Local directory to save the downloaded files
local_directory = config["AWS CREDENTIALS"]["LOCAL_DIRECTORY"]

# Create the local directory if it doesn't exist
if not os.path.exists(local_directory):
    os.makedirs(local_directory)


def main():
    try:
        download_s3_directory(bucket_name, s3_directory, local_directory)
        print("Download completed.")

    except Exception as e:
        print(f"Error occured: {str(e)}")


if __name__ == "__main__":
    main()