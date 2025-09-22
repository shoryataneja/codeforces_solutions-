t = int(input())

for _ in range(t):
    n = int(input())
    row1 = input()
    row2 = input()
    
    converted_row1 = ""
    for i in row1:
        if i == "R":
            converted_row1 += "R"
        else: 
            converted_row1 += "X"

    converted_row2 = ""
    for i in row2:
        if i == "R":
            converted_row2 += "R"
        else: 
            converted_row2 += "X"


    if converted_row1 == converted_row2:
        print("yes")
    else:
        print("no")
    