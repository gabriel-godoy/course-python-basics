friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Gets difference between sets
local_friends = friends.difference(abroad)

print(local_friends)          # set(['Rolf'])


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Annie"}

both_arts = art.intersection(science)
print(both_arts)              # set(['Bob', 'Jen'])
