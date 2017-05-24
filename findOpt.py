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
	if feedBack > 0:
		expectedReturn = 0
		for idx, val in enumerate(array):
			if val == 1:
				continue
			expectedReturn += helper(array, N, state + idx + 1) * 1.0 / N
		return expectedReturn
	else:
		return state


print(findOpt([1,0,1,1,0,1], 6))