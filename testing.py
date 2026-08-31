import ValidParenthesis as vp
import PlusOne as po
import ctypes 

#Creates a little dialogue box (for fun)
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def testCasesVP():
    output = True
    test = vp.Solution
    testList = ["()","()[]{}","(]", "([])", "([)]"]
    solns = [True, True, False, True, False]
    for i in testList:
        idx = testList.index(i)
        if solns[idx] == test.isValid(i):
            output= True
        else:
            #Kicks you out of the function as soon as a test fails
            return False
    return output

def testCasesPO():
    output = True
    testList = [[1,2,3], [4,3,2,1], [9], [9,9,9]]
    solns = [[1,2,4], [4,3,2,2], [1,0], [1,0,0,0]]
    test = po.Solution
    for i in testList:
        idx = testList.index(i)
        if solns[idx] == test.plusOne(i):
            output = True
        else:
            return False
    return output

if testCasesVP():
    Mbox('Passed', 'All Tests Passed For Valid Parenthesis', 0)
else:
    Mbox('Failed', 'One or More Tests Failed', 0)

if testCasesVP():
    Mbox('Passed', 'All Tests Passed For Plus One', 0)
else:
    Mbox('Failed', 'One or More Tests Failed', 0)

