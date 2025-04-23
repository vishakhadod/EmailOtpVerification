import streamlit as st
import random
import smtplib
from email.message import EmailMessage

st.title("📧 Email OTP Verification")

from_mail=st.text_input("Enter your Gmail address (sender):")
to_mail=st.text_input("Enter recipient email:")

# OTP Generation
if st.button("Generate & Send OTP"):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    st.session_state.otp=otp  

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('vishakhadod240@gmail.com','adjg ktqw ftiq msyu')

        msg = EmailMessage()
        msg['Subject']="OTP Verification"
        msg['From']=from_mail
        msg['To']=to_mail
        msg.set_content(f"Your OTP is: {otp}")

        server.send_message(msg)
        server.quit()
        st.success("OTP has been sent to your email!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# OTP Verification
if "otp" in st.session_state:
    input_otp = st.text_input("Enter the OTP you received:")

    if st.button("Verify OTP"):
        if input_otp==st.session_state.otp:
            st.success("✅ OTP Verified Successfully!")
        else:
            st.error("❌ Invalid OTP. Please try again.")

