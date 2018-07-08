'''
there are two ways of writing or saving data 
to a file ,i.e, writing and appending
 
 In writing to a file all the data which was
 earlier present in the file is overrided that
 is the data which was earlier there in the 
 file will be deleted form the file and new 
 data will replace it whereas
 
 In appending the we add the new data to the file
 without affecting the data present in the file
 '''
 
text = 'Sample Text To Save\nNew Line! '

saveFile = open('exampleFile.txt','w') #if this file doesn't exist then it will be autometically created 

saveFile.write(text)
saveFile.close()

saveFile = open('../../exampleFile2.txt','w') 
saveFile.write(text)
saveFile.close()