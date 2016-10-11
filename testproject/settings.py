
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'SUPERSEKRIT'

ROOT_URLCONF = 'testproject.urls'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'privateviews.middleware.LoginRequiredMiddleware',
]

PUBLIC_VIEWS = [
    'testproject.views.test_public_views',
]

PUBLIC_PATHS = [
    '^/test-public-paths/$'
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'privateviews',
]
