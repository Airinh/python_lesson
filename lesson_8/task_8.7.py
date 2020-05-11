class Complex:
    def __init__(self, x, y):
        self.comp_dict = {"a": x, "b": y}

    def __str__(self):
        if self.comp_dict.get("a") == 0:
            return f'({self.comp_dict.get("b")}j)'
        else:
            if self.comp_dict.get("b") >= 0:
                return f'({self.comp_dict.get("a")}+{self.comp_dict.get("b")}j)'
            else:
                return f'({self.comp_dict.get("a")}{self.comp_dict.get("b")}j)'


    def __add__(self, other):
        return Complex(self.comp_dict.get("a") + other.comp_dict.get("a"),
                       self.comp_dict.get("b") + other.comp_dict.get("b"))

    def __mul__(self, other):
        x = self.comp_dict.get("a") * other.comp_dict.get("a") - self.comp_dict.get("b") * other.comp_dict.get("b")
        y = self.comp_dict.get("a") * other.comp_dict.get("b") + self.comp_dict.get("b") * other.comp_dict.get("a")
        return Complex(x, y)


c1 = Complex(3, -2)
c2 = Complex(3, 2)
c3 = c1 * c2
print(c3)

