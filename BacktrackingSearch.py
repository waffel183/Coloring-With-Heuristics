



from State import State
from Node import Node
import CSP
from TreePlot import TreePlot


class BacktrackingSearch():
    """
    this performs backtracking search
    """

    def search(self):
        """
        this method performs the search
        """
        #get the initail state
        initialState = State()

        #create root node
        rootNode = Node(initialState)

        #show the serarch tree explored so far
        treeplot = TreePlot()
        treeplot.generateDiagram(rootNode, rootNode)

        #perform search from root node
        self.performBacktrackSearch(rootNode, rootNode)


    def performBacktrackSearch(self, rootNode, node):
        """
        This creates the search tree
        """

        #print "-- proc --", node.state.assignment

        #check if we have reached our goal state
        if node.state.checkGoalState():
            print "reached goal state"
            return True
        else:
            #find an unassigned variable
            variable = node.state.selectUnassignedVariable()

            #for all values in the domain
            for value in node.state.orderDomainValues(variable):

                #check if constraints are satisfied
                if CSP.checkConstraints(node.state.assignment,
                                        variable, value):

                    #create child node
                    childNode = Node(State(node.state.assignment, variable, value))
                    node.addChild(childNode)

                    #show the search tree explorer so far
                    treeplot = TreePlot()
                    treeplot.generateDiagram(rootNode, childNode)

                    result = self.performBacktrackSearch(rootNode, childNode)
                    if result == True:
                        return True

            return False


bts = BacktrackingSearch()
bts.search()
