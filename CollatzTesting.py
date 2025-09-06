#CollatZ Testing Suite

import Collatz_base as Base
import Collatz_Optimized as Optimized
import Collatz_Optimized_Bonus as Bonus
import time


def testing(range):

    # Setting up Askii Table
    print(f"Collatz Optimization Testing (1, {range})")
    print("Collatz Program\t\t Runtime\t\t\t Largest Pair (num, steps)")

    # getting time duration for base Collatz
    s_time = time.time()

    longest = Base.collatz_length_in_range(1, range)

    duration = time.time() - s_time
    print("Base:\t\t\t", duration, "s\t\t", longest)


    # getting time duration for Optimized Collatz
    s_time = time.time()

    longest = Optimized.collatz_length_in_range(1, range)

    duration = time.time() - s_time
    print("Optimized:\t\t", duration, "s\t\t", longest)

    # getting time duration for Bonus Optimized Collatz
    s_time = time.time()

    longest = Bonus.collatz_length_in_range(1, range)

    duration = time.time() - s_time
    print("Bonus:\t\t\t", duration, "s\t\t", longest)
    print('\n')
testing(10_000)
testing(1_000_000)