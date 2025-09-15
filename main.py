from customer import Customer
from operator_class import Operator
from bill import Bill

def main():
    customers = []
    operators = []
    bills = []

    op1 = Operator(0, talkingCharge=1.0, messageCost=0.5, networkCharge=0.1, discountRate=20)
    op2 = Operator(1, talkingCharge=0.6, messageCost=0.5, networkCharge=0.3, discountRate=15)
    operators.extend([op1, op2])

    b1 = Bill(200)
    b2 = Bill(300)
    bills.extend([b1, b2])

    c1 = Customer(0, "Maks", 17, op1, b1, 200)
    c2 = Customer(1, "Anna", 30, op2, b2, 300)
    customers.extend([c1, c2])

    c1.talk(10, c2)
    c1.message(5, c2)
    c2.connection(50)

    print(f"{c1.name} bill: {c1.getBill()}")
    print(f"{c2.name} bill: {c2.getBill()}")

if __name__ == "__main__":
    main()
