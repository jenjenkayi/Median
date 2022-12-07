from app.models import db, Story, environment, SCHEMA


def seed_stories():
    instance1 = Story(
        user_id=1,
        title="A Guide to Random from Start to Finish",
        image="https://cdn.pixabay.com/photo/2022/04/24/05/20/flowers-7152917_1280.jpg",
        content="I'm heading back to Colorado tomorrow after being down in Santa Barbara over the weekend for the festival there. I will be making October plans once there and will try to arrange so I'm back here for the birthday if possible. I'll let you know as soon as I know the doctor's appointment schedule and my flight plans. \
                It was a simple tip of the hat. Grace didn't think that anyone else besides her had even noticed it. It wasn't anything that the average person would notice, let alone remember at the end of the day. That's why it seemed so unbelievable that this little gesture would ultimately change the course of the world."
    )
    instance2 = Story(
        user_id=1,
        title="Why Random Is Harder Than You Think",
        image="https://cdn.pixabay.com/photo/2022/02/02/09/47/iceland-6988000_1280.jpg",
        content="It had been her dream for years but Dana had failed to take any action toward making it come true. There had always been a good excuse to delay or prioritize another project. As she woke, she realized she was once again at a crossroads. Would it be another excuse or would she finally find the courage to pursue her dream? Dana rose and took her first step. \
There was nothing to indicate Nancy was going to change the world. She looked like an average girl going to an average high school. It was the fact that everything about her seemed average that would end up becoming her superpower."
    )
    instance3 = Story(
        user_id=2,
        title="15 Random Benefits Everyone Should Know",
        image="https://cdn.pixabay.com/photo/2022/11/01/08/43/mountains-7561636_1280.png",
        content="Sometimes that's just the way it has to be. Sure, there were probably other options, but he didn't let them enter his mind. It was done and that was that. It was just the way it had to be."
    )
    instance4 = Story(
        user_id=2,
        title="The Little Known Benefits of Story",
        image="https://cdn.pixabay.com/photo/2022/07/07/10/46/woman-7306978_1280.jpg",
        content="It was cloudy outside but not really raining. There was a light sprinkle at most and there certainly wasn't a need for an umbrella. This hadn't stopped Sarah from pulling her umbrella out and opening it. It had nothing to do with the weather or the potential rain later that day. Sarah used the umbrella to hide."
    )
    instance5 = Story(
        user_id=2,
        title="25 Books About Story You Should Read",
        image="https://cdn.pixabay.com/photo/2022/10/23/23/43/temple-7542299_1280.jpg",
        content="There was little doubt that the bridge was unsafe. All one had to do was look at it to know that with certainty. Yet Bob didn't see another option. He may have been able to work one out if he had a bit of time to think things through, but time was something he didn't have. A choice needed to be made, and it needed to be made quickly."
    )
    instance6 = Story(
        user_id=2,
        title="7 Helpful Tricks to Making the Most of Your Story",
        image="https://cdn.pixabay.com/photo/2022/10/25/13/28/hanoi-7545860_1280.jpg",
        content="It really shouldn't have mattered to Betty. That's what she kept trying to convince herself even if she knew it mattered to Betty more than practically anything else. Why was she trying to convince herself otherwise? As she stepped forward to knock on Betty's door, she still didn't have a convincing answer to this question that she'd been asking herself for more than two years now. \
Since they are still preserved in the rocks for us to see, they must have been formed quite recently, that is, geologically speaking. What can explain these striations and their common orientation? Did you ever hear about the Great Ice Age or the Pleistocene Epoch? Less than one million years ago, in fact, some 12,000 years ago, an ice sheet many thousands of feet thick rode over Burke Mountain in a southeastward direction. The many boulders frozen to the underside of the ice sheet tended to scratch the rocks over which they rode. The scratches or striations seen in the park rocks were caused by these attached boulders. The ice sheet also plucked and rounded Burke Mountain into the shape it possesses today.5"
    )
    instance7 = Story(
        user_id=3,
        title="10 Things about Article We're Tired of Hearing",
        image="https://cdn.pixabay.com/photo/2022/11/05/22/11/venice-7572877_1280.jpg",
        content="She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work? \
His mother had always taught him not to ever think of himself as better than others. He'd tried to live by this motto. He never looked down on those who were less fortunate or who had less money than him. But the stupidity of the group of people he was talking to made him change his mind."
    )
    instance8 = Story(
        user_id=4,
        title="What Everybody Needs to Know about Article",
        image="https://cdn.pixabay.com/photo/2022/10/18/10/53/dandelion-7529879_1280.jpg",
        content="My pincher collar is snapped on. Then comes the electric zapper collar. Finally, my purple at-home collar is taken off and I know I’m going for a walk to the dog park. I’m so excited to see my friends. I hope Spike or Thunder are there already. They're the most fun to chase and tumble with. My human is pretty strict with me. I’m only allowed on the grass and not on the sidewalks. I think she’s afraid I’m going to jump on the other humans. I don’t understand why everyone else gets to jump on the benches and run wild on the sidewalks. They don’t listen to their humans. I know I could ignore mine but if I do she may zap me and it’s just not worth it. She probably wouldn’t let me back at the dog park if I didn’t listen to her. I just love the dog park."
    )
    instance9 = Story(
        user_id=5,
        title="What Weather Experts Want You to Know",
        image="https://cdn.pixabay.com/photo/2022/10/21/21/17/interior-7537974_1280.jpg",
        content="Begin today! That's all the note said. There was no indication from where it came or who may have written it. Had it been meant for someone else? Meghan looked around the room, but nobody made eye contact back. For a brief moment, she thought it might be a message for her to follow her dreams, but ultimately decided it was easier to ignore it as she crumpled it up and threw it away."
    )
    instance10 = Story(
        user_id=6,
        title="The Ultimate Guide to the Weather Gadgets That You Need",
        image="https://cdn.pixabay.com/photo/2022/10/23/09/07/bicycle-7540835_1280.png",
        content="The picket fence had stood for years without any issue. That's all it was. A simple, white, picket fence. Why it had all of a sudden become a lightning rod within the community was still unbelievable to most. Yet a community that had once lived in harmony was now divided in bitter hatred and it had everything to do with the white picket fence."
    )
    instance11 = Story(
        user_id=7,
        title="Why Everyone Is Talking About Weather Right Now",
        image="https://cdn.pixabay.com/photo/2022/10/03/23/41/house-7497001_1280.png",
        content="Rhonda prided herself on always taking the path less traveled. She'd decided to do this at an early age and had continued to do so throughout her entire life. It was a point of pride and she would explain to anyone who would listen that doing so was something that she'd made great efforts to always do. She'd never questioned this decision until her five-year-old niece asked her, So, is this why your life has been so difficult? and Rhonda didn't have an answer for her. \
The wave crashed and hit the sandcastle head-on. The sandcastle began to melt under the waves force and as the wave receded, half the sandcastle was gone. The next wave hit, not quite as strong, but still managed to cover the remains of the sandcastle and take more of it away. The third wave, a big one, crashed over the sandcastle completely covering and engulfing it. When it receded, there was no trace the sandcastle ever existed and hours of hard work disappeared forever."
    )
    instance12 = Story(
        user_id=8,
        title="The History of Rain in 10 Milestones",
        image="https://cdn.pixabay.com/photo/2022/09/29/01/26/lighthouse-7486290_1280.jpg",
        content="I'm meant to be writing at this moment. What I mean is, I'm meant to be writing something else at this moment. The document I'm meant to be writing is, of course, open in another program on my computer and is patiently awaiting my attention. Yet here I am plonking down senseless sentiments in this paragraph because it's easier to do than to work on anything particularly meaningful. I am grateful for the distraction. \
The towels had been hanging from the rod for years. They were stained and worn, and quite frankly, just plain ugly. Debra didn't want to touch them but she really didn't have a choice. It was important for her to see what was living within them."
    )
    instance13 = Story(
        user_id=9,
        title="Is Rain as Important as Everyone Says?",
        image="https://cdn.pixabay.com/photo/2020/11/21/11/17/houses-5763699_1280.jpg",
        content="He heard the song coming from a distance, lightly floating over the air to his ears. Although it was soft and calming, he was wary. It seemed a little too soft and a little too calming for everything that was going on. He wanted it to be nothing more than beautiful music coming from the innocent and pure joy of singing, but in the back of his mind, he knew it was likely some type of trap. \
The red ball sat proudly at the top of the toybox. It had been the last to be played with and anticipated it would be the next as well. The other toys grumbled beneath. At one time each had held the spot of the red ball, but over time they had sunk deeper and deeper into the toy box."
    )
    instance14 = Story(
        user_id=10,
        title="Promote Your Rain Idea in 7 Easy Steps",
        image="https://cdn.pixabay.com/photo/2018/06/17/17/48/pen-3481061__480.jpg",
        content="The wave roared towards them with speed and violence they had not anticipated. They both turned to run but by that time it was too late. The wave crashed into their legs sweeping both of them off of their feet. They now found themselves in a washing machine of saltwater, getting tumbled and not know what was up or down. Both were scared, not knowing how this was going to end, but it was by far the best time of the trip thus far. \
There was something beautiful in his hate. It wasn't the hate itself as it was a disgusting display of racism and intolerance. It was what propelled the hate and the fact that although he had this hate, he didn't understand where it came from. It was at that moment that she realized that there was hope in changing him. \
Nobody really understood Kevin. It wasn't that he was super strange or difficult. It was more that there wasn't enough there that anyone wanted to take the time to understand him. This was a shame as Kevin had many of the answers to the important questions most people who knew him had. It was even more of a shame that they'd refuse to listen even if Kevin offered to give them the answers. So, Kevin remained silent, misunderstood, and kept those important answers to life to himself."
    )
    instance15 = Story(
        user_id=11,
        title="Who's the World's Top Expert in Snow?",
        image="https://cdn.pixabay.com/photo/2022/10/05/08/21/autumn-7500200__480.jpg",
        content="There was a time and a place for Stephanie to use her magic. The problem was that she had a difficult time determining this. She wished she could simply use it when the desire hit and there wouldn't be any unforeseen consequences. Unfortunately, that's not how it worked and the consequences could be devastating if she accidentally used her magic at the wrong time."
    )
    instance16 = Story(
        user_id=12,
        title="How to Find the Perfect Snow Online",
        image="https://cdn.pixabay.com/photo/2022/09/01/09/31/sunset-glow-7425170__340.jpg",
        content="He was after the truth. At least, that's what he told himself. He believed it, but any rational person on the outside could see he was lying to himself. It was apparent he was really only after his own truth that he'd already decided and was after this truth because the facts didn't line up with the truth he wanted. So he continued to tell everyone he was after the truth oblivious to the real truth sitting right in front of him. \
Twenty-five hours had passed since the incident. It seemed to be a lot longer than that. That twenty-five hours seemed more like a week in her mind. The fact that she still was having trouble comprehending exactly what took place wasn't helping the matter. She thought if she could just get a little rest the entire incident might make a little more sense."
    )
    instance17 = Story(
        user_id=13,
        title="How Snow Changed My Life for the Better",
        image="https://cdn.pixabay.com/photo/2022/07/06/20/56/landscape-7306014__480.jpg",
        content="She never liked cleaning the sink. It was beyond her comprehension how it got so dirty so quickly. It seemed that she was forced to clean it every other day. Even when she was extra careful to keep things clean and orderly, it still ended up looking like a mess in a couple of days. What she didn't know was there was a tiny creature living in it that didn't like things neat."
    )
    instance18 = Story(
        user_id=14,
        title="Who's the World's Top Expert in Snow?",
        image="https://cdn.pixabay.com/photo/2022/09/22/04/23/seascape-7471616__480.jpg",
        content="The shades were closed keeping the room dark. Peter knew that he should open them and let in the sunlight so he could begin the day, but he didn't have the energy or willpower. Nothing had gone as expected the day before and he no longer wanted to spend the energy to begin a new day. He stared at the shades wondering if there was a way to disappear from the reality of the world for the rest of the day."
    )
    instance19 = Story(
        user_id=15,
        title="Why Windy Is the Reprieve We All Need Right Now",
        image="https://cdn.pixabay.com/photo/2016/12/27/17/10/pendulum-1934311__480.jpg",
        content="Then came the night of the first falling star. It was seen early in the morning, rushing over Winchester eastward, a line of flame high in the atmosphere. Hundreds must have seen it and taken it for an ordinary falling star. It seemed that it fell to earth about one hundred miles east of him."
    )
    instance20 = Story(
        user_id=16,
        title="The History of Windy in 10 Milestones",
        image="https://cdn.pixabay.com/photo/2022/09/09/11/33/silver-wattle-7442792__480.jpg",
        content="She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work? \
Green vines attached to the trunk of the tree had wound themselves toward the top of the canopy. Ants used the vine as their private highway, avoiding all the creases and crags of the bark, to freely move at top speed from top to bottom or bottom to top depending on their current chore. At least this was the way it was supposed to be. Something had damaged the vine overnight halfway up the tree leaving a gap in the once pristine ant highway."
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


def undo_stories():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM stories")

    db.session.commit()
