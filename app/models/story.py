from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Story(db.Model):
    __tablename__ = "stories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    user = db.relationship("User", back_populates="stories")
    comments = db.relationship(
        "Comment", back_populates="story", cascade="all, delete")
    likes = db.relationship(
        "Like", back_populates="story", cascade="all,delete")

    def to_dict(self):

        return {"id": self.id, "user_id": self. user_id,
                "title": self.title, "image": self.image, "content": self.content, "createdAt": self.created_at,
                'author': self.user.to_dict(), 'likeCount': sum(like.get_count() for like in self.likes), 'commentCount': len(self.comments)}

    def to_dict_no_relations(self):
        return {
            "id": self.id, "user_id": self. user_id,
            "title": self.title, "image": self.image, "content": self.content, "createdAt": self.created_at, "updatedAt": self.updated_at
        }
