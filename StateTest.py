



from State import State

initialState = State()
intermediateState = State(initialState.assignment, "state1", "red")

variable = intermediateState.selectUnassignedVariable()
print "selectUnassignedVariable", variable

print "------------------------"


print "orderDomainValues", intermediateState.orderDomainValues(variable)

