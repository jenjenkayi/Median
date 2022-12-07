from .db import db, environment, SCHEMA, add_prefix_for_prod

from datetime import datetime


class Comment(db.Model):
    __tablename__ = "comments"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)
    story_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("stories.id")), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user = db.relationship("User", back_populates="comments")
    story = db.relationship("Story", back_populates="comments")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'story_id': self.story_id,
            'content': self.content,
            "created_at": self.created_at
        }

    def to_dict_with_user(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'story_id': self.story_id,
            'content': self.content,
            "created_at": self.created_at,
            "user": self.user.to_dict()
        }
