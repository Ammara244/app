import streamlit as st

st.title('Bank Balance Simulation')

st.write('updated')

# creating account
if "balance" not in st.session_state:
    st.session_state.balance = 0

# placeholder on page where balance will always be displayed
balance_display = st.empty()
balance_display.text(f'Your current bank balance is: £{st.session_state.balance}')

# add initial balance
initial_balance = st.number_input(
    "Enter Current Balance (£):", 
    min_value=0,        # makes sure they dont put negative number
    step=1, # i think this lets the pick a number by pressing the up/down
    value=st.session_state.balance,  # sets original number in box as 0
    key="balance_input",  # this input box is called 'balance_input', it doesnt change
)

balance_display.text(f'Your current bank balance is: £{st.session_state.balance}')

st.write('Your current bank balance is ', st.session_state.balance)

if st.button('Add Money'):
    amount = st.number_input('Enter Amount')
    st.session_state.balance += amount
    st.success(f'You added £{amount} to your account!')
    balance_display.text(f'Your current bank balance is: £{st.session_state.balance}')
  
if st.button('Withdraw Money'):
    amount = st.number_input('Enter Amount')
    st.session_state.balance -= amount
    st.success(f'You withdrew £{amount} from your account!')
    balance_display.text(f'Your current bank balance is: £{st.session_state.balance}')
