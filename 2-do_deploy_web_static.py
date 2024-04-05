#!/usr/bin/python3
"""a script to pack static content into a tarball
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    # check if the file at the path archive_path doesn’t exist
    if not exists(archive_path):
        return False

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
        archive_filename = archive_path.split("/")[-1]
        without_tgz = archive_filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(without_tgz))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, without_tgz))
        # delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(without_tgz, without_tgz))
        run("rm -rf /data/web_static/releases/{}/web_static".format(without_tgz))
        # delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(without_tgz))
        print("New version deployed!")
        return True
    except:
        return False
