def solution(price, money, count):
    tot_price = 0
    for i in range(1, count+1):
        tot_price += (i * price)
    if money < tot_price:
        return tot_price - money
    else:
        return 0