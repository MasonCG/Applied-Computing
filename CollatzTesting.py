#CollatZ Testing Suite

import Collatz_base as Base
import Collatz_Optimized as Optimized
import Collatz_Optimized_Bonus as Bonus
import time

range = 1_000_000

# getting time duration for base Collatz
s_time = time.time()

longest = Base.collatz_length_in_range(1, range)

duration = time.time() - s_time
print("base: ", duration, "s")

# getting time duration for Optimized Collatz
s_time = time.time()

longest = Optimized.collatz_length_in_range(1, range)

duration = time.time() - s_time
print("base: ", duration, "s")

