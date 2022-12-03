class Soda:
    def __init__(self, ingr):
        if isinstance(ingr, str):
            self.ingr = ingr
        else:
            self.ingr = None
    def show_my_drink(self):
        if self.ingr:
            print(f'Газировка и {self.ingr}')
        else:
            print('Обычная газировка')

test = Soda(input())
test.show_my_drink()