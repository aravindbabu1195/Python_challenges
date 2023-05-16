# function defining..
def function1(x,y):
    try:

        return (x/y)
    except:
        print("Error :dividing by zero")
        print()
    finally:
        print("Program completed")

# function calling..
print(function1(int(input("Enter Two numbers :")),
    int(input())))
