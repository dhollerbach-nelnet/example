import json
import subprocess
import sys

SECRETS_DICT = json.loads(sys.argv[1])


def main(secrets: dict):
  """Sets secrets as GitHub environment variables. Makes each secret usable by Terraform by prefixing with TF_VAR_.

  Args:
      secrets (dict): Dictionary of secrets.
  """
  for secret_name, secret_value in secrets.items():
    cmd = 'echo TF_VAR_{}={} >> $GITHUB_ENV'.format(secret_name, secret_value)
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


if __name__ == "__main__":
  main(SECRETS_DICT)
