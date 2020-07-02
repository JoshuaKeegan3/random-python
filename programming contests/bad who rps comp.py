def get_wins(players):
    global tommy
    wins = 0
    for n in range(k):
        winners = []
        for i in range(0,len(players),2):
            j = i+1
            if (i == tommy and players[i] > players[j]) or (j == tommy and players[i] < players[j]):
                wins += 1
            elif i == tommy or j == tommy:
                return wins
            
            if players[i] > players[j]:
                winners.append(players[i])
                if i == tommy:
                    tommy1 = len(winners)-1
            else:
                winners.append(players[j])
                if j == tommy:
                    tommy1 = len(winners)-1
        players = winners
        tommy = tommy1
    return wins


def swap(i, j):
    global tommy
    temp = _i[i]
    if i == 0:
        tommy = j
    _i[i] = _i[j]
    _i[j] = temp
    
    
_i = input()
_i = _i.split(' ')
n=int(_i[0])
k=int(_i[1])
s = [0]*n
a_s = []
for i in range(n):
    for j in range(n):
        if i != j:
            a = s.copy()
            a[i]=1
            a[j]=1
            if a not in a_s:
                a_s.append(a)
_i = input()
_i = _i.split(' ')
for i in range(len(_i)):
    _i[i] = int(_i[i])
tommy = 0
norm = get_wins(_i)
win_dict = {}
for i in range(len(a_s)):
    tommy = 0
    swaps = []
    for j in range(len(a_s[i])):
        if a_s[i][j] == 1:
            swaps.append(j)
    swap(swaps[0], swaps[1])
    w = get_wins(_i)
    try:
        win_dict[w] += 1
    except:
        win_dict[w] = 1
    
    swap(swaps[0], swaps[1])

m = max(win_dict.keys())
if m <= norm:
    print(norm)
    print(-1)
else:
    print(m)
    print(win_dict[m])
