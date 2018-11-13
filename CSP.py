#variables of CSP
variables = ["state1", "state2", "state3", "state4", "state5", "state6", "state7", "state8", "state9",
             "state10", "state11", "state12"]


#possible values of the variables
domainValues = ["red", "green", "blue"]


#problem specific details
#The x and y positions of the blocks
positions = {}
positions["state1"] = [(2,1),(3,1),(4,1),(4,2)]
positions["state2"] = [(5,1),(5,2),(6,1),(6,2),(6,3),
                       (7,1)]
positions["state3"] = [(8,0),(8,1),(9,0),(9,1)]
positions["state4"] = [(7,2),(7,3),(7,4),(7,5),(7,6),
                       (8,2),(8,3),(8,4),(8,5),(8,6)]
positions["state5"] = [(7,7),(8,7),(9,6),(9,7),(10,7),
                       (11,7)]
positions["state6"] = [(5,3),(5,4)]
positions["state7"] = [(3,5),(4,4),(4,5)]
positions["state8"] = [(4,6),(5,5),(5,6),(5,7),(6,4),
                       (6,5),(6,6),(6,7),(6,8)]
positions["state9"] = [(3,6),(3,7),(4,7),(4,8),(5,8)]
positions["state10"] = [(1,8),(2,7),(2,8),(3,8)]
positions["state11"] = [(0,7),(0,8),(1,7)]
positions["state12"] = [(0,4),(0,5),(0,6),(1,4),(1,5),
                       (1,6),(2,4),(2,5),(2,6)]

#The blocks that border the given block
constraints = {}
constraints["state1"] = {"state2"}
constraints["state2"] = {"state1", "state3", "state4", "state6", "state8"}
constraints["state3"] = {"state2", "state4"}
constraints["state4"] = {"state2", "state3", "state5", "state8"}
constraints["state5"] = {"state4", "state8"}
constraints["state6"] = {"state2", "state7", "state8"}
constraints["state7"] = {"state6", "state8", "state9", "state12"}
constraints["state8"] = {"state2", "state4", "state5", "state6", "state7", "state9"}
constraints["state9"] = {"state7", "state8", "state10", "state12"}
constraints["state10"] = {"state9", "state11", "state12"}
constraints["state11"] = {"state10", "state12"}
constraints["state12"] = {"state7", "state9", "state10", "state11"}


def checkConstraints(assignment, variable, value):
    """
    This method checks if the constraints are violated
    It returns true if the constraints are not violated
    """
    #find the neighbours of the variable
    neighbours = constraints[variable]
    for neighbour in neighbours:
        #find if the neighbour has been assigned a value
        if neighbour in assignment:
            #check if the neighbour has the same value
            if assignment[neighbour] == value:
                return False
    return True
