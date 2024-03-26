#!/usr/bin/env python3
""" lists all documents in a school collection """


def list_all(mongo_collection):
    """Lists all documents in a given collection."""
    return list(mongo_collection.find())
