# S3 Directory Downloader
This Python script allows you to download an entire directory (including subdirectories and files) from an Amazon S3 bucket to your local machine. It utilizes the AWS SDK for Python (Boto3) and reads configuration settings from a config.ini file.

## Features
Download entire directories from Amazon S3.
Support for downloading subdirectories and files recursively.
Easy configuration using a config.ini file.
Error handling and logging for robustness.

## Requirements
To run the script, you need the following:

Python 3.x
boto3

## Installation
1. Clone the repository to your local machine: `git clone https://github.com/Shubham268Mishra/AWS-Multidirectory-Download.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Configuration
Before running the script, make sure to configure the config.ini file with your AWS credentials and other settings.

Sample config.ini:
```
[AWS CREDENTIALS]
ACCESS_KEY_ID =your_access_key_id
SECRET_ACCESS_KEY =your_secret_access_key
REGION =your_region
BUCKET_NAME =your_bucket_name
S3_SUB_DIRECTORY =your_s3_sub_directory
LOCAL_DIRECTORY =your_local_directory
```
## Usage
To download an S3 directory, follow these steps:

Ensure that the config.ini file is properly configured with your AWS credentials, S3 bucket details, and local directory path.

Run the script: `python multi-dir-download.py`

The script will download the specified S3 directory to your local machine.