#!/usr/bin/env python

import argparse
import sys
from getpass import getpass
import vk_voice


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


parser = argparse.ArgumentParser()
parser.add_argument("--path")
parser.add_argument("--user_id")
parser.add_argument("--chat", action='store_true')
parser.set_defaults(chat=False)
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

log("Login: ", end="")
sys.stderr.flush()
login = sys.stdin.readline()
password = getpass(stream=sys.stderr)

try:
    vk_voice.send(login, password, args.path, args.user_id, args.chat)

except Exception as e:
    log(e)
