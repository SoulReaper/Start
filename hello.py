years = 1
value_start = 1
value_end = 3.73112934
compounding_periods = 365
rate = (pow(value_end / value_start, 1 / (years * compounding_periods)) - 1) * compounding_periods
print("Yearly rate: " + str(rate * 100) + "%")

value_start = 1
years = 1
value_end = value_start * pow((1 + (rate / compounding_periods)), compounding_periods * years)
print("Future Value: " + str(value_end))
growth_rate = (value_end - value_start) / value_start
print("Growth Rate:" + str(growth_rate * 100) + "%")
