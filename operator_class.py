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
        self.customers = []   # список клієнтів цього оператора

    def addCustomer(self, customer) -> None:
        """Додати клієнта до списку цього оператора"""
        self.customers.append(customer)

    # --- окремі функції для знижок ---
    def getDiscountForTalking(self, customer) -> float:
        if customer.age < 18 or customer.age > 65:
            return 1 - self.discountRate / 100.0
        return 1.0

    def getDiscountForMessage(self, customer, other) -> float:
        if customer.operator.ID == other.operator.ID:
            return 1 - self.discountRate / 100.0
        return 1.0
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
