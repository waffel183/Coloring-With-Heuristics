import CSP
import collections
import numpy as np
import copy





class State:
    '''
    This class retrieves state information for search application
    '''
    
    def __init__(self, assignment = None, variable = None, value = None):
        if assignment == None:
            #create initial state
            self.assignment = self.getInitialState()
        else:
            assignment1 = copy.deepcopy(assignment)
            assignment1[variable] = value
            self.assignment = assignment1
            

    def getInitialState(self):
        """
        This method returns empty dictionary
        """
        return collections.OrderedDict()


    def findPossibleValuesCount(self, variable):
        """
        This method finds the number of pissible values for the variable
        """
        #for each domain values find which ones satisfies the constraints
        count = 0
        for value in CSP.domainValues:
            if CSP.checkConstraints(self.assignment, variable, value):
                count += 1
        return count


    def findConstraintsCount(self, variable):
        """
        This method finds the number of constraints created by a variable
        on the remaining variables
        In this ase, it is the number of neighbours
        """
        count = 0
        #find all neighbours
        for neighbour in CSP.constraints[variable]:
            #find neighbours which are not assigned
            if neighbour not in self.assignment:
                count += 1
        return count
    

    def selectUnassignedVariable(self):
        """
        This method returns one variable which has not been assigned according
        to heuristics: most constrained variable and most constraining variable
        """
        #find the most constrained var
        remainingValues = {}
        #calculate the pssible values for each variable
        for variable in CSP.variables:
            if variable not in self.assignment:
                remainingValues[variable] = self.findPossibleValuesCount(variable)

        #find the variable with least remainingValues
        min_val = min(remainingValues.itervalues())
        minVariables = [k for k, v in remainingValues.iteritems() if v == min_val]
        #print "remainingValues" , remainingValues
        #print "minVariables" , minVariables

        #if there are multiple values, use a tie-breaker
        if len(minVariables) > 0:
            #find the most constraining variable
            constraintCounts = {}
            #find the variable with most constraints on the max constrained variables
            for variable in minVariables:
                constraintCounts[variable] = self.findConstraintsCount(variable)

            #find the variable with maximum constraints
            max_val = max(constraintCounts.itervalues())
            maxConVar = [k for k, v in constraintCounts.iteritems() if v == max_val]
            #print "constraintCounts" , constraintCounts
            #print "max_val", max_val
            #print "maxConVar" , maxConVar

            return maxConVar[0]


    def orderDomainValues(self, variable):
        """
        This method return the values in a particular order
        """
        #find the count of the possible values for all remaining neighbours
        # for each domain value assigned to variable
        neighbourValuesCounts = []
        #for each domain value
        for value in CSP.domainValues:
            #check if that value is possible
            if CSP.checkConstraints(self.assignment, variable, value):
                neighbourValuesCount = 0

                #create a child state
                childState = State(self.assignment, variable, value)

                #for all vairalbe's neighbours
                for neighbour in CSP.constraints[variable]:

                    #check if it has not been assigned, remaining variable
                    if neighbour not in self.assignment:

                        #count the possible domain values for this neighbour
                        #for each domain value
                        for value1 in CSP.domainValues:
                            #check if it satisfies the constraints
                            if CSP.checkConstraints(childState.assignment,
                                                     neighbour, value1):
                                neighbourValuesCount += 1
                #since we want to sort in decreasing order, we will add
                #negative of this count
                neighbourValuesCounts.append(-neighbourValuesCount)
            else:
                #if constraints are not satisfied
                neighbourValuesCounts.append(0)
        #print "neighbourValuesCounts", neighbourValuesCounts

        #order the domain values in increasing order of these counts
        sortedCounts = sorted(zip(neighbourValuesCounts,CSP.domainValues))
        #print "sortedCounts", sortedCounts
        orderedValues = [x for (_,x) in sortedCounts]

        return orderedValues
    

    def checkGoalState(self):
        """
        This method checks whether the path is goal state
        """
        #check if all the variables have been assigned
        return len(self.assignment) == len(CSP.variables)


    def drawState(self):
        """
        This method draws the state
        """
        image = np.zeros((12,11,3), np.uint8)
        for key in self.assignment:
            #find the channel index
            if self.assignment[key] == "red":
                channelIndex = 0
            elif self.assignment[key] == "green":
                channelIndex = 1
            else:
                channelIndex = 2
            for (xcoord, ycoord) in CSP.positions[key]:
                image[xcoord, ycoord, channelIndex] = 255
        return image
