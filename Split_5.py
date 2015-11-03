import os
import regex

for firms in os.listdir('F:/College Park/Combined/1_Without_Spaces/'):
    print(firms)
    #os.mkdir('F:/College Park/Combined/2_Split_Files/'+firms.strip('.txt'))
    with open('F:/College Park/Combined/1_Without_Spaces/'+firms,'r') as input_buffer:
        list=[]
        i=0
        for line in input_buffer:
            headache=line.split()
            if (len(headache)==4 and headache[1].strip()=='of' and headache[3].strip()=='DOCUMENTS'):
                list.append(i)
            i+=1
    with open('F:/College Park/Combined/1_Without_Spaces/'+firms,'r') as input_buffer:
        data = input_buffer.read().splitlines(True)
        n=1
        for n in range(0,len(list)):
            i=list[n]
            firm_name=firms.strip('.txt')
            headline=regex.sub(r'[^\w]', ' ', data[i+3].strip()).replace('  ',' ')
            if(len(headline)>50):
                headline=headline[0:50]
            raw_date=data[i+2].strip().split()
            if(len(raw_date)<3):
                date=raw_date[0]+' '+raw_date[1]
            else:
                date=raw_date[0]+' '+raw_date[1].replace(',','')+' '+raw_date[2]
                date=regex.sub(r'[^\w]', ' ', date)
            source=regex.sub(r'[^\w]', ' ', data[i+1].strip())
            few_lines=regex.sub(r'[^\w]', ' ', data[i+7].strip())+'----'+regex.sub(r'[^\w]', ' ', data[i+8].strip())+'----'+regex.sub(r'[^\w]', ' ', data[i+9].strip())+'----'+regex.sub(r'[^\w]', ' ', data[i+10].strip())
            '''
            file_name=str(n+1)+'-'+firm_name+'-'+headline+'-'+date+'-'+source+'.txt'


            with open('F:/College Park/Combined/2_Split_Files/'+firms.strip('.txt').strip()+'/'+file_name,'w') as output_buffer:
                if(n==len(list)-1):
                    output_buffer.writelines(data[i:len(data)])
                else:
                    output_buffer.writelines(data[list[n]:list[n+1]])


                    '''

            with open('F:/College Park/Combined/Deliverable1.txt','a') as output:
                output.write(str(n+1)+'\t'+firm_name+'\t'+headline+'\t'+date+'\t'+source+'\t'+few_lines+'\n')

