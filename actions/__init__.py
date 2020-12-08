import os

# Slots from Rasa
NAME_SLOT = os.getenv("NAME_SLOT", "PERSON")
PRESENT_SLOT = os.getenv("PRESENT_SLOT", "product")

# Database configurations
DB_USER = os.getenv("DB_USER", "rasa_action_server")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "santa_bot")
