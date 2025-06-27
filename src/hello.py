def say_hello(name, times=1):
    """Prints a hello message multiple times."""
    # Intentional bug: off-by-one error, shadowing built-in, and unused variable
    for i in range(times):
        message = "Hello from CodeRabbit demo, " + name + "!"
        print(message)
    if times == 1:
        print("Only once!")
    # Unreachable code
    return

if __name__ == "__main__":
    say_hello("World")
    say_hello()  # Missing required argument in function definition