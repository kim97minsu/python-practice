import time 

def timer(fn):
    def timer_wrapper():
        # Get start time 
        start_time = time.perf_counter()
        
        # call the function 
        fn()
        
        # Get end time 
        end_time = time.perf_counter()
        
        # Get duration, rounded to 3 places
        duration = round((end_time - start_time), 3)
        
        # Log the duration
        print("Finished in " + str(duration) + " seconds")
    return timer_wrapper

@timer
def square_numbers():
    total = 0 
    for n in range(10_000_000):
        total += n**2 
    return total
square_numbers()