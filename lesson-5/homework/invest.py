def invest(amount,rate,years):
    for i in range(years):
        amount = amount + amount*rate/100
        print(f"year {i+1}: {amount:.2f}")
invest(100,5,5)
