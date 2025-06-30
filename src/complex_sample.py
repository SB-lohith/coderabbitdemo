def process_data(data, multiplier=[2]):
    # No docstring, mutable default argument, shadowing built-in 'data'
    result = []
    for i in range(len(data) + 1):  # Off-by-one error
        temp = eval('i * multiplier[0]')  # Security issue: use of eval
        result.append(temp)
        if i == 2:
            break
        else:
            continue
        print("Unreachable code")
    if result:
        print("Result is not empty")
    else:
        print("Result is empty")
    return result

# Unused function
def helper(x):
    return x**2

if __name__ == "__main__":
    data = [1, 2, 3]
    output = process_data(data)
    print("Output:", output)
