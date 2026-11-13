from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total:float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.__percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_amount: float):
        self.__threshold = threshold
        self.__discount_amount = discount_amount

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return total - self.__discount_amount
        return total

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.95