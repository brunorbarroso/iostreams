import autoload
import os

STRING_BLOCK_SEPARATOR  = os.getenv("STRING_BLOCK_SEPARATOR")
EXT_DEFAULT_OUTPUT      = os.getenv("EXT_DEFAULT_OUTPUT")

database_user           = os.getenv("DATABASE_USER")
database_password       = os.getenv("DATABASE_PASSWORD")
database_host           = os.getenv("DATABASE_HOST")
database_name           = os.getenv("DATABASE_NAME")