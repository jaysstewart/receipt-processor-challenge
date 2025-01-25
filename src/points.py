from model.item import Item
from model.receipt import Receipt


class Points:
    def calculatePoints(self, receipt):
        points = 0
        points += self.alphanumericCharactersRule(receipt)
        points += self.roundDollarRule(receipt)
        points += self.multipleOfPointTwentyFiveRule(receipt)
        points += self.twoItemsRule(receipt)
        points += self.trimmedItemDescriptionRule(receipt)
        points += self.oddPurchaseDateRule(receipt)
        points += self.timeOfPurchaseRule(receipt)
        return points

    def alphanumericCharactersRule(self, receipt):
        # One point for every alphanumeric character in the retailer name
        points = 0
        for i in receipt.retailer:
            if i.isalnum():
                points += 1
        return points

    def roundDollarRule(self, receipt):
        points = 0
        # 50 points if the total is a round dollar amount with no cents.
        if receipt.total.isInteger():
            points += 50

    def multipleOfPointTwentyFiveRule(self, receipt):
        # 25 points if the total is a multiple of 0.25
        pass

    def twoItemsRule(self, receipt):
        # 5 points for every two items on the receipt.
        pass

    def trimmedItemDescriptionRule(self, receipt):
        # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to
        # the nearest integer. The result is the number of points earned.
        pass

    def oddPurchaseDateRule(self, receipt):
        # 6 points if the day in the purchase date is odd.
        pass

    def timeOfPurchaseRule(self, receipt):
        # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
        pass
