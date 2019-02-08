import string
import random

s = ''

for x in range(10):
	s += random.choice(string.ascii_letters)

for i in range(3):
	s+= str(random.randint(0,10))

r = s[::-1]

# It wasn't specified that I shouldn't, so  I'm overwriting the file each time.
f = open("revRandStrFile.txt", "w+")
f.write("s: " + s + "\n")
f.write("r: " + r + "\n")
f.close()
