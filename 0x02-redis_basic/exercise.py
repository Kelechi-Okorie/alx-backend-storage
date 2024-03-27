#!/usr/bin/env python3
""" Creates a store that takes a data argument and returns string"""

import redis
import uuid
from typing import Union


class Cache:
    """The cache class takes a data argument and returns a string."""

    def __init__(self):
        """The init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """The count_calls function"""

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """The wrapper function"""

            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The store function"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """The get function"""

        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """The str_str functin"""

        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """The get_int function"""

        return self.get(key, lambda x: int(x))

    @staticmethod
    def call_history(method: Callable) -> Callable:
        """call_history method"""

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """The wrapper function"""

            input_key = method.__qaulname__ + ":inputs"
            output_ey = method.__qualname__ + ":output"

            self._redis.rpush(input_key, str(args))

            output = method(self, *args, **kwargs)

            self._redis.rpush(output_output, output)

            return output
        return wrapper

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
