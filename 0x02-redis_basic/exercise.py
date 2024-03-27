#!/usr/bin/env python3
""" Creates a store that takes a data argument and returns string"""

import redis
import uuid
from typing import Union


class Cache:
    """The cache class takes a data argument and returns a string."""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
