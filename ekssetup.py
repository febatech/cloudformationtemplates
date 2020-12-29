from __future__ import print_function

import subprocess

import shlex

# This is to run the ekssetup.sh shell script

print('Loading function')
subprocess.call(shlex.split('/Users/venkataponnapalli/PycharmProjects/pythonProject/venv/ekssetup.sh'))


