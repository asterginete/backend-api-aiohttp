backend-api-aiohttp
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── users.py
│   │   ├── orders.py
│   │   ├── products.py
│   │   ├── categories.py
│   │   ├── comments.py
│   │   └── ratings.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── items.py
│   │   ├── users.py
│   │   ├── orders.py
│   │   ├── products.py
│   │   ├── categories.py
│   │   ├── comments.py
│   │   ├── ratings.py
│   │   ├── tokens.py
│   │   └── user_socials.py
│   │
│   ├── middlewares/
│   │   ├── __init__.py
│   │   ├── jwt_middleware.py
│   │   └── rate_limiter.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── email_service.py
│   │   ├── search_service.py
│   │   ├── payment_service.py
│   │   └── recommendation_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── validators.py
│   │   ├── cache.py
│   │   └── file_storage.py
│   │
│   └── tasks/
│       ├── __init__.py
│       ├── email_tasks.py
│       └── data_processing_tasks.py
│
├── migrations/
│
├── tests/
│   ├── __init__.py
│   ├── test_items.py
│   ├── test_users.py
│   └── ... (other test modules)
│
├── static/
│   ├── images/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── user/
│   ├── admin/
│   └── common/
│
├── config.py
├── requirements.txt
└── main.py
