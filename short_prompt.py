#!/usr/bin/env/python
from __future__ import print_function
import os
from socket import gethostname

MAX_LENGTH=33
FRONT_LENGTH = 10
assert MAX_LENGTH > FRONT_LENGTH

host = gethostname()
user = os.environ["USER"]
known_hosts = {}

host = known_hosts.get(host, host)

pwd = os.getcwd()

homedir = os.path.expanduser("~")

# Replace everything before homedir with ~

pwd = pwd.replace(homedir, "~", 1)

#Now shorten

dirs = pwd.split("/")
if len(pwd) > MAX_LENGTH:
    pwd = pwd[:FRONT_LENGTH] + "..." + pwd[FRONT_LENGTH - MAX_LENGTH:]
elif len(dirs) > 5:
    pwd = "/".join(dirs[:2] + ["..."] + dirs[-2:]

prompt = "[%s@%s:%s]" % (user, host, pwd)

# Add conda env if active

conda_env = os.environ.get("CONDA_DEFAULT_ENV", None)
if conda_env is not None:
    prompt = "(" + conda_env + ") " + prompt

print(prompt)
