
words = []
with open('old-corpus.csv','r') as infile:
    for line in infile.readlines():
        cells = line.strip().split(',')
        for word in cells[2].split(' '):
            words.append(word)

chunk = 200
lines = [[] for w in range(round(len(words)/chunk)+1)]
for i, word in enumerate(words):
    lines[round(i/chunk)].append(word)

with open('corpus.csv','w') as outfile:
    for i, line in enumerate(lines):
        outfile.write(str(i)+',foo,'+' '.join(line)+'\n')
