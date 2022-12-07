from app.models import db, Comment, environment, SCHEMA


def seed_comments():
    instance1 = Comment(
        user_id=2,
        story_id=1,
        content="This was an awesome blog post."
    )
    instance2 = Comment(
        user_id=2,
        story_id=2,
        content="Thanks for sharing."
    )
    instance3 = Comment(
        user_id=2,
        story_id=3,
        content="Great article!"
    )
    instance4 = Comment(
        user_id=2,
        story_id=4,
        content="I totally agree with you"
    )
    instance5 = Comment(
        user_id=2,
        story_id=5,
        content="Very cool. Thanks for sharing!"
    )
    instance6 = Comment(
        user_id=2,
        story_id=6,
        content="My 66 year old niece rates this notification very minimal!!"
    )
    instance7 = Comment(
        user_id=2,
        story_id=7,
        content="This idea blew my mind."
    )
    instance8 = Comment(
        user_id=2,
        story_id=8,
        content="I think I'm crying. It's that fun."
    )
    instance9 = Comment(
        user_id=2,
        story_id=9,
        content="Super engaging."
    )
    instance10 = Comment(
        user_id=2,
        story_id=10,
        content="This shot has navigated right into my heart."
    )
    instance11 = Comment(
        user_id=2,
        story_id=11,
        content="I want to learn this kind of pattern! Teach me."
    )
    instance12 = Comment(
        user_id=2,
        story_id=12,
        content="Such sexy."
    )
    instance13 = Comment(
        user_id=2,
        story_id=13,
        content="Splendid :) I want to make love to the use of lines and shade!"
    )
    instance14 = Comment(
        user_id=2,
        story_id=14,
        content="Elegant work you have here."
    )
    instance15 = Comment(
        user_id=3,
        story_id=1,
        content="This is sublime work."
    )
    instance16 = Comment(
        user_id=3,
        story_id=2,
        content="Just nice!"
    )
    instance17 = Comment(
        user_id=3,
        story_id=3,
        content="Such colour, many playfulness, so fabulous"
    )
    instance18 = Comment(
        user_id=3,
        story_id=4,
        content="Love your shot."
    )
    instance19 = Comment(
        user_id=3,
        story_id=5,
        content="Very cool. Thanks for sharing!"
    )
    instance20 = Comment(
        user_id=3,
        story_id=6,
        content="Cool shot m8"
    )
    instance21 = Comment(
        user_id=3,
        story_id=7,
        content="Mission accomplished. It's gorgeous dude"
    )
    instance22 = Comment(
        user_id=3,
        story_id=8,
        content="Playfulness, pattern, experience, shot – incredible, friend."
    )
    instance23 = Comment(
        user_id=3,
        story_id=9,
        content="Fab. So appealing."
    )
    instance24 = Comment(
        user_id=4,
        story_id=1,
        content="Let me take a nap... great camera angle, anyway."
    )
    instance25 = Comment(
        user_id=4,
        story_id=2,
        content="How do you make this? Photoshop?"
    )
    instance26 = Comment(
        user_id=4,
        story_id=3,
        content="Trying it now."
    )
    instance27 = Comment(
        user_id=4,
        story_id=4,
        content="Truly thought out! I think clients would love this."
    )
    instance28 = Comment(
        user_id=4,
        story_id=5,
        content="Overly appealing shot!"
    )
    instance29 = Comment(
        user_id=4,
        story_id=6,
        content="Space grey. I'm in!"
    )
    instance30 = Comment(
        user_id=4,
        story_id=7,
        content="It's minimal not just neat!"
    )
    instance31 = Comment(
        user_id=4,
        story_id=8,
        content="This is clean work!!"
    )
    instance32 = Comment(
        user_id=4,
        story_id=9,
        content="It's sexy not just alluring!"
    )
    instance33 = Comment(
        user_id=4,
        story_id=10,
        content="I want to learn this kind of lines! Teach me."
    )
    instance34 = Comment(
        user_id=4,
        story_id=11,
        content="Can't wait to try it out."
    )
    instance35 = Comment(
        user_id=4,
        story_id=12,
        content="Whoa."
    )
    instance36 = Comment(
        user_id=4,
        story_id=13,
        content="Such shot, many iconography, so good"
    )
    instance37 = Comment(
        user_id=5,
        story_id=1,
        content="Very cool design :-)"
    )
    instance38 = Comment(
        user_id=5,
        story_id=2,
        content="My 37 year old niece rates this work very elegant m8"
    )
    instance39 = Comment(
        user_id=5,
        story_id=3,
        content="Just graceful mate"
    )
    instance39 = Comment(
        user_id=5,
        story_id=4,
        content="Mission accomplished. It's simple m8"
    )
    instance40 = Comment(
        user_id=5,
        story_id=5,
        content="Nice use of slate grey in this job =)"
    )
    instance41 = Comment(
        user_id=6,
        story_id=1,
        content="Magical. So classic."
    )
    instance42 = Comment(
        user_id=6,
        story_id=2,
        content="xxx"
    )
    instance43 = Comment(
        user_id=6,
        story_id=3,
        content="Magical camera angle m8"
    )
    instance44 = Comment(
        user_id=6,
        story_id=4,
        content="Beastly work you have here."
    )
    instance45 = Comment(
        user_id=7,
        story_id=1,
        content="I like your notification mate"
    )
    instance46 = Comment(
        user_id=7,
        story_id=2,
        content="So admirable and sexy!"
    )
    instance47 = Comment(
        user_id=7,
        story_id=3,
        content="This experience blew my mind."
    )
    instance48 = Comment(
        user_id=7,
        story_id=4,
        content="Green. Yup."
    )
    instance49 = Comment(
        user_id=7,
        story_id=5,
        content="Iconography, button, notification, shot – sublime!!"
    )
    instance50 = Comment(
        user_id=8,
        story_id=1,
        content="Found myself staring at it for minutes."
    )

    db.session.add(instance1)
    db.session.add(instance2)
    db.session.add(instance3)
    db.session.add(instance4)
    db.session.add(instance5)
    db.session.add(instance6)
    db.session.add(instance7)
    db.session.add(instance8)
    db.session.add(instance9)
    db.session.add(instance10)
    db.session.add(instance11)
    db.session.add(instance12)
    db.session.add(instance13)
    db.session.add(instance14)
    db.session.add(instance15)
    db.session.add(instance16)
    db.session.add(instance17)
    db.session.add(instance18)
    db.session.add(instance19)
    db.session.add(instance20)
    db.session.add(instance21)
    db.session.add(instance22)
    db.session.add(instance23)
    db.session.add(instance24)
    db.session.add(instance25)
    db.session.add(instance26)
    db.session.add(instance27)
    db.session.add(instance28)
    db.session.add(instance29)
    db.session.add(instance30)
    db.session.add(instance31)
    db.session.add(instance32)
    db.session.add(instance33)
    db.session.add(instance34)
    db.session.add(instance35)
    db.session.add(instance36)
    db.session.add(instance37)
    db.session.add(instance38)
    db.session.add(instance39)
    db.session.add(instance39)
    db.session.add(instance40)
    db.session.add(instance41)
    db.session.add(instance42)
    db.session.add(instance43)
    db.session.add(instance44)
    db.session.add(instance45)
    db.session.add(instance46)
    db.session.add(instance47)
    db.session.add(instance48)
    db.session.add(instance49)
    db.session.add(instance50)

    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM comments")

    db.session.commit()
