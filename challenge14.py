#Creating a tuple and insert ,append values to the tuple then show the index value of 2nd last value on the tuple.
Movies=("jhon wick","interstellar","Inception","Shazam","TENET","uncharted","Shang_chi","Eternals","Zack snyder's","WW84")
print(Movies)

y=list(Movies)
print(type(y))
print(y)

y.append("2018")
print(y)

y.insert(2,"PS-2")
print(y)

print(y.index("WW84"))

Movies=tuple(y)
print(type(Movies))
print(Movies)