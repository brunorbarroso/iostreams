import os

STRING_BLOCK_SEPARATOR  = os.getenv("STRING_BLOCK_SEPARATOR", "firstName|lastName|birthday|")
EXT_DEFAULT_OUTPUT      = os.getenv("EXT_DEFAULT_OUTPUT", ".txt")

database_user           = os.getenv("DATABASE_USER", "root")
database_password       = os.getenv("DATABASE_PASSWORD", "")
database_host           = os.getenv("DATABASE_HOST", "127.0.0.1")
database_name           = os.getenv("DATABASE_NAME", "parse")