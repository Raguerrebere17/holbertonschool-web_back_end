#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""

def list_all(mongo_collection):
    """
        List all in db
    """
    return [i for i in mongo_collection.find()]
