#Example #1

#When, opening files we also need to close them

#f = open('filename', 'r')

#print(f.name) 
#Name will only print out the file name. 
#Instead of name you can use mode. Mode will show you
#mode that the files is currently open with. In this 
#situaton it would be r that stand for read.

#f.close()

#___________________________________________________________

#Example #2

#If we open a file as per above it is important to 
#explicitly close the file. If you forget to close the
#file it will only get you unecessary errors. By using 
#context manager we can easily avoid this with "with".
#This method allows us to work with files within a
#block of code. Once it is done it will it will automaticaly
#close the block of code once used.

#with open('json notes.txt', 'r') as f:
    #f_contents = f.readline() #You can also use read.line to read the first
    #line of the file and this can be repeated multiple times.
    #print(f_contents)


#___________________________________________________________

#Example #3

#Sometimes we have very large files that need to be read 
#efficiently. To do that we can simply iterate the lines in
#a file

#with open('json notes.txt', 'r') as f:

    #for line in f:
        #print(line, end='')


#___________________________________________________________

#Example #4

#If you want more control over the file you can specify the 
#amount of data that you want to read at a time by passing in
#the size as an argument. If I would wirite "f_contents = f.read(100)"
#it will only print out first 100 characters. By repeating the code
#it would print out 200, 300, etc. Because it picks up where it left
#off and write a 100 more characters. But if we will use this too many
#times nothing will happen since we have reached the limit and it only
#returns an empty string. This technique will help you read a file without
#knowing the true size of it. For this we would use a loop that iterates
#small chuncks of text(data) with size_to_read variable. It is bound to
#reach the end of the file and it will only print out empty strings.
#To avoid that we will use while loop.

#with open('json notes.txt', 'r') as f:

    #size_to_read = 10

    #f_contents = f.read(size_to_read)

    #while len(f_contents) > 0:
        #print(f_contents, end='*') #Adding astrix to the loop shows chunks
        #of file that was read by marking it each time.
        #f_contents = f.read(size_to_read)


#___________________________________________________________

#Example #5

#When we read from files in chuncks each time it advances it 
#as per previous example. We can actually specify the current
#possition using f.tell. We can also munipulate our current 
#with seek method. Let's print the first 20 characters of the
#file by running f.read twice and add f.seek(0). It will set our
#position to the begining of the file.

with open('json notes.txt', 'r') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)


 