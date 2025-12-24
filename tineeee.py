import streamlit as st

st.set_page_config(page_title="Our Timeline", page_icon="🎧")

st.title("🎶 Our Timeline Playlist")
st.caption("Songs, moments, and feelings—one timeline.")

timeline = [
    {
        "title": "When I First Noticed My Feelings for You",
        "description": "That moment when everything feels so different.",
        "song": "https://open.spotify.com/track/48CiA3IjkNZiyl6S6UbPCy?si=efccc71ac7f043d4"
    },
    {   
        "title": "When You Started to Matter More",
        "description": "And I didn’t even realize it that I was falling for you.",
        "song": "https://open.spotify.com/track/06zLpakRZhozCnk3bZnGFT?si=7b149526e57d404b?start=22"
        
    },
    {
        "title": "Our Sponty Galas",
        "description": "Doing random things without ",
        "song": "https://open.spotify.com/track/6t4CmQGucLORsKZF4M6NNC?si=0b5d0cb5d2cd4939?start=42"
    },
    {
        "title": "Right Now",
        "description": "This is where my heart is.",
        "song": "https://open.spotify.com/track/0kE1SmlJNLg14dgdo9kJws?si=cf0e99c76dfa42dc?start=174"
    }
]

for moment in timeline:
    st.subheader(moment["title"])
    st.write(moment["description"])
    st.components.v1.iframe(moment["song"], height=80)
    st.divider()
