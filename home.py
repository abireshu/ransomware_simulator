import streamlit as st

st.set_page_config(
    page_title="Ransomware Simulator",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .stPageLink {
        font-size: 1.2rem;
        padding: 0.5rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("💻 Ransomware Simulation")
st.markdown("***Educational demonstration!***")

#st.page_link("app.py", label="🏠 Home", icon="🏠")
st.page_link("pages/files.py", label="📂 My Files", )
#st.page_link("pages/pay.py", label="💳 Payment Portal", icon="💳")

st.markdown("---")
st.info("ℹ This is a simulation for educational purposes only.")
