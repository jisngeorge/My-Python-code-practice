#Maximum profit
#Order of constraints - N K A
# N - Number of shares
# K - Maximum number that can be bought
# A - Money with the buyer
C = input('Enter constraints : ')
V = input('Enter the value of stocks : ')
P = input('Enter the profit percentage: ')
v = V.split()
p = P.split()
c = C.split()
N = int(c[0])
K = int(c[1])
A = float(c[2])
profit = list()
for i in range(N) :
# For knowing how many shares can be bought maximum given the money
    j = int(A / float(v[i]))
    if j > K : j = K
# Tuple containing profit% , value , profit , Maximum number of a particular share that can be bought with given money
    newtuple = (float(p[i]),float(v[i]),(float(v[i]) * float(p[i]) * 0.01),j)
    profit.append(newtuple)
# Sorting the list containing tuples with preference given to profit%
profit.sort(reverse = True)
# If shares with same profit% comes preference is given to the one with least value
for i in range(N - 1) :
    j = 0
    while j < N - i :
        if profit[i][0] == profit[i + 1][0] and profit[i][1] > profit[i + 1][1] :
            temp = profit[i]
            profit[i] = profit[i + 1]
            profit[i + 1] = temp
        j = j + 1
# Calculating how many shares of a particular stock needs to be bought for maximum profit
nos = list()
r = A
for i in range(N) :
    j = 1
    while j <= profit[i][3] :
        if r - (profit[i][1]) >= 0 :
            r = r - (profit[i][1])
        else : break
        j = j + 1
    if r >= 0 :
        nos.append(j - 1)
# Calculatin the maximum profit
maxprofit = 0
for i in range(N) :
    maxprofit = maxprofit + nos[i] * profit[i][2]
# Rounding the maximum profit
temp = maxprofit - int(maxprofit)
if temp < 0.5 : print(int(maxprofit))
elif temp > 0.5 : print(int(maxprofit) + 1)
elif int(maxprofit) % 2 != 0 : print(int(maxprofit) + 1)
else : print(int(maxprofit))
