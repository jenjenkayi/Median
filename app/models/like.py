from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Like(db.Model):
    __tablename__ = "likes"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # COMPOSITE PRIMARY KEY, USE GET WITH A TUPLE (user_id, story_id)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("stories.id")), nullable=False, primary_key=True)
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    story = db.relationship("Story", back_populates="likes")
    user = db.relationship("User", back_populates="likes")

    def get_count(self):
        return self.count
