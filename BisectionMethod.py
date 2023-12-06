import math
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("The function has the same sign at both interval endpoints.")
        return None

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint  # Found exact root
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1

    return (a + b) / 2

def get_user_function():
    function_str = input("Enter the function: ")
    try:
        # Create a lambda function from the user input
        user_function = lambda x: eval(function_str, {'math': math}, {'x': x})
        return user_function
    except Exception as e:
        print("Error in the input function:", e)
        return None

def get_user_intervals():
    a = float(input("Enter the left endpoint of the interval(a): "))
    b = float(input("Enter the right endpoint of the interval(b): "))
    return a, b

if __name__ == "__main__":
    print("Bisection Method for Finding Roots")
    print("Example: Enter 'math.sin(x) - x' for sin(x) - x = 0")

    user_func = get_user_function()
    if user_func is None:
        exit()

    interval_a, interval_b = get_user_intervals()

    root = bisection_method(user_func, interval_a, interval_b)
    if root is None:
        print("No root found in the given interval.")
    else:
        print(f"Approximate root found at x = {root}")
