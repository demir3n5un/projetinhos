import subprocess
import sys

subprocess.Popen(['start', 'cmd', '/k', sys.executable, 'main.py'], shell=True)