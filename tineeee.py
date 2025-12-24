import streamlit as st

st.set_page_config(
    page_title="Our Timeline",
    page_icon="🎧",
    layout="centered"
)

st.markdown("""
<style>
body, .main {
    background-color: #cceeff;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

.timeline-card {
    background: linear-gradient(145deg, #ffe0f0, #ffd6e0);
    padding: 1.8rem;
    border-radius: 20px;
    margin-bottom: 1rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.timeline-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #d63384;
}

.timeline-desc {
    color: #6a1b4d;
    font-size: 1.1rem;
    margin-bottom: 1rem;
}

iframe {
    border-radius: 12px;
    border: 2px dashed #d63384;
    margin-bottom: 2rem;
}

.long-message {
    background: linear-gradient(145deg, #ffcce0, #ffb6c1);
    padding: 2rem;
    border-radius: 25px;
    font-size: 1.1rem;
    line-height: 1.7;
    color: #6a1b4d;
}
</style>
""", unsafe_allow_html=True)

st.title("🎶 Our Timeline Playlist")
st.caption("Thank You for being in my 2025 💘🥰")

timeline = [
    {
        "title": "When I First Noticed My Feelings for You",
        "description": "That moment when I knew I was going on a crazy ride. Never knew that I would start having these deep deep feelings for you.",
        "song": "https://open.spotify.com/embed/track/48CiA3IjkNZiyl6S6UbPCy",
        "image": "./image/WIFNMFY.jpg"
    },
    {
        "title": "When You Started to Matter More",
        "description": "And I didn’t even realize I was falling for you. They told me that I fell deep into this rabbit hole of loving you",
        "song": "https://open.spotify.com/embed/track/06zLpakRZhozCnk3bZnGFT",
        "image": "./image/WYSMM.jpg"
    },
    {
        "title": "Our Sponty Galas",
        "description": "Doing random things with no plans — just us, enjoying every moment. Every time this happens, I find myself looking forward to whatever we’ll do next, as long as it’s with you.",
        "song": "https://open.spotify.com/embed/track/6t4CmQGucLORsKZF4M6NNC",
        "image": "./image/OURSPONTYGALAS.jpg"
    },
    {
        "title": "Right Now",
        "description": "And now my heart is with you Tine.",
        "song": "https://open.spotify.com/embed/track/0kE1SmlJNLg14dgdo9kJws",
        "image": "./image/RIGHTNOW.jpg"
    }
]

for moment in timeline:
    st.markdown(f"""
    <div class="timeline-card">
        <div class="timeline-title">{moment['title']}</div>
        <div class="timeline-desc">{moment['description']}</div>
    </div>
    """, unsafe_allow_html=True)


    st.image(moment["image"], use_container_width=True)

    st.components.v1.iframe(
        moment["song"],
        height=152,
        scrolling=False
    )

st.markdown("## 💌 Merry Christmas to mi Favorite Girl 🎄💖")

st.markdown("""
<div class="long-message">
HELLOOO MERRY CHRISTMAS TO YOU MI FAVORITE GIRL 💖. I know this isn't much of a Christmas surprise but I hope you like this. Eto na rin yung part 2 ng letter ko hehehe because you deserve more than 1 part of a letter. I feel like mauubos writing juice ko dito but if it's for you then okay lang.


I had one of if not the best year of my life, especially because you were in it. There are days when I randomly remember our moments, even the smallest ones, I catch myself smiling like an idiot. Even tho sobrang simple lang ng mga nangyari, as long as it’s with you, it replays my over and over again na para bang movie scene. The way you laugh, the way you smile, the way you react pag like I have surprises for you—those little things stayed with me more than I expected it to be. Sometimes I realize that you aren’t just a random passerby in my life; you’re someone who loudly settled in my life and especially in my heart and mind.

You became my “I wish you were here” person. Whenever something funny happens, or I see something that I knew you would like, or I experience anything even slightly interesting, my first thought is always “Sana andito ka sa tabi ko” or “I will make kwento it to Tine later.” And that’s when I knew it was different—because not everyone becomes the person I want to share my day with by default and yet nagging ikaw yun (grabe ang galing mo talaga). Kaya nga nung hindi tayo nagusap ng 1 month andami kong kwento sayo kasi I really want to share it with you, because I wanted you to be by my side that time.

Falling in love with you this year was one hell of an experience. I never knew that once I really—like really—fell in love with a girl, I would act this way. Giving flowers, writing poems, making long messages, DIY gifts, and handwritten letters. I never thought I, out of all people, would be like this. Most of our close moots just think I’m this kupal and ragebaiter type of person, but falling in love with you brought out this “loverboy” version of me. And I feel like lumabas lang siya because “ikaw” yung taong gusto ko—not anybody else. You brought out one of the best, if not the best, versions of me, and I’m really glad that you, Justine, made me like this.

And honestly, I’m not ashamed nor embarrassed that I’m this soft when it comes to you. If anything, I’m proud—because ikaw nagpatiklop sakin and loving you made me kinder, more patient, more thoughtful. YOU made me want to try, to show up, to care loudly instead of pretending I don’t. No other girl can make me act like this, I can assure you that. You also made me realize that being soft and gentle with someone isn’t a sign of weakness; sometimes it’s proof of how deeply someone matters.

There were moments when I got scared of how strong my feelings became. Yung tipong mapapatanong ako sa sarili. “What if mawala sya?” or “What if all of these would change?” But even with that fear I’d still choose this, choose you—every single time. Because loving you, with all the uncertainty and all the vulnerability that comes with it, is still one of the best things that ever happened to me. And I do think that all of these were worth it because here you are, with me, celebrating our first Christmas together.

I don’t know exactly what the future has planned for us, but I do know this: I want to keep choosing you in all the simplest, everyday ways. I still want to hear you laughs sa mga corny jokes natin, see you get flustered to my small surprises, take photobooths together and to be with you at every random galas even tho wala tayong clear plan. I want more soft mornings, more late-night talk kahit parehas tayong inaantok na, more “late na pero ayaw pa umuwi” meoments with you.

So here’s my quiet promise—no pressure, no grand declaration—just me being bare and honest:

As long as I’m in your life, I’ll do my best to be someone who makes you feel safe, appreciated, and chosen. Someone you can run to when things get heavy. Someone who listens. Someone who stays. I’ll do my best to make you the happiest girl in the world and to treat you the way you deserve to be treated, Tine.

Merry Christmas again, my favorite girl, and sa family mo. Thank you for being the reason this year felt more different than usual. And thank you for letting me love you the way I do. (I REALLY MISS YOU NA TALAGA)

</div>
""", unsafe_allow_html=True)




