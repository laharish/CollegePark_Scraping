import os
import shutil


def Move(name):
    list=os.listdir('C:/Users/laharish/Downloads')

    for file in list:
        if(file.startswith('Major_US_Newspapers')):

            with open('C:/Users/laharish/Downloads/New/'+name+'.txt', 'a') as outfile:
                outfile.write('\n')
                with open('C:/Users/laharish/Downloads/'+file) as infile:
                    for line in infile:
                        outfile.write(line)

            shutil.move('C:/Users/laharish/Downloads/'+file,'C:/Users/laharish/Downloads/500/'+name+'.txt')
