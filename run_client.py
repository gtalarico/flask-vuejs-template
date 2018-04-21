import os
import subprocess

here = os.path.dirname(__file__)
client_app_dir = os.path.join(here, 'app', 'client', 'app')

subprocess.call('npm run dev', shell=True, cwd=client_app_dir)
