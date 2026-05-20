import streamlit as st
from main import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Update Account",
        "Delete Account"
    ]
)

if menu == "Create Account":

    st.subheader("Create New Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1, step=1)
    email = st.text_input("Email Address")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):

        if not pin.isdigit():

            st.error("PIN must contain only numbers")

        else:

            status, result = Bank.create_account(
                name,
                age,
                email,
                int(pin)
            )

            if status:

                st.success("Account Created Successfully")

                st.info(
                    f"Your Account Number: {result['account_no']}"
                )

            else:
                st.error(result)

elif menu == "Deposit":

    st.subheader("Deposit Money")

    account_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit Money"):

        status, result = Bank.deposit(
            account_no,
            int(pin),
            amount
        )

        if status:

            st.success("Money Deposited Successfully")

            st.write(
                f"Updated Balance: Rs. {result['balance']}"
            )

        else:
            st.error(result)

elif menu == "Withdraw":

    st.subheader("Withdraw Money")

    account_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw Money"):

        status, result = Bank.withdraw(
            account_no,
            int(pin),
            amount
        )

        if status:

            st.success("Withdrawal Successful")

            st.write(
                f"Remaining Balance: Rs. {result['balance']}"
            )

        else:
            st.error(result)

elif menu == "Show Details":

    st.subheader("Account Details")

    account_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):

        status, result = Bank.show_details(
            account_no,
            int(pin)
        )

        if status:

            st.success("Account Found")

            st.write(f"Name: {result['name']}")
            st.write(f"Age: {result['age']}")
            st.write(f"Email: {result['email']}")
            st.write(f"Account Number: {result['account_no']}")
            st.write(f"Balance: Rs. {result['balance']}")

        else:
            st.error(result)

elif menu == "Update Account":

    st.subheader("Update Account")

    account_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN", type="password")

    if st.button("Update Details"):

        updated_pin = int(new_pin) if new_pin else None

        status, result = Bank.update_details(
            account_no,
            int(pin),
            new_name,
            new_email,
            updated_pin
        )

        if status:

            st.success("Details Updated Successfully")

        else:
            st.error(result)

elif menu == "Delete Account":

    st.subheader("Delete Account")

    account_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):

        status, result = Bank.delete_account(
            account_no,
            int(pin)
        )

        if status:

            st.success(result)

        else:
            st.error(result)