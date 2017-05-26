def findOpt(array, N):
	return helper(array, N, 0)
def helper(array, N, state):
	localReward = 0
	localLoss = 0
	for idx, val in enumerate(array):
		if val == 1:
			localLoss += 1
		else:
			localReward += idx + 1
	feedBack = state * -1.0 * localLoss / N + localReward * 1.0 / N
	# print(feedBack)
	if feedBack > 0.01:
		print(feedBack)
		expectedReturn = 0
		for idx, val in enumerate(array):
			if val == 1:
				continue
			expectedReturn += helper(array, N, state + idx + 1) * 1.0 / N
		return expectedReturn
	else:
		return state

input = [
	# ([0,1,1,0], 4),
	# ([0,1,0,1,1,0,0,1,1,0,0], 11),
	# ([0,0,1,1,1,1,0,1,0,1,1,0,0,1], 14),
	# ([0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0], 28),
	# ([0,0,0,1,0,1,1,1], 8),
	# ([0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1], 21),
	# ([0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1], 22),
	# ([0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0], 16),
	# ([0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1], 19),
	([0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1], 27)
	]
for idx, data in enumerate(input):
	print("Q" + str(idx) + " : " + str(findOpt(data[0], data[1])))
