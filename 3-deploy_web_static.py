#!/usr/bin/python3
"""a script to deploy web static
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.164.145.199', '34.229.67.107']

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time)

    if not isdir("versions"):
        local("mkdir versions")

    local("tar -cvzf {} web_static".format(file_path))

    return file_path

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive_filename = archive_path.split("/")[-1]
        without_tgz = archive_filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(without_tgz))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, without_tgz))
        run("rm /tmp/{}".format(archive_filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(without_tgz, without_tgz))
        run("rm -rf /data/web_static/releases/{}/web_static".format(without_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(without_tgz))
        print("New version deployed!")
        return True
    except:
        return False

def deploy():
    """
    Creates and distributes an archive to web servers
    """

    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
