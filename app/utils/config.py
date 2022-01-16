import os

if os.environ.get("APP_ENV") == "production":
    PROTOCOL = "https://"
    HOSTNAME = "73h.de"
    DATABASE = "blog"
else:
    PROTOCOL = "http://"
    HOSTNAME = "73h-dev.de"
    DATABASE = "blog-dev"
