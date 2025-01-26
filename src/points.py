import math
from datetime import datetime

class Points:


    def __init__(self):
        self.memory = {}

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
        # 50 points if the total is a round dollar amount with no cents.
        points = 0
        if float(receipt.total).is_integer():
            points += 50
        return points

    def multipleOfPointTwentyFiveRule(self, receipt):
        # 25 points if the total is a multiple of 0.25
        points = 0
        if float(receipt.total) % 0.25 == 0:
            points += 25
        return points

    def twoItemsRule(self, receipt):
        # 5 points for every two items on the receipt.
        points = (len(receipt.items) // 2) * 5
        return points

    def trimmedItemDescriptionRule(self, receipt):
        # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to
        # the nearest integer. The result is the number of points earned.
        points = 0
        for item in receipt.items:
            if len(item.shortDescription.strip()) % 3 == 0:
                points += math.ceil(float(item.price) * 0.2)
        return points

    def oddPurchaseDateRule(self, receipt):
        # 6 points if the day in the purchase date is odd.
        points = 0
        date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
        if date.day % 2 == 1:
            points += 6
        return points

    def timeOfPurchaseRule(self, receipt):
        # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
        points = 0
        time = datetime.strptime(receipt.purchaseTime, "%H:%M").time()
        if 14 <= time.hour < 16:
            points += 10
        return points
