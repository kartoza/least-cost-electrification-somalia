# coding=utf-8

"""Project level settings."""
from .base import *  # noqa

# Comment if you are not running behind proxy
USE_X_FORWARDED_HOST = ast.literal_eval(
    os.getenv('USE_X_FORWARDED_HOST', 'True'))


if EMAIL_ENABLE:
    # See fig.yml file for postfix container definition#
    EMAIL_BACKEND = os.getenv(
        'DJANGO_EMAIL_BACKEND',
        default='django.core.mail.backends.smtp.EmailBackend')
    # Host for sending e-mail.
    EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'smtp')
    # Port for sending e-mail.
    EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT', 25)
    # SMTP authentication information for EMAIL_HOST.
    # See fig.yml for where these are defined
    EMAIL_HOST_USER = os.getenv(
        'DJANGO_EMAIL_HOST_USER', 'noreply@kartoza.com')
    EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', 'docker')
    EMAIL_USE_TLS = ast.literal_eval(os.getenv(
        'DJANGO_EMAIL_USE_TLS', 'False'))
    EMAIL_USE_SSL = ast.literal_eval(os.getenv(
        'DJANGO_EMAIL_USE_SSL', 'False'))
else:
    EMAIL_BACKEND = os.getenv(
        'DJANGO_EMAIL_BACKEND',
        default='django.core.mail.backends.console.EmailBackend')

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'admin@kartoza.com')
