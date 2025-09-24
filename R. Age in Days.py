n = int(input())

years = n//365 
print(years,"years")

days_left = n - (years*365)

months = days_left//30 

print(months,"months")

days_left_2 = days_left - (months*30)

print(days_left_2,"days")