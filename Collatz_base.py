#Mason Goddard
#Applied computing
#Collatz with no optmization.


def collatz_length(num):
    """Get the number of steps it takes to go through Collatz Conjecture Sequence"""

    # keeps track of number of steps
    steps = 1
    # storing each step


    while (num != 1):
        
        #if num is odd
        if num % 2:
            num = num * 3 + 1
        else:
            num /= 2

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

