#Example, #1

#Some times you need to write files. The file json notes2.txt did not 
#exsit priort to this. This will create a new file. If it does exist it
#will overwirte it. To avoid that you can use a lower case w - write. 
#Seek can also be used when writting files. If seek is 0 it will just 
#overwrite what you typed previously.  

# with open('json notes2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')
    

#___________________________________________________________

#Example #2    

#In order to write to a copy of text. First read then write follow
#the example bellow. Bellow we open two files. It will make a copy.
#

# with open('json notes.txt', 'r') as rf:
#     with open('json notes_copy.txt', 'w') as wf:
#             for line in rf:
#                 wf.write(line)


#___________________________________________________________

#Example #3

#This can also be done with images. But instead of just r we need
# to add binary "rb"

# with open('1200px-Google_2015_logo.PNG', 'rb') as rf:
#     with open('1200px-Google_2015_logo_copy.PNG', 'wb') as wf:
#             for line in rf:
#                 wf.write(line)


#___________________________________________________________

#Example #4

#This can also be done in chuncks as well. Everything can be
#looped as well.

# with open('1200px-Google_2015_logo.PNG', 'rb') as rf:
#     with open('1200px-Google_2015_logo_copy.PNG', 'wb') as wf:
#         chunk_size = 2058
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)