#!/usr/bin/env python3
"""pymongo module to update many rows"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """update many rows"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
