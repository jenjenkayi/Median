from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user, login_user
from app.models import User, Story
from app.errors import NotFoundError
from .helpers import get_user_model
from ..models.db import db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


# Get detail of User by id
@user_routes.route('/<int:id>')
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    if user:
        stories = Story.query.filter(Story.user_id == id)
        result = user.to_dict()
        result["Stories"] = [ele.to_dict_no_relations() for ele in stories]
        return result
    else:
        raise NotFoundError("User not found")

# Get details of current User


@user_routes.route('/profile')
@login_required
def get_current_user():
    curr_user = get_user_model(current_user, User)

    if curr_user:
        stories = Story.query.filter(Story.user_id == curr_user.id)
        result = curr_user.to_dict()
        result["followingCount"] = len(
            [ele.to_dict() for ele in curr_user.following])
        result["Stories"] = [ele.to_dict_no_relations() for ele in stories]
        return result


# Get all Stories by a UserId
@user_routes.route("/<int:userId>/stories")
def all_user_stories(userId):
    user = User.query.get(userId)
    if not user:
        raise NotFoundError("User not found")
    stories = Story.query.filter(Story.user_id == userId).all()
    return jsonify({"Stories": [story.to_dict() for story in stories]})


# Get all Followers of a User
@user_routes.route('/<int:user_id>/followers')
def get_followers_of_user(user_id):
    page = request.args.get('page', type=int)
    size = request.args.get('size', type=int)
    user = User.query.get(user_id)

    if not user:
        raise NotFoundError("User not found")
    followers = user.followers.paginate(page=page, per_page=size).items
    return jsonify({"Followers": [follower.to_dict() for follower in followers]})


@user_routes.route('<int:user_id>/following')
def get_followings_of_user(user_id):
    page = request.args.get('page', type=int)
    size = request.args.get('size', type=int)
    user = User.query.get(user_id)
    if not user:
        raise NotFoundError("User not found")
    followings = user.following.paginate(page=page, per_page=size).items
    return jsonify({"Followings": [following.to_dict() for following in followings]})

# Follow a User by id


@user_routes.route("/<int:userId>/followers", methods=["POST"])
@login_required
def follow_user(userId):
    following = User.query.get(userId)
    current = get_user_model(current_user, User)

    if not following:
        raise NotFoundError("User not found.")

    res = current.follow(following)
    current.following = res.following

    db.session.commit()
    return {"message": "Successfully Followed", "statusCode": 201}


# Unfollow a User by id
@user_routes.route('/<int:user_id>/followers', methods=['DELETE'])
@login_required
def remove_follow(user_id):
    user = User.query.get(user_id)
    if not user:
        raise NotFoundError(f'User {user_id} does not exist.')
    current = get_user_model(current_user, User)

    if current not in user.followers:
        return {"message": f"Current user does not follow user {user_id}"}

    # del user.followers[i]

    resp = current.unfollow(user)
    current.following = resp.following

    db.session.commit()
    return {"message": "Successfully Unfollowed", "statusCode": 200}


# Check if current user follows target user
@user_routes.route('/<int:user_id>/isFollowing')
@login_required
def is_following(user_id):
    user = get_user_model(current_user, User)
    return {'isFollowing': user.is_following(user_id)}
