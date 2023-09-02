import boto3
from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME, S3_REGION

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=S3_REGION
)

def upload_file(file_path, object_name=None):
    """
    Upload a file to S3.
    
    Args:
    - file_path (str): The path to the file to upload.
    - object_name (str): The S3 object name. If not specified, the file name is used.
    
    Returns:
    - str: The URL of the uploaded file.
    """
    if object_name is None:
        object_name = file_path.split('/')[-1]

    s3_client.upload_file(file_path, S3_BUCKET_NAME, object_name)

    file_url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com/{object_name}"
    return file_url

def download_file(object_name, file_path):
    """
    Download a file from S3.
    
    Args:
    - object_name (str): The S3 object name.
    - file_path (str): The path to save the downloaded file.
    """
    s3_client.download_file(S3_BUCKET_NAME, object_name, file_path)

def delete_file(object_name):
    """
    Delete a file from S3.
    
    Args:
    - object_name (str): The S3 object name.
    """
    s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=object_name)
