# Server Configuration
HOST = '127.0.0.1'
PORT = 8080

# Database Configuration
DB_CONFIG = {
    'db': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': 3306,
    'autocommit': True
}

# JWT Configuration
SECRET_KEY = "your_secret_key_here"
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 3600  # 1 hour

# Other configurations can be added as needed
