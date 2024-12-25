class User:
    USER_TYPE = ["HR", "Buyer"]

    def __init__(self, first_name, last_name, user_type):
        self.first_name = first_name
        self.last_name = last_name
        if user_type in User.USER_TYPE:
            self.user_type = user_type
        else:
            raise ValueError(f"Špatný typ usera! {user_type}. Povolené typy jsou pouze: {', '.join(User.USER_TYPE)}")