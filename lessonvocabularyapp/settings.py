# Only included the parts you would need to modify

# Add the 'lessons' app for our lesson model - adding 'LessonsConfig' from lessons/apps
INSTALLED_APPS = [
    'lessons.apps.LessonsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# An example of modifying the database setup - we used MySQL for this projects\
# We set options to allow INNODB as the default storage engine - INNODB allows foreign keys
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lessonvocabularyapp',
        'USERNAME':'username',
        'PASSWORD':'password',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'init_command':'SET default_storage_engine=INNODB'
        }
    }
}
