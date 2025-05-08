


import streamlit as st
import csv
from utils.lead_logger import save_lead

def is_valid_postcode(postcode):
    with open(r"C:\Users\user\Downloads\Assignment\uk_postcodes 1.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        return postcode.upper() in [row[0].strip().upper() for row in reader]

def handle_buy_flow():
    if "step" not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        st.session_state.home_type = st.radio("Are you looking for a new home or a resale home?", ["new", "resale"])
        if st.button("Next"):
            st.session_state.step += 1

    elif st.session_state.step == 2:
        st.session_state.name = st.text_input("👤 Your name:")
        if st.session_state.name:
            st.session_state.step += 1

    elif st.session_state.step == 3:
        st.session_state.phone = st.text_input("📞 Phone number:")
        if st.session_state.phone:
            st.session_state.step += 1

    elif st.session_state.step == 4:
        st.session_state.email = st.text_input("✉️ Email address:")
        if st.session_state.email:
            st.session_state.step += 1

    elif st.session_state.step == 5:
        st.session_state.budget = st.number_input("💰 Your budget :")
        if st.session_state.budget > 0:
            if st.session_state.budget < 1000000 and st.session_state.home_type == "new":
                st.error("❌ We don't have new homes under 1 million. Please contact our office.")
                return False, None, None, None, None, None, None

            # Skip postcode step for resale buyers
            if st.session_state.home_type == "resale":
                st.session_state.location = "N/A"  # Optional: since resale skips postcode
                st.session_state.step = 7
            else:
                st.session_state.step += 1

    elif st.session_state.step == 6:
        st.session_state.location = st.text_input("📍 Can I know the postcode of your location of interest?")
        if st.session_state.location:
            if not is_valid_postcode(st.session_state.location):
                st.error("❌ Sorry, we don’t cater to postcodes that you provided. "
                         "Please contact our office on 1800 111 122 to get help.")
                return False, None, None, None, None, None, None
            st.session_state.step += 1

    elif st.session_state.step == 7:
        st.markdown("✅ I can expect someone to get in touch with you within 24 hours via phone or email.")
        further_help = st.radio("Is there anything else I can help you with?", ["Yes", "No"])

        if further_help == "Yes":
            st.info("💬 How can I help you?")
            # Optional: continue or restart
        elif further_help == "No":
            save_lead(
                intent="BUY",
                name=st.session_state.name,
                location=st.session_state.location,
                budget=st.session_state.budget,
                phone=st.session_state.phone,
                email=st.session_state.email,
                home_type=st.session_state.home_type,
            )
            st.success("✅ Lead info saved!")
            st.markdown("👋 Thank you for chatting with us. Goodbye!")
            return True, st.session_state.name, st.session_state.phone, st.session_state.email, st.session_state.location, st.session_state.budget, st.session_state.home_type
# This is for FastAPI
def handle_buy_flow_api(name, location, phone, email, budget=None, home_type=None):
    from utils.lead_logger import save_lead

    save_lead(
        intent="BUY",
        name=name,
        location=location,
        phone=phone,
        email=email,
        budget=budget,
        home_type=home_type
    )

    return {
        "status": "saved",
        "name": name,
        "location": location,
        "budget": budget,
        "phone": phone,
        "email": email,
        "home_type": home_type
    }
    return None
