import os

if os.environ.get("APP_ENV") == "production":
    HOSTNAME = "73h.de"
    DATABASE = "blog"
    POKER_API = "https://poker.3doo.de/api/slack"
elif os.environ.get("APP_ENV") == "dev-8080":
    HOSTNAME = "73h-dev.de:8080"
    DATABASE = "blog-dev"
    POKER_API = "https://dev.poker.3doo.de/api/slack"
else:
    HOSTNAME = "73h-dev.de"
    DATABASE = "blog-dev"
    POKER_API = "https://dev.poker.3doo.de/api/slack"
