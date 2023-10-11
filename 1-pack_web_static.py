#!/usr/bin/python3
"""Compress before sending
"""
from fabric.api import *
from datetime import datetime


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
