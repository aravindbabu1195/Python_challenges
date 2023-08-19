#match
import re
pattern="python"
if re.match(pattern,"python am a fresher,hyy "):
    print("Matched")
else:
    print("not matchec")
#search

pattern="inmakes"
if re.search(pattern,"hii inmakes am aravind"):
    print("matched")
else:
    print("not matched")

#findall
pattern="hyy"
print(re.findall(pattern,"hyy am aravind,helo mr inmakes,hyy its me "))

#findall&replace
pattern="hello"
new=re.sub(pattern,"hyy","hello am aravind,hello devo am a sci")
print(new)

#Dotmeta_character
pattern="p.th.n"
if re.match(pattern,"python"):
    print("correct")
else:
    print("incorrect")

#character_class
pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"L2d"):
    print("correct")
else:
    print("incorrect")