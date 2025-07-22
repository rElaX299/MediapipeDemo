print("helloworld!")

def add(a, b):
    return a + b

if __name__ == "__main__":
    # c = add(1, 2)
    # print(c)
    # colors = ['red', 'green', 'blue']
    # for color in colors:
    #     print(color)

    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}*{i}={i * j}", end="\t")
        print()