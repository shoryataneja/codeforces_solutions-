disc , price = map(int,input().split())

orig_price = price / (1-(disc/100)) 
# print(f"{orig_price:.2f}")  
print(f"{orig_price:.2f}")
