file=open("text.txt",'w')
file.close()

file=open("text.txt",'a')
file.write("hii am aravind")
file.close()

file=open("text.txt",'a')
file.write("\nam a web developer")
file.close()

file=open("text.txt",'r')
content=file.read()
print(content)
file.close()