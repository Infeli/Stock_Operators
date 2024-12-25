class Item:
    list_of_Items = []

    def __init__(self, item_name, size, stock):
        self.item_name = item_name
        self.size = size
        self.stock = stock

        self.add_item_to_list()

    def add_item_to_list(self):
        self.list_of_Items.append(self)

    @classmethod
    def create_item(cls, item_name, size, stock):
        new_item = cls(item_name, size, stock)


    @classmethod
    def view_stock(cls):
        print("ID  Name  Size  Stock")
        for item in cls.list_of_Items:
            print(f"{cls.list_of_Items.index(item)}  {item.item_name}  {item.size}    {item.stock}")


    @classmethod
    def change_stock(cls, item_index):
        cls.item_index = int(item_index)
        item = cls.list_of_Items[cls.item_index]
        item_stock_change = input("Zadejte nový stock: ")
        item.stock = item_stock_change


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
        cls.operator_index = int(operator_index)

        print(operator_index)

        operator = cls.list_of_operators[cls.operator_index]

        print(cls.list_of_operators.index(operator))
        first_name_change = input("Name: ")
        operator.first_name = first_name_change

        last_name_change = input("Last name: ")
        operator.last_name = last_name_change

        date_of_birth_change = input("Date of birth: ")
        operator.date_of_birth = date_of_birth_change

    @classmethod
    def assign_item(cls, operator_index, item_index, quantity):

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


    @classmethod
    def view_list_of_operators(cls):
        print("ID    Name    Date of Birth")
        for operator in cls.list_of_operators:
            print(f"{cls.list_of_operators.index(operator)} {operator.first_name} {operator.last_name} {operator.date_of_birth}")



class User:
    USER_TYPE = ["HR", "Buyer"]

    def __init__(self, first_name, last_name, user_type):
        self.first_name = first_name
        self.last_name = last_name
        if user_type in User.USER_TYPE:
            self.user_type = user_type
        else:
            raise ValueError(f"Špatný typ usera! {user_type}. Povolené typy jsou pouze: {', '.join(User.USER_TYPE)}")



operator_Pavel = Operator("Pavel", "Novák", "2000-12-19")
operator_Jiri = Operator("Jiri", "Bubák", "1990-12-9")

danielaHR = User("Daniela", "Testova", "HR")
lukasNakup = User("Lukáš", "Novák", "Buyer")

mikina = Item("Mikina", "L", 10)
tricko = Item("Tričko", "XL", 20)


if __name__ == "__main__":
    while True:
        user_choice = input("----------------------------------\n"
                            "Vyberte možnost:\n"
                            "a - zobrazit stock\n"
                            "b - zobrazit seznam operatoru\n"
                            "c - zmenit operatora\n"
                            "d - změnit stock\n"
                            "e - vytvořit item\n"
                            "f - vytvořit operátora\n"
                            "g - přiřaď item k operátorovi\n"
                            "k - Konec\n------------------------\n")
        user_choice.strip().lower()

        match user_choice:
            case "a":
                Item.view_stock()
            case "b":
                Operator.view_list_of_operators()
            case "c":
                op_id = input("Jakého operátora chcete změnit?")
                Operator.edit_operator(operator_index=op_id)
            case "d":
                item_id = input("Jaký item chcete změnit?")
                Item.change_stock(item_index=item_id)
            case "e":
                item_name = input("Item name: ")
                item_size = input("Item size: ")
                item_stock = input("Item stock: ")
                Item.create_item(item_name=item_name,size=item_size, stock=item_stock)
            case "f":
                op_name = input("Jmeno: ")
                op_lastN = input("Prijmeni: ")
                op_date = input("Datum narození: ")
                Operator.create_operator(first_name=op_name, last_name=op_lastN, date_of_birth=op_date)
            case "g":
                op_id = input("ID operátora: ")
                item_id = input("ID itemu: ")
                quantity = int(input("Počet kusů: "))
                Operator.assign_item(operator_index=op_id, item_index=item_id, quantity=quantity)
            case "k":
                break
            case _:
                print("Špatná volba!")
