import streamlit as st
import csv
from utils.lead_logger import save_lead

def is_valid_postcode(postcode):
    with open(r"C:\Users\user\Downloads\Assignment\uk_postcodes 1.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        return postcode.upper() in [row[0].strip().upper() for row in reader]

def handle_sell_flow():
    if "sell_step" not in st.session_state:
        st.session_state.sell_step = 1

    if st.session_state.sell_step == 1:
        selling = st.radio("Are you looking to sell a property?", ["yes", "no"])
        if selling == "no":
            st.warning("Alright. Let us know if you need help in the future.")
            return False, None, None, None, None, None
        if st.button("Next"):
            st.session_state.sell_step += 1

    elif st.session_state.sell_step == 2:
        st.session_state.has_buyer = st.radio("Do you already have a buyer?", ["yes", "no"])
        if st.button("Next"):
            st.session_state.sell_step += 1

    elif st.session_state.sell_step == 3:
        st.session_state.name = st.text_input("👤 Your name:")
        if st.session_state.name:
            st.session_state.sell_step += 1

    elif st.session_state.sell_step == 4:
        st.session_state.phone = st.text_input("📞 Phone number:")
        if st.session_state.phone:
            st.session_state.sell_step += 1

    elif st.session_state.sell_step == 5:
        st.session_state.email = st.text_input("✉️ Email address:")
        if st.session_state.email:
            st.session_state.sell_step += 1

    elif st.session_state.sell_step == 6:
        st.session_state.postcode = st.text_input("📍 What is your postcode?")
        if st.session_state.postcode:
            if not is_valid_postcode(st.session_state.postcode):
                st.error("❌ Sorry, we don’t cater to the postcode you provided. Please call 1800 111 222.")
                return False, None, None, None, None, None
            st.session_state.sell_step += 1

    elif st.session_state.sell_step == 7:
        st.markdown("✅ I can expect someone to get in touch with you within 24 hours via phone or email.")

        further_help = st.radio("Is there anything else I can help you with?", ["yes", "no"])
        if further_help == "Yes":
            st.info("💬 How can I help you?")
            # Optional: continue or restart
        elif further_help == "No":
            save_lead(
                intent="SELL",
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
def handle_sell_flow_api(name, location, phone, email, postcode):
    from utils.lead_logger import save_lead

    save_lead(
        intent="SELL",
        name=name,
        location=location,
        phone=phone,
        email=email,
        postcode=postcode
    )

    return {
        "status": "success",
        "intent": "SELL",
        "name": name,
        "location": location,
        "postcode": postcode,
        "phone": phone,
        "email": email
    }
    return None
