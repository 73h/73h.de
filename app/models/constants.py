import os

if os.environ.get("ENV") == "production":
    HOSTNAME = "73h.de"
else:
    HOSTNAME = "73h-dev.de"
