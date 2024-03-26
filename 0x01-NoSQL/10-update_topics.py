#!/usr/bin/env python3
""" Updates all school topics """


def update_topics(mongo_collection, name, topics):
    """Update topics of all school collection with a given name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
