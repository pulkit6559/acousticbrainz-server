import os


DEBUG = False  # set to False in production mode
# Additional files to watch to restart the development server
RELOAD_ON_FILES = ["webserver/static/build/rev-manifest.json"]

SECRET_KEY = "CHANGE_ME"


# DATABASES

# Primary database
SQLALCHEMY_DATABASE_URI = "postgresql://acousticbrainz@db/acousticbrainz"

# URI to connect to an empty database as the superuser
POSTGRES_ADMIN_URI = "postgresql://postgres@db/template1"
# URI to connect to the acousticbrainz database as the superuser (to install extensions)
POSTGRES_ADMIN_AB_URI = "postgresql://postgres@db/acousticbrainz"

# MUSICBRAINZ

MUSICBRAINZ_USERAGENT = "acousticbrainz-server"
MUSICBRAINZ_HOSTNAME = None

# OAuth
MUSICBRAINZ_CLIENT_ID = "wE0tI-zvooqR5ZgwdVJW6Q"
MUSICBRAINZ_CLIENT_SECRET = "OxT7k7WbvlZpqIN3_JpZOQ"

# CACHE

REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_NAMESPACE = "AB"
REDIS_NS_VERSIONS_LOCATION = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cache_namespaces')

# LOGGING
# Uncomment any of the following logging stubs if you want to enable logging
# during development. In general you shouldn't need to do this.

# LOG_FILE = {
#    'filename': './acousticbrainz.log',
#    'max_bytes': 512 * 1024, # optional
#    'backup_count': 10, # optional
# }

# LOG_EMAIL = {
#    'mail_server': 'localhost',
#    'mail_port': 25,
#    'mail_from_host': 'acousticbrainz.org',
#    'log_email_recipients': [
#        '',
#    ],
#    'log_email_topic': 'AcousticBrainz Error',
#    'level': 'ERROR',
# }

# LOG_SENTRY = {
#    'dsn':'',
#    'environment': 'development',
#    'level': 'ERROR',
# }

# MISCELLANEOUS

DATASET_DIR = "/data/datasets"
FILE_STORAGE_DIR = "/data/files"

#Feature Flags
FEATURE_EVAL_LOCATION = False
