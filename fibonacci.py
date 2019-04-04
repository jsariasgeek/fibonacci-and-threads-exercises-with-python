#1
#ToDo: Implement Fibonacci function recursively.

def caching(func):
    cache = {}
    def cache_func(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return cache_func

@caching
def fibonacci_recursive(n):
    
        """ Creates a fibonaccy with recursion, this will not calculate a big n, 
        but it's recursive 
        """
        if n < 1 or not isinstance(n, int):
            return "n has to be integer and greather than 0"

        if n == 1 or n  == 2:
            return 1
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
#1
#ToDo:Implement Fibonacci function non-recursively. 
#     Optimize to avoid recomputations.
def fibonacci_not_recursive(n):
        """Fibonacci not recursive optimized"""

        if n < 1 or not isinstance(n, int):
            return "n has to be integer and greather than 0"

        j = k = 1
        if n  == 1 or n == 2:
            return 1
        for i in range(n-2):
            if i%2 == 0:
                j+=k
            else:
                k+=j
        return max(j, k)
    

#1
#ToDo: Implement a class called Fibonacci to calculate 
#      the n-th value of the Fibonacci function.
class Fibonacci():
    """
    The class allows getting the n-th value of the 
    Fibonacci Function. The class can use  recursive
    and no-recursive methods.
    """
    def __init__(self, n):
        self.n = n
    
    def caching(func):
        cache = {}
        def cache_func(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = func(n)
                return cache[n]
        return cache_func


    @caching
    def fibonacci_recursive(self):
        """ Creates a fibonaccy with recursion, 
        this will not calculate a big n, 
        but it's recursive 
        """

        if self.n < 1 or not isinstance(self.n, int):
            return "n has to be integer and greather than 0"


        if self.n == 1 or self.n  == 2:
            return 1
        return fibonacci_recursive(self.n-1) + fibonacci_recursive(self.n-2)

    def fibonacci_not_recursive(self):
        """Fibonacci not recursive optimized"""

        if self.n < 1 or not isinstance(self.n, int):
            return "n has to be integer and greather than 0"

        j = k = 1
        if self.n  == 1 or self.n == 2:
            return 1
        for i in range(self.n-2):
            if i%2 == 0:
                j+=k
            else:
                k+=j
        return max(j, k)
    