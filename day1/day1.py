with open('input.txt', 'r') as file:
    data = file.read()

grouped = data.split("\n\n")
sums = list(map(lambda g: sum(list(map(int, g.split("\n")))), grouped))
sums.sort(reverse = True)

# Part 1
print(sums[0])

# Part 2
print(sum(sums[0:3]))
