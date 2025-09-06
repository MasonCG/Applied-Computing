#CollatZ Testing Suite

import Collatz_base as Base
import Collatz_Optimized as Optimized
import Collatz_Optimized_Bonus as Bonus
import time


def testing(range):

    # Setting up Askii Table
    print(f"Collatz Optimization Testing (1, {range})")
    print("Collatz Program\t\t Runtime\t\t\t Speedup")

    # getting time duration for base Collatz
    s_time = time.time()

    longest = Base.collatz_length_in_range(1, range)

    base_duration = duration = time.time() - s_time



    # storing base duration
    print("Base:\t\t\t", duration, "s\t\t", base_duration/duration)


    # getting time duration for Optimized Collatz
    s_time = time.time()

    longest = Optimized.collatz_length_in_range(1, range)

    duration = time.time() - s_time
    print("Optimized:\t\t", duration, "s\t\t", base_duration/duration)

    # getting time duration for Bonus Optimized Collatz
    s_time = time.time()

    longest = Bonus.collatz_length_in_range(1, range)

    duration = time.time() - s_time
    print("Bonus:\t\t\t", duration, "s\t\t", base_duration/duration)
    print('\n')


    
testing(1_000_000)
testing(10_000_000)