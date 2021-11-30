stones=list(map(int,input().split()))


def hop(a,N,i,fact,trippleHop_flag):
	if(i>=N):
		return 0

	score = 0
	if(i!=-1):
		score = fact*a[i]

	#Single Hop
	singleHop = hop(a,N,i+1,1,trippleHop_flag)

	#Double Hop
	doubleHop = hop(a,N,i+2,2,trippleHop_flag)

	#Tripple Hop
	trippleHop = 0

	if(trippleHop_flag==False):
		trippleHop = hop(a,N,i+3,3,trippleHop_flag=True)

	greatest = max(singleHop, doubleHop, trippleHop)

	total_score = score + greatest

	return total_score



print(hop(stones, len(stones), -1, 1, False))