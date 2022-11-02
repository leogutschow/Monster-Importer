import os

AWS_SECRET_ACCESS_KEY = os.environ.get("DJANGO_DEV_SECRET")
AWS_ACCESS_KEY = os.environ.get("DJANGO_DEV")
DJANGO_PRODUCTION = os.environ.get("DJANGO_PRODUCTION")
DJANGO_PRODUCTION_SECRET = os.environ.get("DJANGO_PRODUCTION_SECRET")
AWS_STORAGE_BUCKET_NAME = "monster-importer"
AWS_S3_ENDPOINT_URL = "https://sfo3.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = "https://monster-importer.sfo3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = 'MonsterImporter.cdn.backends.MediaRootS3Boto3Storage'
STATICFILES_STORAGE = 'MonsterImporter.cdn.backends.StaticRootS3Boto3Storage'
