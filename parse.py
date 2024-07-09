from typing import List
import ast

class Parsing:
    def parse(filename, elements:List[str]):
        lines = []
        with open(filename, "r") as f:
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