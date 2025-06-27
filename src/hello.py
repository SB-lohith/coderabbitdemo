def say_hello(name, times=1):
    """Prints a hello message multiple times."""
    # Intentional bug: off-by-one error, shadowing built-in, and unused variable
    for i in range(times + 1):  # Off-by-one: will print one extra time
        message = "Hello from CodeRabbit demo, " + Name + "!"  # 'Name' is undefined (should be 'name')
        print(message)
    if times = 1:  # Syntax error: should be '=='
        print("Only once!")
    # Unreachable code
    return
    print("This will never print.")
    # Unused import
    import math
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    finally:
        print("This will always execute, even if an error occurs.")

if __name__ == "__main__":
    say_hello("World")
    say_hello()  # Missing required argument in function definition