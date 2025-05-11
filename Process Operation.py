def process_operations(*args, **kwargs):
    
    if len(args) == 0: 
        raise ValueError("At least one number must be provided.")

    for arg in args: 
        if not isinstance(arg, (int, float)): 
            raise TypeError(f"Invalid argument {arg}. All positional arguments must be numbers.")

    results = {}

    if kwargs.get("add"):
        results["add"] = sum(args)

    if kwargs.get("subtract"):
        result = args[0]

        for num in args[1:]: 
            result -= num
        results["subtract"] = result
        
        
    if kwargs.get("multiply"):
        result = 1
        for num in args:
            result *= num
            
        results["multiply"] = result

    if kwargs.get("divide"):
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero.")
            result /= num
        results["divide"] = result

    return results

def calculate(*args, **kwargs):
    return process_operations(*args, **kwargs)

if __name__ == "__main__":
    print(calculate(10, 5, add=True, subtract=True)) 
    print(calculate(3, 4, multiply=True)) 
    print(calculate(100, 10, 2, divide=True))