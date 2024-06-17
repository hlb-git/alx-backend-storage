#!/usr/bin/env python3
"""pymongo module to list all documents in a collection"""


def top_students(mongo_collection):
    """ students by score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
