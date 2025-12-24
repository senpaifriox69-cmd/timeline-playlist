import streamlit as st

st.set_page_config(page_title="Our Timeline", page_icon="🎧")

st.title("🎶 Our Timeline Playlist")
st.caption("Songs, moments, and feelings—one timeline.")

timeline = [
    {
        "title": "When I First Noticed My Feelings for You",
        "description": "That moment when everything feels so different.",
        "song": "https://youtu.be/izVXgdiTcQ8?si=atwtBskYK6Jwkk1h?start=32&end=66"
    },
    {   
        "title": "When You Started to Matter More",
        "description": "And I didn’t even realize it that I was falling for you.",
        "song": "https:/https://youtu.be/KsbxOp496A4?si=L2cSXexbdClLegAl?start=20&end=73"
    },
    {
        "title": "Our Sponty Galas",
        "description": "Doing random things without plans but loving every second of it.",
        "song": "https://music.youtube.com/watch?v=bgCansrDpVo&si=i2XJAfktKYEWB4V-?start=42"
    },
    {
        "title": "Right Now",
        "description": "This is where my heart is.",
        "song": "https://music.youtube.com/watch?v=GpQ63UI7mQc&si=NLTGa7hmgbirIwtr?start=206&end=236"
    }
]

for moment in timeline:
    st.subheader(moment["title"])
    st.write(moment["description"])
    st.components.v1.iframe(moment["song"], height=152)
    st.divider()
