# corner cases description:
# 1. 2018-99-108 is not treated as date as they are not valid date. Rather, they are treated as 'NUM-NUM-NUM'
# 2. Type order matters. In responding to 'When strings of different basic types appear, you must separate the basic types'
# i.e. ['a1','3a', 'a3', 'a2016-06-02'] may be sorted to => ['a1', 'a3', 'a2016-06-02', '3a'] where 'a3' and '3a' are considered 
# to be different types.
# This protocol make case ['1', '2', '12a', 'a12', 'abc']

import re
from dateutil.parser import parse
class Solution:

	def __init__(self):
		pass

	def sortString(self, array):
		# quick sort
		self.helper(array, 0, len(array) - 1)
		return array

	def helper(self, array, start, end):
		# implement quick sort
		if start >= end:
			return
		left = start
		right = end
		pivot = array[start + (end - start) / 2]
		while left <= right:
			while left <= right and self.comparator(array[left], pivot):
				left += 1
			while left <= right and self.comparator(pivot, array[right]):
				right -= 1
			if left <= right:
				temp = array[right]
				array[right] = array[left]
				array[left] = temp
				left += 1
				right -= 1
		self.helper(array, start, right)
		self.helper(array, left, end)

	def getFirstElement(self, string, offset):
		# grab the first element from string
		stringLength = len(string)
		string = string[offset:]
		if offset >= stringLength:
			return ('', None, -1)
		ele = self.findFirstDate(string)
		if ele is not None:
			try: 
				# validate data-like substring
				parse(ele[0])
				return (ele[0], 'date', offset + ele[1])
			except ValueError:
				ele = None
		ele = self.findFirstAlpha(string)
		if ele is not None:
			return (ele[0], 'alpha', offset + ele[1])
		ele = self.findFirstnNum(string)
		if ele is not None:
			return (ele[0], 'num', offset + ele[1])

	def comparator(self, left, right):
		# universal comparator
		# return True when left < right
		# otherwise return False
		result = None
		offsetL = 0
		offsetR = 0
		while result is None:
			leftEle = self.getFirstElement(left, offsetL)
			offsetL = leftEle[2]
			rightEle = self.getFirstElement(right, offsetR)
			offsetR = rightEle[2]
			if rightEle[1] is None:
				result = False
			elif leftEle[1] is None:
				result = True
			elif leftEle[1] != rightEle[1]:
				result = self.flagComparator(leftEle[1], rightEle[1])
			else:
				flag = leftEle[1]
				if leftEle[0].lower() != rightEle[0].lower():
					if flag == 'date':
						result = self.dateComparator(leftEle[0], rightEle[0])
					if flag == 'alpha':
						result = self.alphaComparator(leftEle[0], rightEle[0])
					if flag == 'num':
						result = self.numComparator(leftEle[0], rightEle[0])
		return result

	def flagComparator(self, left, right):
		if left is None:
			return True
		if left == 'date' and right is not None:
			return True
		if left == 'alpha' and right != 'date' and right is not None:
			return True
		return False

	def dateComparator(self, left, right):
		left = left.replace('/', '-')
		right = right.replace('/', '-')
		return left < right

	def alphaComparator(self, left, right):
		return left.lower() < right.lower()

	def numComparator(self, left, right):
		return float(left) < float(right)

	def findFirstDate(self, input):
		# match the first date-like substring
		regex = re.compile(r'(^([\s\/-]*)(\d{4})/(\d{2})/(\d{2})|^([\s\/-]*)(\d{4})-(\d{2})-(\d{2}))')
		try:
			return regex.search(input).group(1).lstrip('/-\s'), regex.search(input).end()
		except AttributeError:
			return None

	def findFirstAlpha(self, input):
		# match the first alphabetic substring
		regex = re.compile(r'(^([\s\/-]*)[A-Za-z]+)')
		try:
			return regex.search(input).group(1).lstrip('/-\s'), regex.search(input).end()
		except AttributeError:
			return None

	def findFirstnNum(self, input):
		regex = re.compile(r'(^([\s\/-]*)[-+]?[0-9]*\.?[0-9]+)')
		regexNum = re.compile(r'[-+]?[0-9]*\.?[0-9]+')
		try:
			return regexNum.search(regex.search(input).group(1)).group(0), regex.search(input).end()
		except AttributeError:
			return None

tests =  [['a1', 'a2016-01-01', 'a3'],
			['-1', '2', '.2', '10', '-2.4'],
			['2016-10-1a2', '2016/10/19', '2017-01-01'],
			['Apple', 'bacon', 'Watermelon'],
			['abc45', 'abc123', 'def45'],
			['Ended on 2016-01-02', 'ended ON 2017-02-05', 'ended on 2017-01-05', 'started on 2016-01-02'],
			['a1', 'a2016-01-01', 'a3'],
			['-1', 'awb/2019', 'cd-0.2', 'abc1', 'abc--2.4', 'ended ON 2017-02-05', 'Awb -- 2018-01-02'],
			['Apple2016', '2016-07-08bacon', 'Watermelon'],
			['z1','z2008-08-08', 'a3', 'a2016-06-02']]
Sol = Solution()
for case in tests:
	print(Sol.sortString(case))