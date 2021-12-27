import os

if os.environ.get("APP_ENV") == "production":
    HOSTNAME = "73h.de"
    DATABASE = "blog"
else:
    HOSTNAME = "73h-dev.de"
    DATABASE = "blog-dev"
