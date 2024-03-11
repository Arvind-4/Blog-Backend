from blog.env import config

DJANGO_LIVE = config("DJANGO_LIVE", cast=bool)

if DJANGO_LIVE:
    print("Loading production settings...")
    from blog.settings.production import *

else:
    print("Loading developement settings...")
    from blog.settings.dev import *
