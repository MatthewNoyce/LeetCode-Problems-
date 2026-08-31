import ValidParenthesis as vp
import ctypes 

#Creates a little dialogue box (for fun)
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def testCases():
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


if testCases():
    Mbox('Passed', 'All Tests Passed', 0)
else:
    Mbox('Failed', 'One or More Tests Failed', 0)