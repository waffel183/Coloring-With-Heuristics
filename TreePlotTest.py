



from Node import Node
from State import State
from TreePlot import TreePlot
import CSP


initialState = State()
root = Node(initialState)

#find an unassigned variable
variable = root.state.selectUnassignedVariable()

#for all values in the domain
value = root.state.orderDomainValues()[0]

#check if constraints are satisfied
if CSP.checkConstraints(root.state.assignment,
                        variable, value):

    childNode = Node(State(root.state.assignment, variable, value))
    root.addChild(childNode)

    #show the search tree explored so far
    treeplot = TreePlot()
    treeplot.generateDiagram(root, childNode)
