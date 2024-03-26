#!/usr/bin/env python3
""" Inserts a new document in the collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document int he school collecttion based on kwargs."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
