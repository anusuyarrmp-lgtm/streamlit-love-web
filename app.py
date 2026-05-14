import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Love Space 💖",
    page_icon="🌷",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #dff6ff;
}

.title {
    text-align: center;
    color: #3b82f6;
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 20px;
}

.love-box {
    background-color: white;
    color: black;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌷 Love General 🌷</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">A cute Streamlit webpage with tabs, bars, and love letters ✨</p>',
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("💌 Navigation")

page = st.sidebar.radio(
    "Choose a section",
    ["Home", "Love Meter", "Love Letter", "Memories"]
)

# HOME PAGE
if page == "Home":

    st.image(
        "https://images.unsplash.com/photo-1520763185298-1b434c919102",
        use_container_width=True
    )

    st.markdown("## 🌸 Welcome")

    st.write("""
    This is a romantic themed webpage made by ANU

    Features:
    - Beautiful tabs
    - Love meter progress bars
    - Written love letters
    - Memory section
    """)

    # Tabs
    tab1, tab2, tab3 = st.tabs(
        ["💖 Feelings", "🌹 Quotes", "✨ Future"]
    )

    with tab1:
        st.success(
            "Love is not about perfection, it's about connection ❤️"
        )

    with tab2:
        st.info(
            '"You are my today and all of my tomorrows."'
        )

    with tab3:
        st.write(
            "Dream together. Grow together. Stay together 💞"
        )

# LOVE METER PAGE
elif page == "Love Meter":

    st.markdown("## 💘 Love Meter")

    name1 = st.text_input("Your Name")
    name2 = st.text_input("Partner Name")

    if st.button("Check Love 💞"):

        score = (len(name1) * len(name2) * 7) % 100

        st.progress(score)

        if score > 80:
            st.success(f"💖 {score}% - Soulmate vibes!")

        elif score > 50:
            st.info(f"💕 {score}% - Strong connection!")

        else:
            st.warning(f"💔 {score}% - Needs more communication!")

# LOVE LETTER PAGE
elif page == "Love Letter":

    st.markdown("## 💌 Written Love Letter")

    letter = """
    My Dear,

    Every moment with you feels like a beautiful dream.
    Your smile brings peace to my heart and happiness to my soul.

    No matter how busy life gets,
    you will always be my favorite thought.

    Yours forever ❤️
    """

    st.markdown(
        f'<div class="love-box">{letter}</div>',
        unsafe_allow_html=True
    )

    user_letter = st.text_area("✍️ Write your own letter")

    if st.button("Save Letter"):
        st.success("Your love letter is saved in memories 💖")

# MEMORIES PAGE
elif page == "Memories":

    st.markdown("## 📸 Memories Timeline")

    memories = [
        ("🌸 First Meeting", "The day everything started."),
        ("💞 First Talk", "Hours felt like minutes."),
        ("🌹 Special Moment", "A memory to cherish forever."),
        ("✨ Future Dreams", "More adventures together.")
    ]

    for title, desc in memories:

        st.markdown(f"""
        <div class="love-box" style="margin-bottom:15px;">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")

st.caption(
    f"Made with ❤️ using Streamlit • {datetime.now().year}"
)
