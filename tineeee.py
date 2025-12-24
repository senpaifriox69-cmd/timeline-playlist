import streamlit as st

st.set_page_config(
    page_title="Our Timeline",
    page_icon="🎧",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
/* Overall background */
body, .main {
    background: linear-gradient(135deg, #ffe0f0, #ffd6e0); /* cute pink gradient */
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Timeline cards */
.timeline-card {
    background: linear-gradient(145deg, #ffebf0, #ffcce0); /* lighter pink for cards */
    padding: 1.8rem;
    border-radius: 20px;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    position: relative;
}

/* Titles & descriptions */
.timeline-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #d63384; /* darker pink for titles */
    margin-bottom: 0.3rem;
}
.timeline-desc {
    color: #6a1b4d; /* dark magenta/purple for text */
    font-size: 1.1rem;
    margin-bottom: 0.8rem;
}

/* Image placeholder */
.timeline-image {
    width: 100%;
    height: 200px;
    background-color: #ffd6e0;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #d63384;
    font-size: 1rem;
    margin-bottom: 1rem;
    border: 2px dashed #d63384;
}

/* Spotify iframe */
iframe {
    border-radius: 12px;
    border: 2px dashed #d63384;
    margin-bottom: 1rem;
}

/* Long message section */
.long-message {
    background: linear-gradient(145deg, #ffcce0, #ffb6c1);
    padding: 2rem;
    border-radius: 25px;
    font-size: 1.1rem;
    line-height: 1.7;
    margin-top: 2rem;
    color: #6a1b4d;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("🎶 Our Timeline Playlist")
st.caption("Songs, moments, and feelings — wrapped in a cute Christmas vibe 🎄💖")

# ---------- Timeline Data ----------
timeline = [
    {
        "title": "When I First Noticed My Feelings for You",
        "description": "That moment when I knew I was going on a crazy ride.",
        "song": "https://open.spotify.com/embed/track/48CiA3IjkNZiyl6S6UbPCy?start=33"
    },
    {
        "title": "When You Started to Matter More",
        "description": "And I didn’t even realize I was falling for you.",
        "song": "https://open.spotify.com/embed/track/06zLpakRZhozCnk3bZnGFT?start=22"
    },
    {
        "title": "Our Sponty Galas",
        "description": "Doing random things with no plans — cherishing every single moment of it",
        "song": "https://open.spotify.com/embed/track/6t4CmQGucLORsKZF4M6NNC?start=42"
    },
    {
        "title": "Right Now",
        "description": "This is where my heart is.",
        "song": "https://open.spotify.com/embed/track/0kE1SmlJNLg14dgdo9kJws?start=174"
    }
]

# ---------- Timeline UI ----------
for moment in timeline:
    st.markdown(f"""
    <div class="timeline-card">
        <div class="timeline-title">{moment['title']}</div>
        <div class="timeline-desc">{moment['description']}</div>
        <div class="timeline-image">Image Placeholder 🎄</div>
    </div>
    """, unsafe_allow_html=True)

    st.components.v1.iframe(
        moment["song"],
        height=152,
        scrolling=False
    )

# ---------- Long Message ----------
st.markdown("## Merry Christmas to mi Favorite Girl 💖🎄")

st.markdown("""
<div class="long-message">
HELLOOO MERRY CHRISTMAS TO YOU MI FAVORITE GIRL, I know this isn't much for a Christmas surprise but I hope you like this. Eto na rin yung part 2 ng letter ko hehehe.

</div>
""", unsafe_allow_html=True)
