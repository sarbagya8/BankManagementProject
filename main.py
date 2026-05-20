import json
import random
import string
from pathlib import Path


class Bank:

    database = "data.json"

    @classmethod
    def load_data(cls):

        if Path(cls.database).exists():

            with open(cls.database, "r") as fs:
                return json.load(fs)

        return []

    @classmethod
    def save_data(cls, data):

        with open(cls.database, "w") as fs:
            json.dump(data, fs, indent=4)

    @classmethod
    def generate_account_number(cls):

        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=5)

        account_no = alpha + num

        random.shuffle(account_no)

        return "".join(account_no)

    @classmethod
    def create_account(cls, name, age, email, pin):

        data = cls.load_data()

        if age < 18:
            return False, "You must be at least 18 years old"

        if len(str(pin)) != 4:
            return False, "PIN must contain exactly 4 digits"

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": cls.generate_account_number(),
            "balance": 0
        }

        data.append(account)

        cls.save_data(data)

        return True, account

    @classmethod
    def find_user(cls, account_no, pin):

        data = cls.load_data()

        for user in data:

            if user["account_no"] == account_no and user["pin"] == pin:
                return user

        return None

    @classmethod
    def deposit(cls, account_no, pin, amount):

        data = cls.load_data()

        for user in data:

            if user["account_no"] == account_no and user["pin"] == pin:

                if amount <= 0:
                    return False, "Enter a valid amount"

                user["balance"] += amount

                cls.save_data(data)

                return True, user

        return False, "Invalid account details"

    @classmethod
    def withdraw(cls, account_no, pin, amount):

        data = cls.load_data()

        for user in data:

            if user["account_no"] == account_no and user["pin"] == pin:

                if amount > user["balance"]:
                    return False, "Insufficient balance"

                user["balance"] -= amount

                cls.save_data(data)

                return True, user

        return False, "Invalid account details"

    @classmethod
    def show_details(cls, account_no, pin):

        user = cls.find_user(account_no, pin)

        if user:
            return True, user

        return False, "Account not found"

    @classmethod
    def update_details(cls, account_no, pin, name, email, new_pin):

        data = cls.load_data()

        for user in data:

            if user["account_no"] == account_no and user["pin"] == pin:

                if name:
                    user["name"] = name

                if email:
                    user["email"] = email

                if new_pin:

                    if len(str(new_pin)) != 4:
                        return False, "PIN must contain 4 digits"

                    user["pin"] = new_pin

                cls.save_data(data)

                return True, user

        return False, "Invalid account details"

    @classmethod
    def delete_account(cls, account_no, pin):

        data = cls.load_data()

        for user in data:

            if user["account_no"] == account_no and user["pin"] == pin:

                data.remove(user)

                cls.save_data(data)

                return True, "Account deleted successfully"

        return False, "Invalid account details"