#!/usr/bin/env python
# coding: utf-8

# In[1]:


#торговый автомат
class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:

    def __init__(self):

        self.items = [
            Item("чай", 0.50),
            Item("кофе", 1.00),
            Item("пирожок", 1.50),
            Item("натуральный сок", 2.00)
        ]

        self.money_inserted = 0.00

    def display_items(self):
        for code, item in enumerate(self.items, start=1):
            print(f"[{code}] - {item.name} (${item.price:.2f})")

    def insert_money(self, money):
        if money <= 0.00:
            raise ValueError
        self.money_inserted += money

def main():

    vending_machine = VendingMachine()
    vending_machine.display_items()

    while True:
        try:
            user_selection = int(input("введите код продукта: "))
        except ValueError:
            continue
        if user_selection in range(1, len(vending_machine.items)+1):
            break
    item = vending_machine.items[user_selection-1]
    print(f"вы выбрали \"{item.name}\" - цена за него составляет ${item.price:.2f}")
    while vending_machine.money_inserted < item.price:
        print(f"вы внесли ${vending_machine.money_inserted:.2f} ")
        while True:
            try:
                money_to_insert = float(input("пожалуйста внесите деньги "))
                vending_machine.insert_money(money_to_insert)
            except ValueError:
                continue
            else:
                break
    print(f"Спасибо! Возьмите ваш \"{item.name}\".")
    print(f"ваша сдача ${vending_machine.money_inserted - item.price:.2f}.")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())


# In[2]:





# In[ ]:




