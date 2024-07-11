#!/usr/bin/python3
""" Setup database tables """

import os
from models import storage

if __name__ == "__main__":
    storage.reload()
