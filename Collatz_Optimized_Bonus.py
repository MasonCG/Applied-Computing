#Mason Goddard
#Applied computing
#Collatz with no optmization.

# empty dictionary to store collatz numbers
collatz_dict = {}

def store_collatz(num):
    """ Used to store number into a dictionary"""
    # keeps track of number of steps
    steps = 1
    # storing original num
    n = num

    while (n != 1):
        
        if n in collatz_dict:
            steps += collatz_dict[n] - 1
            collatz_dict[num] = steps
            return

        #if num is odd
        if n % 2:
            n = n * 3 + 1
        else:
            n = n//2

        steps += 1
    
    collatz_dict[num] = steps



def collatz_length(num):
    """Get the number of steps it takes to go through Collatz Conjecture Sequence"""

    # keeps track of number of steps
    steps = 1
    # storing original num
    n = num



    while (n != 1):
        
        if n in collatz_dict:
            steps += collatz_dict[n] - 1
            return steps
        else: 
            store_collatz(n)
            if n % 2:
                n = n * 3 + 1
            else: 
                n = n//2

        steps += 1
        
    return steps

def collatz_length_in_range(s_num, e_num):
    """ Getting the largest number of steps in Collatz Conjecture for each number withing the given range"""
    
    # starting value of length
    length = 0
    l_num = 1

    for i in range(s_num, e_num):
        t_length = collatz_length(i)
        if (t_length > length):
            length = t_length
            l_num = i

    return l_num, length

