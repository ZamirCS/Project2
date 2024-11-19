
class items:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def __str__(self):
        return f"{self.name} ${self.cost:.2f}"
class vending_machine:
    def showItems(self):
        print("\nAll Items Avaliable")
        for i, items in enumerate(self.items, start=1):
            print(f"{i}. {items}")
    def __init__(self):
        self.items = [
            items("Pepsi", 1.20),
            items("Sprite", 2.00),
            items("Dr.paper",2.00),
            items("Ginger ale",1.50),
            items("Snapple",1.25),
            items("Gatorade",1.75)
        ]
    def run(self):
        while True:
            self.showItems()
            selection = int(input("Select an Item (1-6)\n"))
            if selection < 1 or selection > len(self.items):
                print("Error, choose a valid item")
                continue
            money = float(input(f"Insert money for {self.items[selection-1].name}: $"))
            self.dispenseItem(selection,money)
    def dispenseItem(self,selection, money):
        item = self.items[selection - 1]
        if money < item.cost:
            print(f"Error, insuficient money {item.name} cost ${item.cost:.2f}. add the correct amount")
        else:
            change = money - item.cost
            print(f"Dispensing {item.name}")
            if change > 0:
                print(f"Your change is ${change:.2f}.")



def main():
    VendingMachine = vending_machine()
    VendingMachine.run()

main()
