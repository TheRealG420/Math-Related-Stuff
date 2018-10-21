# --- Fibonacci Sequence --- #

# --- While loop method of fib sequence --- #
def while_loop():
    
    # Values 0, 1 and variables needed for while loop
    n1 = 0
    n2 = 1
    nth = n1 + n2

    # How many values of the seq. do you want to print
    count = 0

    # While count is less than no. keep looping
    while count < 10:
        print(n1, end=',')

        nth = n1 + n2
        n1 = n2
        n2 = nth
        
        count += 1

# --- For loop method of fib sequence --- #

def for_loop():
    # Empty list, soon values will be pasted into here
    count_list = []

    # Values 0, 1 and variables needed for 'for' loop
    count_fib_0 = 0
    count_fib_1 = 1

    # For loop keeps looping values
    for i in range(10):
        print(count_fib_0, end=',', flush=True)
        count_plus = count_fib_0 + count_fib_1
        count_fib_0 = count_fib_1
        count_fib_1 = count_plus
        
        count_list.append(count_plus)

# Variable to keep running user_input
user_input = True

# User input to know if for loop or while loop is running
while user_input:
    user_q = str(input("While loop or For loop: W/F: ")).upper()

    if user_q == "W":
        while_loop()
        break
    
    elif user_q == "F":
        for_loop()
        break
    
    else:
        user_q
                


