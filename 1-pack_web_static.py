#!/usr/bin/env python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # create a versions directory if not exists
    local("mkdir -p versions")

    # create a tgz archive of the web_static directory
    timestr = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestr)
    result = local("tar -cvzf {} web_static".format(archive_path))

    # return the archive path if the archive has been correctly generated. Otherwise, it should return None
    if result.failed:
        return None
    else:
        return archive_path
