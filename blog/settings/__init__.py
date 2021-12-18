from .production import *

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'