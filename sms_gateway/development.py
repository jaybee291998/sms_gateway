from sms_gateway.settings import *


# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

DEBUG = True

ALLOWED_HOSTS = ['guidancesmsgateway.pythonanywhere.com', '127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

print(STATIC_ROOT)

print("IM HERE deve")
print(f'secret key {SECRET_KEY}')