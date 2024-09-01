from uuid import uuid4

base_configs = {
    "production": {
        "DEBUG": 'False',
        "TESTING": 'False',
        "SECRET_KEY": uuid4().hex,
        "SESSION_COOKIE_SECURE": 'True',
        "CORS_HEADERS": "Content-Type",
        "JWT_SECRET_KEY": uuid4().hex,
    },
    "development": {
        "DEBUG": 'True',
        "TESTING": 'True',
        "SECRET_KEY": "secret",
        "SESSION_COOKIE_SECURE": 'True',
        "CORS_HEADERS": "Content-Type",
        "JWT_SECRET_KEY": "secret",
    }
}
