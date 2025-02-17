from .item import Item

class Operator(Item):
    list_of_operators = []

    def __init__(self,first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.assigned_items = []
        self.add_operator()

    def add_operator(self):
        self.list_of_operators.append(self)

    @classmethod
    def create_operator(cls, first_name, last_name, date_of_birth):
        new_operator = cls(first_name, last_name, date_of_birth)

    @classmethod
    def edit_operator(cls, operator_index):
        try:
            cls.operator_index = int(operator_index)
            operator = cls.list_of_operators[cls.operator_index]
            first_name_change = input("Name: ")
            operator.first_name = first_name_change
            last_name_change = input("Last name: ")
            operator.last_name = last_name_change
            date_of_birth_change = input("Date of birth: ")
            operator.date_of_birth = date_of_birth_change
        except IndexError:
            print(f"Operator with index {operator_index} does not exists!")

    @classmethod
    def assign_item(cls, operator_index, item_index, quantity):

        try:
            cls.operator_index = int(operator_index)
            operator = cls.list_of_operators[cls.operator_index]
            cls.item_index = int(item_index)
            item = cls.list_of_Items[cls.item_index]


            if quantity > item.stock:
                print(f"Nedostatek zásob! Dostupné množství je: {item.stock}")
                return

            operator.assigned_items.append((item.item_name, item.size, quantity))
            item.stock -= quantity

            print(f"Položka {item.item_name} byla přidělena operátorovi {operator.first_name} {operator.last_name}")

        except IndexError:
            print("Invalid operator or item index")

    @classmethod
    def view_list_of_operators(cls):
        print("ID    Name    Date of Birth   Assigned items")
        for index, operator in enumerate(cls.list_of_operators):
            print(f"{cls.list_of_operators.index(operator)} "
                  f"{operator.first_name} "
                  f"{operator.last_name} "
                  f"{operator.date_of_birth}  "
                  f"{operator.assigned_items}")