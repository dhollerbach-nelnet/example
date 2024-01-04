import json
import os
import subprocess

SECRETS = json.loads(os.environ['ALL_SECRETS'])

for k, v in SECRETS.items():
  cmd = 'echo TF_VAR_{}={} >> $GITHUB_ENV'.format(k, v)
  proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
