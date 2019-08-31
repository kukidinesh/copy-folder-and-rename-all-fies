#author Dinesh Goyal
import os
import shutil

copyFromFolder = 'meia'
newdomain_name = 'digimate'

fodlerpath = '/var/www/html/ra_meia/CIR/application/modules'
csspath = '/var/www/html/ra_meia/CIR/assets/css'
jspath = '/var/www/html/ra_meia/CIR/assets/js'



for folderName, subfolders, filenames in os.walk(fodlerpath):
    #print('The current folder is ' + folderName)


    # for subfolder in subfolders:
    #     print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
    
        if(filename.startswith(copyFromFolder)):

        	print('FILE INSIDE ' + folderName + ': '+ filename)
        	newfilename = filename.replace("meia",newdomain_name)
        	print('New FILE ' + folderName + ': '+ newfilename)
        	shutil.copy(folderName+"/"+filename,folderName+"/"+newfilename); 



    print('')

for folderName,subfolders, filenames in os.walk(csspath):

     for subfolder in subfolders:
    
         if(subfolder == copyFromFolder):
         	print('Css SUBFOLDER OF ' + folderName + ': ' + subfolder)
        	shutil.copytree(folderName+"/"+subfolder,folderName+"/"+newdomain_name)




print('')

for folderName,subfolders, filenames in os.walk(jspath):

     for subfolder in subfolders:
    
         if(subfolder == copyFromFolder):
         	print('JS SUBFOLDER OF ' + folderName + ': ' + subfolder)
        	shutil.copytree(folderName+"/"+subfolder,folderName+"/"+newdomain_name)




print('')