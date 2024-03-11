from blog.settings.base import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "testdb.sqlite3",
        },
    }
}
