import os

for file in os.listdir('E:/College Park/Combined/Total_Main'):
    if (file[-7:-4]=='INC'):
         firm=file[0:-7]+'.txt'
    else:
        firm=file
    with open('E:/College Park/Combined/Total_Main/'+file) as file_read:
        with open('E:/College Park/Combined/Without_Spaces/'+firm,'w') as output:
            for line in file_read:
                if not line.isspace():
                    output.write(line)