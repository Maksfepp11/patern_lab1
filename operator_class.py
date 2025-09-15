from bill import Bill

class Operator:
    """описує оператора мобільного зв’язку і всі його характеристики та тарифи."""
# init - ініціалізація обєкта класу
    def __init__(self, ID: int, talkingCharge: float, messageCost: float,
                 networkCharge: float, discountRate: int) -> None:
        self.ID = ID 
        self.talkingCharge = talkingCharge 
        self.messageCost = messageCost 
        self.networkCharge = networkCharge 
        self.discountRate = discountRate 

    # Cost calculations
    def calculateTalkingCost(self, minute: int, customer) -> float:
        cost = minute * self.talkingCharge
        if customer.age < 18 or customer.age > 65:
            cost *= (1 - self.discountRate / 100)
        return cost

    def calculateMessageCost(self, quantity: int, customer, other) -> float:
        cost = quantity * self.messageCost
        if customer.operator.ID == other.operator.ID:  # однакові операори
            cost *= (1 - self.discountRate / 100)
        return cost

    def calculateNetworkCost(self, amount: float) -> float:
        return amount * self.networkCharge

    # Getters / setters - присвоєння атриуту нове значення
    def getTalkingCharge(self) -> float:
        return self.talkingCharge

    def setTalkingCharge(self, value: float) -> None:
        self.talkingCharge = value

    def getMessageCost(self) -> float:
        return self.messageCost

    def setMessageCost(self, value: float) -> None:
        self.messageCost = value

    def getNetworkCharge(self) -> float:
        return self.networkCharge

    def setNetworkCharge(self, value: float) -> None:
        self.networkCharge = value

    def getDiscountRate(self) -> int:
        return self.discountRate

    def setDiscountRate(self, value: int) -> None:
        self.discountRate = value
