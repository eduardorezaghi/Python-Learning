class IceCream(object):
    def __init__(self, flavor, numScoops, costPerScoop, remaining_icecream):
        self.flavor = flavor
        self.numScoops = numScoops
        self.costPerScoop = costPerScoop
        self.remaining_icecream = remaining_icecream

    def scoop(self):
                #shows the amount of ice cream remaining after an order is scooped
        #scoops icecream and decreases the number of scoops left
        self.remaining_icecream -= self.numScoops
        return self.remaining_icecream

    def total_cost(self):
        #vanilla ice cream is sold at a discount of half off!
        if self.flavor == "vanilla":
            total_cost = self.numScoops * .5*self.costPerScoop

        else:
            total_cost = self.numScoops * self.costPerScoop

        return total_cost

cream = IceCream("chocolate",4,1,6)
print(f"{cream.flavor.title()} icecream number of scoops is: {cream.remaining_icecream}!\n")
print(f"After using {cream.numScoops} scoops for a customer, it is: {cream.scoop()}")
