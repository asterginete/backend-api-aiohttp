import pytest
from app.utils.validators import validate_email, validate_password, validate_date, validate_price
from app.utils.file_storage import upload_file, download_file, delete_file

# Tests for validators

def test_validate_email():
    assert validate_email("test@example.com")
    assert not validate_email("test")

def test_validate_password():
    assert validate_password("Test@1234")
    assert not validate_password("test")

def test_validate_date():
    assert validate_date("2022-05-15")
    assert not validate_date("15-05-2022")

def test_validate_price():
    assert validate_price(10.5)
    assert not validate_price(-5)

# Tests for file storage (mocked for the purpose of this example)

def test_upload_file(mocker):
    mocker.patch('app.utils.file_storage.s3_client.upload_file', return_value=True)
    assert upload_file("path/to/file.txt", "file.txt") == f"https://your_bucket_name.s3.your_region.amazonaws.com/file.txt"

def test_download_file(mocker):
    mocker.patch('app.utils.file_storage.s3_client.download_file', return_value=True)
    download_file("file.txt", "path/to/downloaded/file.txt")

def test_delete_file(mocker):
    mocker.patch('app.utils.file_storage.s3_client.delete_object', return_value=True)
    delete_file("file.txt")

