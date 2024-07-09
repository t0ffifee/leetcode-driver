from typing import List
import ast

def parse(elements:List[str]):
    lines = []
    with open("testcases.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    testcases = []
    while lines:
        testcase = []
        for el in elements: # later this will be handy if the have other types of variables as well
            line = lines.pop(0)
            testcase.append(ast.literal_eval(line))
        testcases.append(testcase)
    
    return testcases

print(parse(["list", "number"]))