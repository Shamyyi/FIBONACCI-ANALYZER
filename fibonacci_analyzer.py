import time

# ---------- Fibonacci implementations ----------

def fib_recursive(n, counter=None):
    if counter is not None:         # count this call
        counter[0] += 1             # base case
    if n <= 1:
        return n
    return fib_recursive(n - 1, counter) + fib_recursive(n - 2, counter)

def fib_memoized(n, memo=None, stats=None):
    if memo is None:
        memo = {}
    if stats is not None:
        stats["calls"] += 1
    if n <= 1:
        return n
    if n in memo:
        if stats is not None:
            stats["hits"] += 1
        return memo[n]
    memo[n] = fib_memoized(n - 1, memo, stats) + fib_memoized(n - 2, memo, stats)
    return memo[n]

def fib_iterative(n, counter=None):
    a, b = 0, 1
    for _ in range(n):
        if counter is not None:
            counter[0] += 1
        a, b = b, a + b
    return a

# ---------- Timing helper ----------

def timed(func, n):
    start = time.perf_counter()
    result = func(n)
    ms = (time.perf_counter() - start) * 1000
    return result, ms

# ---------- Compare all three for one n ----------
# Note: the higher the n, the longer processing takes overall,
# but recursive slows down MUCH faster (exponential) than
# memoized/iterative (linear) — that's the whole point of the demo.

def compare(n):
    r_counter = [0]
    i_counter = [0]
    m_stats = {"calls": 0, "hits": 0}

    r_val, r_time = timed(lambda x: fib_recursive(x, r_counter), n)
    m_val, m_time = timed(lambda x: fib_memoized(x, None, m_stats), n)
    i_val, i_time = timed(lambda x: fib_iterative(x, i_counter), n)

    print(f"\nF({n}) = {r_val}")
    print("Recursive:")
    print(f"  Time:  {r_time:.6f} ms")
    print(f"  Calls: {r_counter[0]:,}")
    print("Memoized:")
    print(f"  Time:        {m_time:.6f} ms")
    print(f"  Calls:       {m_stats['calls']:,}")
    print(f"  Cache hits:  {m_stats['hits']:,}")
    print("Iterative:")
    print(f"  Time:       {i_time:.6f} ms")
    print(f"  Iterations: {i_counter[0]:,}")

def performance_test():
    print("\nRunning multiple values to show growth in processing time...")
    for n in [5, 10, 20, 25, 30, 35]:
        compare(n)

def show_complexity():
    print("\nMethod       Time      Space")
    print("Recursive    O(2^n)    O(n)")
    print("Memoized     O(n)      O(n)")
    print("Iterative    O(n)      O(1)")
    print("\nHigher n = more processing time for all methods,")
    print("but recursive grows exponentially while memoized")
    print("and iterative stay fast even at large n.")

def get_n():
    while True:
        try:
            n = int(input("Enter n (0-40 recommended): "))
            if n >= 0:
                return n
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# ---------- Menu ----------

def main():
    while True:
        print("\n--- FIBONACCI ANALYZER ---")
        print("1. Input a value (compare all methods)")
        print("2. Performance test (multiple values)")
        print("3. Show time complexity")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            compare(get_n())
        elif choice == "2":
            performance_test()
        elif choice == "3":
            show_complexity()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()