import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Добавить эту строку
        'APP_DIRS': True,
        # ... остальные настройки
    },
]
