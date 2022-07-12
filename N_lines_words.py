lines = []
line = []
i = 0
N = input("Enter count of the lines, integer, between 1 and 100: ")
N= int(N)
while N <= 0 or N > 100 :
    N = input("Enter integer N(between 1 and 100, inclusive): ")
    N= int(N)
while i < N:
    W = input("Enter line with min. one, max. 100 English words, separated by a spacewith length of every word is between 1 and 10 characters: ")
    #print (len(W))
    while (len(W) < 1) or (len(W) == 0) or (len(W.split()) > 100) or (len(max(W.split(), key=len)) > 10):
        W = input("Incorrect! Enter one word or max 100 words with one or max. 10 characters: ")
    line = W.split()
        #print(line)
        #for w in line:
            #if len(w) > 10:
                #break
    line.reverse()
    i+=1
    lines.append(line)
    #print(lines)
for line in lines:
    print(*line) 