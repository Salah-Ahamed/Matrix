#Importing moudles
import MatrixS.MatFuns

#Getting size of the matrix from the user
ms=input("Type matrix size (2x2 to 9x9 only) : ")

#Getting values for the matrix
if((len(ms)>3) or (len(ms)<3)):
    print("Invalid input")

else:
    MatrixS.MatFuns.GetValues(ms)
    
#Printing matrix size
    print("\nMatrix size : ",ms)

#Printing the matrix
    MatrixS.MatFuns.DisMatrix()

#Getting a value to multiply the matrix
    print("\n")
    mul=int(input("Type a value to multiply the matrix : "))

#Printing new Matrix size
    print("\t")
    print("Matrix size : ",ms)

#Printing the new matrix
    MatrixS.MatFuns.PrintNew(mul)


