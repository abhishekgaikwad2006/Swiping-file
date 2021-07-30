def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1,'r') as a:
     data_a = a.read()

    with open(file2)  as b:
     data_b = b.read()    


    with open(file2)  as a:
     a.write(data_b)    

    with open(file2)  as b:
     b.write(data_a)    