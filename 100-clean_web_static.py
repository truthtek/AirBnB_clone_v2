#!/usr/bin/python3
"""a script to pack static content into a tarball
"""
from fabric.api import env, local, run
from os.path import exists, isdir

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """

    number = int(number)

    if number < 2:
        number = 1
    else:
        number += 1

    local("ls -dt versions/* | tail -n +{} | xargs rm -rf".format(number))
    run("ls -dt /data/web_static/releases/* | tail -n +{} | xargs rm -rf".format(number))
