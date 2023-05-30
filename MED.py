import numpy as np

source="intention"
target="execution"

MED=np.random.randint(0,1,size=(len(source)+1,len(target)+1))


for i in range(len(source)):

    for j in range(len(target)):

        if i==0 and j ==0:

            MED[i][j]=0

for i in range(len(source)+1):

    
    MED[i][0]=i


for i in range(len(target)+1):

    MED[0][i]=i

counter_i=0


for i in range(len(source)+1):
    cointer_j=0
   
    for j in range(len(target)+1):

        result=[]
        s=source[counter_i]
        t=target[cointer_j]

        if (i != 0 and j !=0):


            insert=(MED[i][j-1])+1
            sub=(MED[i-1][j-1])
            delete=(MED[i-1][j])+1

            if s != t :
                sub+=2

            result.append(insert)
            result.append(sub)
            result.append(delete)

            MED[i][j]=min(result)

            if cointer_j + 1 < len(target):
                cointer_j += 1


    if counter_i + 1 < len(source):
            counter_i += 1
     
print(MED)

print("MED:",MED[-1][-1])


        




    