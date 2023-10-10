#!/usr/bin/python3
""" creates and distributes an archive to your web servers, using the
function deploy """
from datetime import datetime
from fabric.api import env, local, put, run
import os
import shlex


env.hosts = ['3.80.18.129', '100.25.130.218']


def deploy():
    """ creates an archive to your web servers"""
    try:
        archive_path = do_pack()
    except:
        return False

    return do_deploy(archive_path)


def do_pack():
    """Function that compresses a folder

    Returns:
        str: archive name
    """
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the function 
    do_deploy

    Args:
        archive_path: path of the archive

    Returns:
        boolean: True if archive is distributed properly, otherwise false
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = archive_path.replace('/', ' ')
        archive_filename = shlex.split(archive_filename)
        archive_filename = archive_filename[-1]

        no_ext_name = archive_filename.replace('.', ' ')
        no_ext_name = shlex.split(no_ext_name)
        no_ext_name = no_ext_name[0]

        releases_name = "/data/web_static/releases/{}".format(no_ext_name)
        tmp_path = "/tmp/{}".format(archive_filename)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_name))
        run("tar -xzf {} -C {}".format(tmp_path, releases_name))
        run("rm {}".format(tmp_path))
        run("mv {}/web_static/* {}".format(releases_name, releases_name))
        run("rm -rf {}/web_static".format(releases_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_name))
        print("New version deployed!")
        return True

    except Exception:
        return False
