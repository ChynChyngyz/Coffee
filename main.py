class CofffeType:
    def __init__(self, name, coffee, water, milk=0):
        self.name = name
        self.coffee = coffee
        self.water = water
        self.milk = milk


class CoffeeTypes:
    def __init__(self):
        self.espresso = CofffeType('Espresso', 100, 200)
        self.americano = CofffeType('Americano', 100, 500)
        self.latte = CofffeType('Latte', 100, 400, 100)
        self.coffee_types = [self.espresso, self.americano, self.latte]

    def add_coffe_type(self):
        name = input('Enter coffee name: ')
        coffee = int(input('Enter coffee amount needed: '))
        water = int(input('Enter water amount needed: '))
        milk = int(input('Enter milk amount needed: '))
        self.coffee_types.append(CofffeType(name, coffee, water, milk))

    def remove_coffee_type(self):
        print('Choose coffee number')
        for i, v in enumerate(self.coffee_types):
            print(f'{i + 1} : {v.name}')
        choose = int(input('>>> '))
        index = choose - 1
        self.coffee_types.pop(index)


class Stock:
    def __init__(self, coffee, water, milk):
        self.coffee = coffee
        self.water = water
        self.milk = milk

    def update_stock(self, coffee: CofffeType):
        if (self.coffee - coffee.coffee < 0 or self.water - coffee.water < 0
                or self.milk - coffee.milk < 0):
            print('Not enough resources')
            print(f'Coffee: {self.coffee} \n'
                  f'Water: {self.water} \n'
                  f'Wilk: {self.milk} \n')
            return
        self.coffee -= coffee.coffee
        self.water -= coffee.water
        self.milk -= coffee.milk

    def __str__(self):
        return (f'Amount of resources \n'
                f'Coffee: {self.coffee} \n'
                f'Water: {self.water} \n'
                f'Milk: {self.milk} \n')


class CoffeeMachine:
    def __init__(self):
        self.stock = Stock(1000, 5000, 300)
        self.coffees = CoffeeTypes()
        self.password = '1234'

    def supply_center(self):
        coffee = int(input('Enter amount of coffee: '))
        water = int(input('Enter amount of water: '))
        milk = int(input('Enter amount of milk: '))
        self.stock.coffee += coffee
        self.stock.water += water
        self.stock.milk += milk
        print(self.stock)

    def coffee_center(self):
        picked_coffee = self.coffee_picker()
        self.stock.update_stock(picked_coffee)
        if self.is_continue():
            return self.coffee_center()

    @staticmethod
    def is_continue():
        return True if input('Do you want to make coffee again?(y/n): ') == 'y' else False

    def coffee_picker(self):
        coffee_name_list = []
        print('Choose coffee number')
        for i, v in enumerate(self.coffees.coffee_types):
            coffee_name_list.append(v)
            print(f'{i + 1} : {v.name}')
        choose = int(input('===> '))
        index = choose - 1
        chosen_coffee = self.coffees.coffee_types[index]
        return chosen_coffee

    def password_check(self):
        counter = 0
        while True:
            if counter == 3:
                inpu = input('Do you want to continue(y/n): ')
                if inpu == 'y':
                    counter = 0
                    continue
                else:
                    return
            inp = input('Write password: ')
            if inp != self.password:
                print('Incorrect password')
                counter += 1
            else:
                return True

    def admin(self):
        action = input('Enter number for: \n'
                       '1 - Add supply resources \n'
                       '2 - Add new coffee type \n'
                       '3 - Remove coffee: \n'
                       '========> ')
        if action == '1':
            self.supply_center()
        elif action == '2':
            self.coffees.add_coffe_type()
        elif action == '3':
            self.coffees.remove_coffee_type()

    def run(self):
        print('Welcome!\n'
              '========')
        while True:
            prompt = input('Enter number for:\n'
                           '1 - Admin\n'
                           '2 - Make coffee\n'
                           '3 - Stop machine\n'
                           '4 - Supply\n'
                           '========> ')
            if prompt == '1':
                if self.password_check():
                    self.admin()
            elif prompt == '4':
                print(self.stock)
            elif prompt == '2':
                self.coffee_center()
            else:
                break


def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.run()


if __name__ == '__main__':
    main()
