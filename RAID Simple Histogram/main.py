# Xavier Raty RAID Simple Histogram

list = []
num = int(input("How long is your histogram?: "))

for i in range(1, num +1):
    list.append(int(input("What number do you want next in your list?\n")))

print("\n")

for y in range(0, len(list)):
    print(f"{y}:\n")
    for yAsterisk in range(list[y]):
        print("*", end = "")
    print("\n")