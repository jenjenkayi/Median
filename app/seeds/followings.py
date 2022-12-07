from app.models import db, environment, SCHEMA

# Adds a demo user, you can add other users here if you want


def seed_followings(users):
    user1 = users[0]
    user2 = users[1]
    user3 = users[2]
    user4 = users[3]
    user5 = users[4]
    user6 = users[5]
    user7 = users[6]
    user8 = users[7]
    user9 = users[8]
    user10 = users[9]
    user11 = users[10]
    user12 = users[11]
    user13 = users[12]
    user14 = users[13]
    user15 = users[14]
    user16 = users[15]
    user17 = users[16]
    user18 = users[17]
    user19 = users[18]
    user20 = users[19]

    user1.following.append(user2)
    user2.following.append(user1)
    user2.following.append(user3)
    user2.following.append(user4)
    user2.following.append(user5)
    user2.following.append(user6)
    user2.following.append(user7)
    user2.following.append(user8)
    user2.following.append(user9)
    user2.following.append(user10)
    user2.following.append(user11)
    user2.following.append(user12)
    user2.following.append(user13)
    user2.following.append(user14)
    user2.following.append(user15)
    user2.following.append(user16)
    user2.following.append(user17)
    user2.following.append(user18)
    user2.following.append(user19)
    user2.following.append(user20)
    user3.following.append(user1)
    user3.following.append(user6)
    user3.following.append(user9)
    user3.following.append(user12)
    user3.following.append(user18)
    user3.following.append(user19)
    user4.following.append(user1)
    user4.following.append(user2)
    user4.following.append(user6)
    user4.following.append(user7)
    user4.following.append(user9)
    user4.following.append(user10)
    user4.following.append(user13)
    user4.following.append(user14)
    user4.following.append(user15)
    user4.following.append(user17)
    user4.following.append(user19)
    user4.following.append(user20)
    user5.following.append(user1)
    user5.following.append(user3)
    user5.following.append(user7)
    user5.following.append(user8)
    user5.following.append(user9)
    user5.following.append(user10)
    user5.following.append(user15)
    user5.following.append(user18)
    user5.following.append(user19)
    user5.following.append(user20)
    user6.following.append(user1)
    user6.following.append(user4)
    user6.following.append(user8)
    user6.following.append(user12)
    user6.following.append(user16)
    user6.following.append(user18)
    user6.following.append(user20)
    user7.following.append(user1)
    user7.following.append(user5)
    user7.following.append(user9)
    user7.following.append(user11)
    user7.following.append(user12)
    user7.following.append(user19)
    user8.following.append(user1)
    user8.following.append(user5)
    user8.following.append(user6)
    user8.following.append(user9)
    user8.following.append(user15)
    user8.following.append(user18)
    user9.following.append(user1)
    user9.following.append(user3)
    user9.following.append(user5)
    user9.following.append(user6)
    user9.following.append(user8)
    user9.following.append(user17)
    user10.following.append(user1)
    user10.following.append(user6)
    user10.following.append(user9)
    user10.following.append(user13)
    user10.following.append(user18)
    user10.following.append(user20)
    user11.following.append(user1)
    user11.following.append(user2)
    user12.following.append(user1)
    user12.following.append(user2)
    user13.following.append(user1)
    user13.following.append(user2)
    user14.following.append(user1)
    user14.following.append(user2)
    user15.following.append(user1)
    user15.following.append(user2)
    user16.following.append(user1)
    user16.following.append(user2)
    user17.following.append(user1)
    user17.following.append(user2)
    user18.following.append(user1)
    user18.following.append(user2)
    user19.following.append(user1)
    user19.following.append(user2)
    user20.following.append(user1)
    user20.following.append(user2)

    db.session.commit()


def undo_followings():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.follows RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM followers")

    db.session.commit()
