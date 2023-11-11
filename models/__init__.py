#!/usr/bin/python3
''' Initialize the models package '''

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
