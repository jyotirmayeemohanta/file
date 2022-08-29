file=open("question3.txt","r")
v=file.read()
newfile1=open("delhi.txt","w")
newfile2=open("shimla.txt","w")
newfile3=open("others.txt","a")
l=v.split("\n")
i=0
while i<len(l):
    if "delhi" in l[i]:
        newfile1.write(l[i])
        newfile1.write("\n")
    elif "shimla" in l[i]:
        newfile2.write(l[i])
        newfile2.write("\n")
    else:
        newfile3.write(l[i])
        newfile3.write("\n")
    i+=1
newfile1.close()
newfile2.close()
newfile3.close()
file.close()