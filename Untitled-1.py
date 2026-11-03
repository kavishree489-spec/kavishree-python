def subsidy(units, ration, age):

    if units <= 100:
        return "Full subsidy"

    elif units <= 200:
        if ration:
            return "Partial subsidy"
        else:
            return "No subsidy"

    else:
        if age > 80:
            return "Special subsidy"
        else:
            return "No subsidy"


print(subsidy(100, False, 50))
print(subsidy(150, True, 40))
print(subsidy(250, False, 85))