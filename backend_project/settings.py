INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "drf_spectacular",

    "extraction",
]
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS":
        "drf_spectacular.openapi.AutoSchema"
}
SPECTACULAR_SETTINGS = {
    "TITLE": "Data Extraction API",
    "DESCRIPTION": "Extraction Service",
    "VERSION": "1.0.0",
}
