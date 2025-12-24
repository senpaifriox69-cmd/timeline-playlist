import streamlit as st

st.set_page_config(
    page_title="Our Timeline"
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
HELLOOO MERRY CHRISTMAS TO YOU MI FAVORITE GIRL 💖  
I know this isn't much for a Christmas surprise but I hope you like this.  
Eto na rin yung part 2 ng letter ko hehehe.
</div>
""", unsafe_allow_html=True)

