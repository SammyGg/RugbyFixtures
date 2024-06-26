# prod
import os
from .settings import *
from .settings import BASE_DIR

# print ("Starting pr_dep")
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]

DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



#A2
# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
#     },
# }


DATABASES = {
    'default': {
        'ENGINE': 'mssql',  # Use 'mssql' for django-mssql-backend
        'NAME': 'DWH_DB',
        'USER': os.getenv('ggUserName', 'default_password'),
        'PASSWORD': os.getenv('ggPassword', 'default_password'),
        'HOST':  "fapr-prod-dwh-sql01.database.windows.net", #os.getenv('ggHostServerName', 'default_password'), 
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=no;Connection Timeout=30;',
        },
    },
}


# A2
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC_ROOT =BASE_DIR/'staticfiles'
SECRET_KEY = os.environ['RFAPP_SECRET_KEY']


#A3 - CHaptgpt
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# # Ensure this is set up if you are using a different storage backend for static files
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage' 
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',  # Use 'mssql' for django-mssql-backend
#         'NAME': 'DWH_DB',
#         'USER': os.getenv('ggUserName', 'default_password'),
#         'PASSWORD': os.getenv('ggPassword', 'default_password'),
#         'HOST':  "fapr-prod-dwh-sql01.database.windows.net", #os.getenv('ggHostServerName', 'default_password'), 
#         'PORT': '1433',

#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#             'extra_params': 'TrustServerCertificate=no;Connection Timeout=30;',
#         },
#     },
# }


