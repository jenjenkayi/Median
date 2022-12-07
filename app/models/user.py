from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from .follower import follows
from sqlalchemy.orm import validates


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    profile_picture = db.Column(db.String)
    bio = db.Column(db.String(5000))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    followers = db.relationship(
        "User",
        secondary=follows,
        primaryjoin=(follows.c.followed_id == id),
        secondaryjoin=(follows.c.follower_id == id),
        backref=db.backref("following", lazy="dynamic"),
        lazy="dynamic"

    )
    comments = db.relationship("Comment", back_populates="user")
    stories = db.relationship("Story", back_populates="user")
    likes = db.relationship("Like", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @validates("following")
    def validates_following(self, key, value):
        if value == self.id:
            raise ValueError("You cannot follow yourself!")

    def is_following(self, userId):

        return self.following.filter(
            follows.c.followed_id == userId).count() > 0

    def follow(self, user):
        if not self.is_following(user.id):

            self.following.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user.id):

            self.following.remove(user)
            return self

    def to_dict(self):

        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'bio': self.bio,
            'followerCount': len(self.followers.all()),
            'followingCount': len(self.following.all()),
            'profile_picture': self.profile_picture,
            'bio': self.bio
        }
