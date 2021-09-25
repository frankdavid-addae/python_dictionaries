name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        # print(words)
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
        # print(counts)

highestCount = None
highestSender = None

for sender, count in counts.items():
    if highestCount is None or count > highestCount:
        highestSender = sender
        highestCount = count

print(highestSender, highestCount)

