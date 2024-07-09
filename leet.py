#! /usr/bin/python3

from solution import Solution
from parse import Parsing

testcases = Parsing.parse(filename="testcases.txt", elements=["list", "number"])

for testcase in testcases:
    answer = Solution.solution(testcase[0], testcase[1])
    print(testcase)
    print(answer)
    print("\n\n")