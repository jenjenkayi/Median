from app.models import db, User, environment, SCHEMA

PROFILE_PIC = 'https://media.istockphoto.com/id/1209654046/vector/user-avatar-profile-icon-black-vector-illustration.jpg?s=612x612&w=0&k=20&c=EOYXACjtZmZQ5IsZ0UUp1iNmZ9q2xl1BD1VvN6tZ2UI='
# Adds a demo user, you can add other users here if you want


def seed_users():
    instance1 = User(
        username='username1',
        email='email1@gmail.com',
        password='password1',
        first_name="John",
        last_name="Smith",
        profile_picture=PROFILE_PIC,
        bio="Diversity&Inclusion educator. Author, Pin Ups (9/20). Columnist, The Writer mag."
    )
    instance2 = User(
        username='username2',
        email='email2@gmail.com',
        password='password2',
        first_name="Li",
        last_name="Sam",
        profile_picture=PROFILE_PIC,
        bio="Leica, GR3, Sony, Minolta & Film user, Street Photographer based in Hong Kon"
    )
    instance3 = User(
        username='username3',
        email='email3@gmail.com',
        password='password3',
        first_name="Thomas",
        last_name="Christopher",
        profile_picture=PROFILE_PIC,
        bio="Science, psychology, and history. Sometimes with a personal angle."
    )
    instance4 = User(
        username='username4',
        email='email4@gmail.com',
        password='password4',
        first_name="Than",
        last_name="Siegel",
        profile_picture=PROFILE_PIC,
        bio="The Universe is: Expanding, cooling, and dark. It starts with a bang! #Cosmology Science writer, astrophysicist, science communicator & NASA columnist."
    )
    instance5 = User(
        username='username5',
        email='email5@gmail.com',
        password='password5',
        first_name="Cory",
        last_name="Doctrowrow",
        profile_picture=PROFILE_PIC,
        bio="Writer, blogger, activist."
    )
    instance6 = User(
        username='username6',
        email='email6@gmail.com',
        password='password6',
        first_name="Clive",
        last_name="Thompson",
        profile_picture=PROFILE_PIC,
        bio="I write 3X a week on tech, science, culture — and how those collide. Writer at NYT mag/Wired; author, 'Coders'. "
    )
    instance7 = User(
        username='username7',
        email='email7@gmail.com',
        password='password7',
        first_name="Chuck",
        last_name="Frey",
        profile_picture=PROFILE_PIC,
        bio="Thought leader in mind mapping, visual thinking and creativity for 15+ years. Relentless explorer, learner and dot-collector. I help you elevate your thinking."
    )
    instance8 = User(
        username='username8',
        email='email8@gmail.com',
        password='password8',
        first_name="Daniel",
        last_name="Burrus",
        profile_picture=PROFILE_PIC,
        bio="#1 Bestselling Author, Global Futurist, Innovation Expert and Keynote Speaker. One of the Worlds Leading Futurists on Global Trends and Innovation."
    )
    instance9 = User(
        username='username9',
        email='email9@gmail.com',
        password='password9',
        first_name="Cait",
        last_name="Mack",
        profile_picture=PROFILE_PIC,
        bio="Lean Living: I simplify everything so you can focus on crushing life"
    )
    instance10 = User(
        username='username10',
        email='email10@gmail.com',
        password='password10',
        first_name="Ben",
        last_name="LeFort",
        profile_picture=PROFILE_PIC,
        bio="Making of a Millionaire editor | Personal finance writer | Author of 'The Financial Freedom Equation'"
    )
    instance11 = User(
        username='username11',
        email='email11@gmail.com',
        password='password11',
        first_name="Sean",
        last_name="Kernan",
        profile_picture=PROFILE_PIC,
        bio="Quality over quantity. Always on the hunt for a good story. That guy from Quora. Writing out of Tampa, Florida."
    )
    instance12 = User(
        username='username12',
        email='email12@gmail.com',
        password='password12',
        first_name="Jamie",
        last_name="Jackson",
        profile_picture=PROFILE_PIC,
        bio="Between two skies."
    )
    instance13 = User(
        username='username13',
        email='email13@gmail.com',
        password='password13',
        first_name="Philip",
        last_name="Son",
        profile_picture=PROFILE_PIC,
        bio="High school teacher by day, koala by night. Founder of Koala Quest. My wife is a cartoonist with a Ph.D., and she co-authors all of these articles.."
    )
    instance14 = User(
        username='username14',
        email='email14@gmail.com',
        password='password14',
        first_name="Erica",
        last_name="Verillo",
        profile_picture=PROFILE_PIC,
        bio="Helping writers get published"
    )
    instance15 = User(
        username='username15',
        email='email15@gmail.com',
        password='password15',
        first_name="Lauren",
        last_name="Sapala",
        profile_picture=PROFILE_PIC,
        bio="Writer. Writing Coach. Author of The INFJ Writer: Cracking the Creative Genius of the Worlds Rarest Type."
    )
    instance16 = User(
        username='username16',
        email='email16@gmail.com',
        password='password16',
        first_name="Daniel",
        last_name="O'Shea",
        profile_picture=PROFILE_PIC,
        bio="The writer, editor, and chief lackey of Knowledge Stew and the Knowledge Stew line of trivia books."
    )
    instance17 = User(
        username='username17',
        email='email17@gmail.com',
        password='password17',
        first_name="Casey",
        last_name="Botticello",
        profile_picture=PROFILE_PIC,
        bio="Entrepreneur, Designer, Blogger | Join 100000+ creators & learn how to make money writing online"
    )
    instance18 = User(
        username='username18',
        email='email18@gmail.com',
        password='password18',
        first_name="Elle",
        last_name="Fredine",
        profile_picture=PROFILE_PIC,
        bio="West-Coaster, born and bred"
    )
    instance19 = User(
        username='username19',
        email='email19@gmail.com',
        password='password19',
        first_name="Elizabeth",
        last_name="Joyce",
        profile_picture=PROFILE_PIC,
        bio="Essayist • Poet • Author"
    )
    instance20 = User(
        username='username20',
        email='email20@gmail.com',
        password='password20',
        first_name="Gus",
        last_name="Gresham",
        profile_picture=PROFILE_PIC,
        bio="Medium Top Writer in Fiction. Interests — the human condition, science, the environment, social justice, family. Also writing non-fiction, life and travel."
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
    db.session.commit()

    return [instance for instance in User.query.all()]


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
