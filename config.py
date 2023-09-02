# Server Configuration
HOST = '127.0.0.1'
PORT = 8080

# Database Configuration
DB_CONFIG = {
    'db': 'database_name',
    'user': 'username',
    'password': 'password',
    'host': 'localhost',
    'port': 3306,
    'autocommit': True
}

# JWT Configuration
SECRET_KEY = "secret_key_here"
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 3600  # 1 hour

# Email Configuration
EMAIL_CONFIG = {
    'SMTP_HOST': 'smtp_host',
    'SMTP_PORT': 587,
    'SMTP_USER': 'smtp_user',
    'SMTP_PASSWORD': 'smtp_password',
    'FROM_EMAIL': 'noreply@yourdomain.com'
}

# Elasticsearch Configuration
ELASTICSEARCH_CONFIG = {
    'host': 'localhost',
    'port': 9200
}

# Stripe Configuration
STRIPE_API_KEY = 'stripe_api_key'

# Cache Configuration (e.g., Redis)
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}

# File Storage Configuration (e.g., local or AWS S3)
FILE_STORAGE_CONFIG = {
    'STORAGE_TYPE': 'local',
    'LOCAL_STORAGE_DIR': '/path/to/storage/dir',
    # For AWS S3:
    # 'AWS_ACCESS_KEY': 'access_key',
    # 'AWS_SECRET_KEY': 'secret_key',
    # 'AWS_BUCKET_NAME': 'bucket_name'
}

# Celery Configuration
CELERY_CONFIG = {
    'BROKER_URL': 'redis://localhost:6379/1',
    'RESULT_BACKEND': 'redis://localhost:6379/2',
    'TASK_SERIALIZER': 'json',
    'RESULT_SERIALIZER': 'json',
    'ACCEPT_CONTENT': ['json'],
    'TIMEZONE': 'UTC',
    'ENABLE_UTC': True,
}

# Other configurations can be added as needed
