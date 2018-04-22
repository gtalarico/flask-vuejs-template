import os
import subprocess

from app.config import Config

subprocess.call('npm run serve', shell=True, cwd=Config.CLIENT_DIR)
