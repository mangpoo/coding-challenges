input_year = int(input())

if(input_year % 400 == 0 or input_year % 100 != 0):
    if(input_year % 4 == 0):
        print("1")
    else:
        print("0")
else:
    print("0")