import copy
from geonode.settings import *
from .utils import absolute_path  # noqa

INSTALLED_APPS += (
    'custom',

    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',
    'wagtailmenus',
    'modelcluster',
)

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'dj_pagination.middleware.PaginationMiddleware',
    # The setting below makes it possible to serve different languages per
    # user depending on things like headers in HTTP requests.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'geonode.base.middleware.MaintenanceMiddleware',
    'geonode.base.middleware.ReadOnlyMiddleware',  # a Middleware enabling Read Only mode of Geonode

    # Wagtail moddleware
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
TEMPLATES = [
    {
        'NAME': 'GeoNode Project Templates',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'geonode.context_processors.resource_urls',
                'geonode.geoserver.context_processors.geoserver_urls',
                'geonode.themes.context_processors.custom_theme',

                # custom context processor
                'custom.context_processors.configs',

                # WAGTAIL
                'wagtail.contrib.settings.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
            'debug': DEBUG,
        },
    },
]

_DEFAULT_LANGUAGES = (
    # ('id', 'Bahasa Indonesia'),
    ('en', 'English'),
    ('fr', 'Français'),
)
LANGUAGES = os.getenv('LANGUAGES', _DEFAULT_LANGUAGES)

# Additional locations of static files
STATICFILES_DIRS = [absolute_path('custom', 'static'), ] + STATICFILES_DIRS

# Additional locations of templates
TEMPLATES[0]['DIRS'] = [absolute_path('custom', 'templates')] + TEMPLATES[0]['DIRS']

# Wagtail Settings
WAGTAIL_SITE_NAME = 'My Example Site'
WAGTAILMENUS_SITE_SPECIFIC_TEMPLATE_DIRS = True
# -- END Settings for Wagtail

ROOT_URLCONF = 'core.urls'
LOCALE_PATHS += (
    os.path.join(PROJECT_ROOT, 'custom', 'locale'),
)

GEP_TITLE = os.getenv('GEP_TITLE', 'Global Electrification Programme')
GEP_SHORT_TITLE = os.getenv('GEP_SHORT_TITLE', 'BEP')
SDI_TITLE = os.getenv('SDI_TITLE', 'Global Electrification Platform SDI')
