def support(fuset: dist):
    print("Support set:", end="")
    
    for element, membership in fuset.items():
        if membership > 0:
            print(element, end=" ")

A1 = {
    "a": 0.2,
    "b": 0,
    "c": 0.7,
    "d": 1
}

support(A1)
