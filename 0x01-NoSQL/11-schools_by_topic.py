#!/usr/bin/env python3
""" Returns the schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topc."""
    return list(mongo_collection.find({"topic": topic}))
