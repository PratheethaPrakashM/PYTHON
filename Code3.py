prices = [250, 300, 200, 400, 500, 450, 350]
min_price=prices[0]
max_profit=0
for price in prices[1:] :
       profit=price - min_price
       min_price=min(min_price,price)
       max_profit=max(max_profit,profit)
print("maximum profit:",max_profit)
      

prices = [250, 300, 200, 400, 500, 450, 350]   
min_price=prices[0]
max_profit=0
for price in prices[1:]:
        if price<min_price:
            min_price=price
        profit=price-min_price
        if profit>max_profit:
            max_profit=profit
print(profit(prices))


prices = [250, 300, 200, 400, 500, 450, 350]   
max_profit=0
for i in range(len(prices)-1):
     for j in range(i+1,len(prices)):
          profit=prices[j]-prices[i]
          if profit>max_profit:
               max_profit=profit
print("maximum profit:",max_profit)               

    
    