import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'zomk1gko4kyiy(v^el6)id#h-#8rocoyvpnt$c6f#=-$c=qdx!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb'
    }
}

STATICBUILDER_BUILD_ROOT = os.path.join(BASE_DIR, 'build_root')
