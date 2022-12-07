from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


follows = db.Table(
    "follows",
    db.Column("follower_id", db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id"))),
    db.Column("followed_id", db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")))
)
if environment == "production":
    follows.schema = SCHEMA
