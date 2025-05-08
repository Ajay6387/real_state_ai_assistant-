import streamlit as st
from agents.buyer_flow_agent import handle_buy_flow
from agents.seller_flow_agent import handle_sell_flow

st.set_page_config(page_title="AI Real Estate Assistant", page_icon="🏠")
st.title("🏠 AI Real Estate Assistant")
st.write("Welcome! Type your intent below (e.g., 'I want to buy/sell a house in London').")

# Initial user input for intent detection
user_input = st.text_input("💬 Enter your message:")

if user_input:
    if "buy" in user_input.lower():
        st.session_state.agent_decision = "BUY"
    elif "sell" in user_input.lower():
        st.session_state.agent_decision = "SELL"
    else:
        st.warning("Sorry, we couldn't understand your intent. Please specify 'buy' or 'sell'.")
        st.stop()

    st.markdown(f"🤖 Agent decided: **{st.session_state.agent_decision}**")

    # Tab-based UI for BUY / SELL flows
    tab1, tab2 = st.tabs(["💼 Buy", "🏡 Sell"])

    with tab1:
        if st.session_state.agent_decision == "BUY":
            handle_buy_flow()

    with tab2:
        if st.session_state.agent_decision == "SELL":
            handle_sell_flow()
