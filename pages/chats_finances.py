import streamlit as st

st.title("Bank Balance Simulation")

if "balance" not in st.session_state:
    st.session_state.balance = 0

# --- placeholder at the top ---
balance_display = st.empty()

# --- ADD MONEY ---
add_amount = st.number_input("Enter amount to add (£):", min_value=0, step=1, key="add_amount")
if st.button("Add Money"):
    st.session_state.balance += add_amount
    st.success(f"You added £{add_amount} to your account!")

# --- WITHDRAW MONEY ---
withdraw_amount = st.number_input("Enter amount to withdraw (£):", min_value=0, step=1, key="withdraw_amount")
if st.button("Withdraw Money"):
    st.session_state.balance -= withdraw_amount
    st.success(f"You withdrew £{withdraw_amount} from your account!")

#  update the placeholder at the very end
balance_display.markdown(
    f"### 💰 Your current bank balance is: **£{st.session_state.balance}**"
)

