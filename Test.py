class Convert1:         # Class for converting USD
    def get_value(self):
        return 3.52

    def calculate(self, user_input):
        return user_input * self.get_value()


class Convert2:         # Class for converting ILS
    def get_value2(self):
        return 0.28

    def calculate2(self, user_input2):
        return (user_input2 * self.get_value2())


print("Welcome to currency converter, Please choose an option (1/2): 1. Dollars to Shekels 2. Shekels to Dollars")
x = input()

print("Please enter an amount to convert")
y = float(input())


def user_value():   # get the value of USD amount to convert, from the user
    if x == 1:
        USDc = Convert1()
        print(USDc.calculate(y))

    else:
        ILSc = Convert2()
        print(ILSc.calculate2(k))


print(user_value())


def main():
    print(user_value())

main()

print(2)