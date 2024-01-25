#!/usr/bin/env python3
# redis chache
import redis
import uuid


class cache:
    """class for chache"""

    def __init__(self, r: redis.Redis) -> None:
        """init"""
        self.__redis__ = r

    def store(self, data: str | bytes | int | float) -> uuid.UUID:
        """store in redis"""
        key = str(uuid.uuid4())
        self.__redis__.set(key, data)
        return key
