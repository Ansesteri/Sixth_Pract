class KgToPounds():
    def __init__(self, kg = 10):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
    
    #Не могу проверить работу этих частей кода, вылазить ошибка: 'int' object is not callable (или float там смотря какие значения ввести)
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self, n_kg):
        if isinstance(n_kg, (int, float)):
            self.__kg = n_kg
        else:
            raise ValueError('Вводить только числа!')

a = float(input())
test = KgToPounds(a)
print(test.to_pounds())
#test.kg(2) - ошибка