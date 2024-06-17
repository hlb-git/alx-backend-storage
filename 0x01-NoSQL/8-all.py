#!/usr/bin/env python3
"""pymongo module to list all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """list all documents in a collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
