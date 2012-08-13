
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

ROOT_URLCONF = 'testproject.urls'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'privateviews.middleware.LoginRequiredMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'privateviews',
]
