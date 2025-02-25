# write a python program to execute a string containing python code

code = "print('Hello, world!')"        # 1
exec(code)

# 2
code= """                              
for i in range(5):
    print(f"line {i+1}")

    """
exec(code)