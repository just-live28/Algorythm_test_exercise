def bnp(money, chart):
    stock = 0
    for price in chart:
        if price <= money:
            get = money // price
            stock += get
            money -= get * price
    
    return chart[-1] * stock + money

def timing(money, prev, chart):
    stock = 0
    increase = 0
    decrease = 0
    for price in chart:
        if price < prev:
            decrease += 1
            increase = 0
        elif price > prev:
            increase += 1
            decrease = 0
        else:
            increase = 0
            decrease = 0
        prev = price
        
        if decrease >= 3 and price <= money:
            get = money // price
            stock += get
            money -= get * price
        
        if increase == 3:
            money += stock * price
            stock = 0
        
    return chart[-1] * stock + money

money = int(input())
chart = list(map(int, input().split()))

bnp_result = bnp(money, chart)
timing_result = timing(money, chart[0], chart[1:])

if bnp_result > timing_result:
    print('BNP')
elif timing_result > bnp_result:
    print('TIMING')
else:
    print('SAMESAME')