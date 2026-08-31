import ValidParenthesis as vp
import PlusOne as po
import ctypes 

#Creates a little dialogue box (for fun)
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#Runs test cases 
def testCases(test, testList, solns):
    for i in testList:
        idx = testList.index(i)
        if solns[idx] == test(i):
            pass
        else:
            return Mbox('Failed', 'One or More Tests Failed', 0)
        
    return Mbox('Passed', 'All Tests Passed', 0)


### Test Cases for Valid Parenthesis
testVP = vp.Solution.isValid
testListVP = ["()","()[]{}","(]", "([])", "([)]"] 
solnsVP = [True, True, False, True, False]

### Test Cases for Plus One
testPO = po.Solution.plusOne
testListPO = [[1,2,3], [4,3,2,1], [9], [9,9,9]]
solnsPO = [[1,2,4], [4,3,2,2], [1,0], [1,0,0,0]]


###Run Test Cases Here 
testCases(testVP, testListVP, solnsVP)
testCases(testPO, testListPO, solnsPO)