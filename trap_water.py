def trap_water(arr,n):
	start = arr[0]
	start_index = 0
	water = 0
	end = 0

	for i in range(1,n):
		if(arr[i]>=start):
			start = arr[i]
			start_index = i
			end = 0
		else:
			water+=start-arr[i]
			end+=start-arr[i]

	if(start_index<n-1):
		water-=end
		start = arr[n-1]

		for i in range(n-1,start_index-1,-1):
			if(arr[i]>=start):
				start = arr[i]
			else:
				water += start-arr[i]

	return water


if __name__=="__main__":
	arr = list(map(int,input().split(" ")))
	print(trap_water(arr,len(arr)))