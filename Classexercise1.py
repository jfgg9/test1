from urllib.request import urlopen

fd = urlopen("https://www.telegraph.co.uk/travel/destinations/europe/spain/madrid/articles/madrid-restaurants/")

counter = 0

for line in fd:
    line = line.decode()

    while True:

         pos = line.find("/", pos)

         if pos != -1:
             counter += 1
             pos += 1

         else:
             break


print(counter)
