import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Our Timeline",
    page_icon="🎧",
    layout="centered"
)

st.markdown("""
<style>
/* Body background */
body, .main {
    background-color: #fff0f5; /* pastel pink */
    font-family: 'Comic Sans MS', cursive, sans-serif;
    overflow-x: hidden;
}

/* Timeline cards */
.timeline-card {
    background: linear-gradient(145deg, #ffd6e0, #ffe0f0);
    padding: 1.8rem;
    border-radius: 20px;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    transition: transform 0.3s;
    position: relative;
    overflow: hidden;
}
.timeline-card:hover {
    transform: scale(1.03);
}

/* Titles & descriptions */
.timeline-title {
    font-size: 1.5rem;
    font-weight: 700;
}
.timeline-desc {
    color: #333333;
    margin-top: 0.5rem;
    font-size: 1.1rem;
}

/* Spotify iframe */
iframe {
    border-radius: 18px;
    border: 2px dashed #ff69b4;
    margin-top: 0.8rem;
}

/* Long message section */
.long-message {
    background: linear-gradient(145deg, #caffbf, #9bf6ff);
    padding: 2.2rem;
    border-radius: 25px;
    font-size: 1.15rem;
    line-height: 1.75;
    margin-top: 2rem;
    opacity: 0;
    animation: fadeIn 2s forwards;
    animation-delay: 0.5s;
}

/* Divider */
.stDivider {
    border-top: 2px dashed #ff69b4;
    margin: 1.5rem 0;
}

/* Fade-in animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Floating hearts */
.heart {
    position: fixed;
    font-size: 20px;
    color: #ff69b4;
    animation: floatUp 6s linear infinite;
}
@keyframes floatUp {
    0% { transform: translateY(100vh) translateX(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-10vh) translateX(50px) rotate(360deg); opacity: 0; }
}

/* Snowflakes */
.snowflake {
    position: fixed;
    top: -10px;
    color: #fff;
    font-size: 1em;
    z-index: 9999;
    user-select: none;
    pointer-events: none;
    animation: fall linear infinite;
}
@keyframes fall {
    0% { transform: translateY(0) translateX(0); opacity: 1; }
    100% { transform: translateY(110vh) translateX(50px); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# ---------- Animated Floating Hearts + Snow ----------
components.html("""
<script>
// Floating hearts
function createHeart() {
    var heart = document.createElement('div');
    heart.className = 'heart';
    heart.style.left = Math.random() * window.innerWidth + 'px';
    heart.style.animationDuration = 4 + Math.random() * 3 + 's';
    heart.innerHTML = '💖';
    document.body.appendChild(heart);
    setTimeout(() => { heart.remove(); }, 7000);
}
setInterval(createHeart, 500);

// Snowflakes
function createSnow() {
    var snow = document.createElement('div');
    snow.className = 'snowflake';
    snow.style.left = Math.random() * window.innerWidth + 'px';
    snow.style.fontSize = (10 + Math.random() * 20) + 'px';
    snow.style.animationDuration = (5 + Math.random() * 5) + 's';
    snow.innerHTML = '❄️';
    document.body.appendChild(snow);
    setTimeout(() => { snow.remove(); }, 10000);
}
setInterval(createSnow, 300);
</script>
""", height=0)

# ---------- Header ----------
st.title("🎶 Our Timeline Playlist")
st.caption("Moments, music, and feelings — sprinkled with a little magic ✨")

# ---------- Timeline Data ----------
timeline = [
    {
        "title": "💘 When I First Noticed My Feelings for You 💘",
        "description": "That moment when everything suddenly felt so different 😳.",
        "song": "https://open.spotify.com/embed/track/48CiA3IjkNZiyl6S6UbPCy"
    },
    {
        "title": "🎯 When You Started to Matter More",
        "description": "I didn’t even realize I was falling for you 🥰.",
        "song": "https://open.spotify.com/embed/track/06zLpakRZhozCnk3bZnGFT"
    },
    {
        "title": "🎉 Our Sponty Galas",
        "description": "No plans, just us. Loving every second 😎.",
        "song": "https://open.spotify.com/embed/track/6t4CmQGucLORsKZF4M6NNC"
    },
    {
        "title": "💖 Right Now",
        "description": "This is where my heart is 💌.",
        "song": "https://open.spotify.com/embed/track/0kE1SmlJNLg14dgdo9kJws"
    }
]

# ---------- Timeline UI ----------
for i, moment in enumerate(timeline):
    st.markdown(f"""
    <div class="timeline-card">
        <div class="timeline-title">{moment['title']}</div>
        <div class="timeline-desc">{moment['description']}</div>
        <img src="https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif" width="40" style="margin-top:0.5rem;">
    </div>
    """, unsafe_allow_html=True)

    st.components.v1.iframe(
        moment["song"],
        height=152,
        scrolling=False,
        key=f"spotify_{i}"
    )
    st.divider()

# ---------- Long Message Section ----------
st.markdown("## 💌 Merry Christmas to My Favorite Girl")

st.markdown("""
<div class="long-message">
I don’t know when exactly this turned into something real —  
maybe it was slow, maybe it was sudden —  
but somewhere between the laughs, the silence, and the random moments,  
you became someone I carry with me.

These aren’t full songs — just the parts that stayed with me.  
The moments I replayed in my head, even when the music stopped.

If you ever wonder where you stand,  
this is my answer —  
right here, right now 💖✨
</div>
""", unsafe_allow_html=True)

