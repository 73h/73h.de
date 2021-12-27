import os

if os.environ.get("APP_ENV") == "production":
    HOSTNAME = "73h.de"
else:
    HOSTNAME = "73h-dev.de"
