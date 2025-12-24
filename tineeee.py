import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Our Timeline",
    page_icon="🎧",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
/* Body background */
body, .main {
    background: linear-gradient(135deg, #ffe0f0, #ffd6e0);
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #222;
    overflow-x: hidden;
}

/* Timeline cards */
.timeline-card {
    background: linear-gradient(145deg, #ffb6c1, #ffc0cb);
    padding: 1.8rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    position: relative;
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.8s ease-out;
}
.timeline-card.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Card decorations */
.timeline-card::after {
    content: "✨🎄❄️";
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 1.2rem;
}

/* Titles & descriptions */
.timeline-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.timeline-desc {
    font-size: 1.1rem;
}

/* Spotify iframe */
iframe {
    border-radius: 16px;
    border: 2px dashed #ff69b4;
    margin-top: 0.8rem;
}

/* Long message section */
.long-message {
    background: linear-gradient(145deg, #ffe6f0, #ffccd9);
    padding: 2rem;
    border-radius: 25px;
    font-size: 1.15rem;
    line-height: 1.7;
    margin-top: 2rem;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    opacity: 0;
    transform: translateY(50px);
    transition: all 1s ease-out;
}
.long-message.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Floating hearts */
.heart {
    position: fixed;
    font-size: 20px;
    color: #ff69b4;
    animation: floatUp 6s linear infinite;
    z-index: 9999;
}
@keyframes floatUp {
    0% { transform: translateY(100vh) translateX(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-10vh) translateX(50px) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# ---------- Animated Hearts + Scroll Reveal ----------
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

// Scroll reveal for cards
function revealOnScroll() {
    const cards = document.querySelectorAll('.timeline-card');
    const longMessage = document.querySelector('.long-message');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if(entry.isIntersecting){
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });

    cards.forEach(card => observer.observe(card));
    if(longMessage) observer.observe(longMessage);
}
document.addEventListener('DOMContentLoaded', revealOnScroll);
</script>
""", height=0)

# ---------- Header ----------
st.title("🎶 Our Timeline Playlist")
st.caption("Moments, music, and feelings — sprinkled with a little Christmas magic ✨🎄")

# ---------- Timeline Data ----------
timeline = [
    {
        "title": "💘 When I First Noticed My Feelings for You 💘",
        "description": "That moment when I knew I was going on a crazy ride 😳.",
        "song": "https://open.spotify.com/embed/track/48CiA3IjkNZiyl6S6UbPCy"
    },
    {
        "title": "🎯 When You Started to Matter More",
        "description": "And I didn’t even realize I was falling for you 🥰.",
        "song": "https://open.spotify.com/embed/track/06zLpakRZhozCnk3bZnGFT"
    },
    {
        "title": "🎉 Our Sponty Galas",
        "description": "Doing random things with no plans — cherishing every single moment 😎",
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
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.components.v1.iframe(
        moment["song"],
        height=152,
        scrolling=False
    )

# ---------- Long Message ----------
st.markdown("## 💌 Merry Christmas to My Favorite Girl")

st.markdown("""
<div class="long-message">
HELLOOO MERRY CHRISTMAS TO YOU MI FAVORITE GIRL! 🎄💖  
I know this isn't much for a Christmas surprise, but I hope you like this.  
Eto na rin yung part 2 ng letter ko hehehe. ✨❄️
</div>
""", unsafe_allow_html=True)


