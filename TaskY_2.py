class TriangCheck:
    def __init__(self, sides):
        self.sides = sides
    def is_triang(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами не выйдет!'
        return 'Нужно вводить только числа!'

(a, b, c) = (float(x) for x in input().split())
y = [a, b, c]
test = TriangCheck(y)
print(test.is_triang())