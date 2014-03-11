#Problem: compute the first ten digits of a large sum

numbers = []

with open("reference/largesum.txt","r") as f:
    content = f.read().replace("\n","")
    numbers = [int(y) for y in [content[x:x+50] for x in range(0,len(content),50)]]

print str(sum(numbers))[0:10]
raw_input()
