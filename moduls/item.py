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
        for index, item in enumerate(cls.list_of_Items):
            print(f"{index}  {item.item_name}  {item.size}    {item.stock}")



    @classmethod
    def change_stock(cls, item_index):
        try:
            cls.item_index = int(item_index)
            item = cls.list_of_Items[cls.item_index]
            item_stock_change = input("Zadejte nový stock: ")
            item.stock = item_stock_change
        except IndexError:
            print(f"Item with index {item_index} does not exist!")
