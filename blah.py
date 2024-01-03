import subprocess

ALLSECRETS = {
  "SECRET1" : "test",
  "SECRET2" : "test"
}

for k, v in ALLSECRETS.items():
  cmd = 'echo {}={} >> $GITHUB_ENV'.format(k, v)
  print(cmd)