#!/usr/bin/python3
""" reloads the storage """


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# create a unique FileStorage instance
storage = FileStorage()

# call the reload method on the instance
storage.reload()
