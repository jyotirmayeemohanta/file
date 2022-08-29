banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"] 
i=0
file=open("file-question3.txt","a")
for i in banks_list:
    file.write(i)
print(file)
