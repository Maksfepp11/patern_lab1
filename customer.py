from bill import Bill
from operator_class import Operator

class Customer:
    """Holds customer details"""

    def __init__(self, ID: int, name: str, age: int,
                 operator: Operator, bill: Bill, limitingAmount: float) -> None:
        self.ID = ID
        self.name = name
        self.age = age
        self.operator = operator
        self.bill = bill
        # змінює початковий ліміт рахунку клієнта.
        self.bill.changeTheLimit(limitingAmount)
        # додаємо клієнта в список оператора
        operator.addCustomer(self)

    def talk(self, minute: int, other: "Customer") -> None:
        cost = self.operator.calculateTalkingCost(minute, self)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} talked with {other.name} for {minute} minutes. Cost={cost}")
        else:
            print(" Talk failed: limit exceeded")

    def message(self, quantity: int, other: "Customer") -> None:
        cost = self.operator.calculateMessageCost(quantity, self, other)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} sent {quantity} messages to {other.name}. Cost={cost}")
        else:
            print(" Message failed: limit exceeded")

    def connection(self, amount: float) -> None:
        cost = self.operator.calculateNetworkCost(amount)
        if self.bill.check(cost):
            self.bill.add(cost)
        else:
            print("Connection failed: limit exceeded")

        def pay(self, amount: float) -> None:
            self.bill.pay(amount)
            print(f"{self.name} paid {amount}. Current debt={self.bill.getCurrentDebt()}")

    def changeOperator(self, new_operator: Operator) -> None:
        self.operator = new_operator
        new_operator.addCustomer(self)
        print(f"{self.name} changed operator to {new_operator.ID}")

    def changeBillLimit(self, amount: float) -> None:
        self.bill.changeTheLimit(amount)
        print(f"{self.name} changed bill limit to {amount}")

    # Getters/setters
    def getAge(self) -> int:
        return self.age

    def setAge(self, age: int) -> None:
        self.age = age

    def getOperator(self) -> Operator:
        return self.operator

    def setOperator(self, operator: Operator) -> None:
        self.operator = operator

    def getBill(self) -> Bill:
        return self.bill

    def setBill(self, bill: Bill) -> None:
        self.bill = bill
