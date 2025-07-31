pres_set = set()
pres_set.update(["Aisha", "Bilal", "Zara"])
# A new student Hassan join in
pres_set.add("Hassan")
# Now a group of students joins in
pres_set.update(["Fahad", "Iqra", "Usman"])
# Now Bilal leaves the group
pres_set.remove("Bilal")
# Display the final set of students
print(pres_set)
# clear the set
pres_set.clear()
print(pres_set)  # This should print an empty set