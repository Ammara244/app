import streamlit as st

st.title('Bank Balance Simulation')

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
    value=st.session_state.balance, # something about setting a value so the input box always shows your balance
    step=1 # i think this lets the pick a number by pressing the up/down
)
st.session_state.balance = initial_balance

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
