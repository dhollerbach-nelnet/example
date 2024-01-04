import json
import subprocess
import sys

SECRETS = json.loads(sys.argv[1])

for k, v in SECRETS.items():
  cmd = 'echo TF_VAR_{}={} >> $GITHUB_ENV'.format(k, v)
  proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
