lst = list(map(int,input().split()))
my_set = set(lst)
new_lst = []
for num in my_set:
    new_lst.append(lst.count(num))
 
print(4 - len(my_set))