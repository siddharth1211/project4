class emp:
    def __init__(self, x):
        self.x = x

    def __float__(self):
        print("called1")
        return round(self.x, 2)

    # def __str__(self):
    #    self.x = super(emp, self).__call__(self)
    #    return self.x

        # @classmethod
    # def __str__(cls):
    #     print("called2")
    #     cls.x = super(emp, cls).__float__(cls)
    #     return type(cls.x)

i = emp(7.00)
print(float(i))
