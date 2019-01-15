from dotenv import load_dotenv
from pathlib import Path
import os

env_path = f"{Path('.')}{str(os.sep)}.env"
load_dotenv( dotenv_path=env_path )