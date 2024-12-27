import hashlib

class User:
    USER_TYPE = ["HR", "Buyer"]
    user_list = []

    def __init__(self, first_name, last_name, user_type, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = self.hash_password(password)

        if user_type in User.USER_TYPE:
            self.user_type = user_type
        else:
            raise ValueError(f"Špatný typ usera! {user_type}. Povolené typy jsou pouze: {', '.join(User.USER_TYPE)}")

        self.add_user()

    def add_user(self):
        for user in User.user_list:
            if user.login == self.login:
                raise ValueError(f"User with login {self.login} already exists!")
        User.user_list.append(self)


    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def user_check(cls, login, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in cls.user_list:
            if user.login == login and user.password == hashed_password:
                return user
        return None

"""
HR - může vytvářet, editovat, mazat, zobrazovat operatory + zobrazovat items
Buyer - může vytvářet, editovat, mazat, zobrazovat item + zobrazovat Operatory
"""
class PermissionManager:
    def __init__(self, user):
        self.user = user

    def can_change_operator(self):
        return self.user.user_type == "HR"

    def can_change_stock(self):
        return self.user.user_type == "Buyer"

    def can_create_item(self):
        return self.user.user_type == "Buyer"

    def can_create_operator(self):
        return self.user.user_type == "HR"

    def can_assign_item(self):
        return self.user.user_type == "HR"