# beatles = ["John", "Mark", "James"]
# beatles.append ("KEN")
# print(beatles)
# print(len(beatles))
# others = ['jack','rick','Mike']
# beatles.extend(others)
# beatles.extend(['1','2','3'])
# print(beatles)
# print(len(beatles))
# print(beatles[0])
# beatles[0] = "bob"
# print(beatles[0])
# print(beatles[-1])
# print(len(beatles))
# print(beatles[len(beatles) - 2])
# beatles[len(beatles)-2] = 100
# print(beatles[len(beatles) - 2])
# beatles.insert(0,"1000")
# print(beatles)
# del beatles[1]
# print(beatles)
# test = beatles.pop()
# print(test)

# continents = [
#     'Asia',
#     'South America',
#     'North America',
#     'Africa',
#     'Europe',
#     'Antarctica',
#     'Australia'
# ]

# for continent in continents:
#     if continent[0] == "A":
#      print("* " + continent)


turtles = [
    "Michelangelo",
    "Leonardo",
    "Raphael",
    "Donatello",
]

def shredder(names):
    if len(names) >= 5:
        names[3] = "Bebop"

shredder(turtles)

for turtle in turtles:
    print("* " + turtle)