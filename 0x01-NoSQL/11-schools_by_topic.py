#!/usr/bin/env python3
"""pymongo module to find by topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """find by topic"""
    return mongo_collection.find({"topics": topic})
