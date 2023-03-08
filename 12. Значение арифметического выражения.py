try:
    a = input()
    exec(f"b = {a}")
    print(b)
except:
    print("WRONG")