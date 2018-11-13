import CSP

assignment = {}
assignment["state1"] = "red"

print CSP.checkConstraints(assignment, "state3", "blue")
print CSP.checkConstraints(assignment, "state3", "red")
