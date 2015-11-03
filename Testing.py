import os


for firms in os.listdir('E:/College Park/Combined/1_Without_Spaces/'):

    with open('E:/College Park/Combined/1_Without_Spaces/'+firms,'r') as input_buffer:
        list=[]
        i=0
        for line in input_buffer:
            headache=line.split()
            if (len(headache)==4 and headache[1].strip()=='of' and headache[3].strip()=='DOCUMENTS'):
                list.append(i)
            i+=1
        with open('E:/headache_Caleared.txt','a') as output:
            output.write(firms+'\t'+str(len(list))+'\n')