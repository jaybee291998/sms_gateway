from sms_gateway.settings import *

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")
PROD_HOSTS = os.getenv("PROD_HOSTS")
print(f'prd pass: {os.getenv("PROD_DB_PASS")}')
ALLOWED_HOSTS = []
ALLOWED_HOSTS.append(PROD_HOSTS)

STATIC_ROOT = '/home/guidancesmsgateway/sms_gateway/static'
# /home/guidancesmsgateway/sms_gateway

MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/guidancesmsgateway/sms_gateway/static/media'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guidancesmsgatew$default',
        'USER': 'guidancesmsgatew',
        'PASSWORD': os.getenv("PROD_DB_PASS"),
        'HOST': os.getenv("PROD_DB_HOST"),
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',
    'https://gleaming-queijadas-fca33f.netlify.app',
]

print("IM NOT HERE")