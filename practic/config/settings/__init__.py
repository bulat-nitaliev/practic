from config.settings.base import *

DEBUG = True

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent.parent

print(BASE_DIR)

# DEBUG = False

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True