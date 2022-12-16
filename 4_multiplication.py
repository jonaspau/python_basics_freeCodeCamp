# Times table:

def time_table():
    while True:
        try:
            x = int(input("Please enter a number: "))
            for row in range(x+1):
                for col in range(x+1):
                    print(f"{row*col:4}", end = " ")
                print()
        except ValueError:
            print("Not a number")
        q = input("Continue?(y/n): ").lower()
        if q[0] == "n":
            break
time_table()