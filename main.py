from moduls.user import User
from moduls.item import Item
from moduls.operator import Operator


operator_Pavel = Operator("Pavel", "Novák", "2000-12-19")
operator_Jiri = Operator("Jiri", "Bubák", "1990-12-9")

danielaHR = User("Daniela", "Testova", "HR", "HR", "123")
lukasNakup = User("Lukáš", "Novák", "Buyer", "Buy", "456")

mikina = Item("Mikina", "L", 10)
tricko = Item("Tričko", "XL", 20)



if __name__ == "__main__":

    # login check

    login = input("Zadej login: ")
    heslo = input("Zadej heslo: ")

    current_user = User.user_check(login=login, password=heslo)

    if current_user:
        print(current_user.user_type)

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
                    if current_user.user_type == "HR":
                        op_id = input("Jakého operátora chcete změnit?")
                        Operator.edit_operator(operator_index=op_id)
                    else:
                        print("You have no permission to change the operator!")
                case "d":
                    if current_user.user_type == "Buyer":
                        item_id = input("Jaký item chcete změnit?")
                        Item.change_stock(item_index=item_id)
                    else:
                        print("You have no permission to change the stock!")
                case "e":
                    if current_user.user_type == "Buyer":
                        item_name = input("Item name: ")
                        item_size = input("Item size: ")
                        item_stock = input("Item stock: ")
                        Item.create_item(item_name=item_name,size=item_size, stock=item_stock)
                    else:
                        print("You have no permission to create item!")
                case "f":
                    if current_user.user_type == "HR":
                        op_name = input("Jmeno: ")
                        op_lastN = input("Prijmeni: ")
                        op_date = input("Datum narození: ")
                        Operator.create_operator(first_name=op_name, last_name=op_lastN, date_of_birth=op_date)
                    else:
                        print("You have no permission to create operator!")
                case "g":
                    if current_user.user_type == "HR":
                        op_id = input("ID operátora: ")
                        item_id = input("ID itemu: ")
                        quantity = int(input("Počet kusů: "))
                        Operator.assign_item(operator_index=op_id, item_index=item_id, quantity=quantity)
                    else:
                        print("You have no permission to assign items to operator!")
                case "k":
                    break
                case _:
                    print("Špatná volba!")
    else:
        print("Invalid login or password!")