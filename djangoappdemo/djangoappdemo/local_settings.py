import os

with open('etc/ket.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '10.0.2.235',
    'localhost',
    '127.0.0.1'
]