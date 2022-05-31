import os
import sys

def menu():
    print('1-Path directory')
    print('2-Local path')

def menu_format():

    print('\n')
    print('For change all files, enter with "all" ')
    print('For others, enter with a format ')
    print('Ex: .txt, .pdf, .doc, .jpn, all'+'\n')

def show_files(files):
    for file in files:print(file + ', ',end='')

def search_format(type_format,files,total):
    files_format = []
    for file in range(total):
        if(files[file].endswith(type_format)):
            files_format.append(files[file])
    return files_format

def choice_files(path):

    files = os.listdir(path)
    print('\n' +'Files:'  +'\n')
    print('Total: ' + str(len(files)))
    show_files(files)

    menu_format()
    
    type_format = input('Type : ').lower()

    print()
    print('How much?')
    input_user_total = int(input('Amount : '))

    files_format = search_format(type_format,files,input_user_total)
    
    if(type_format=='all'):
      
        files_format =files

    return files_format

def file_renamer(path):

    files = choice_files(path)
    if(len(files)==0):print('There is not this format')

    else:
   
        print()
        input_user = input('Enter with new file name :')
        print()
        i =0
        for file in files:
            if(file !='FileRenamer.py'): 
                index = file.find('.')
                old_name = path +'/'+ file 
                new_name = path +  '/' + file.replace(file[:index],input_user+ str(i)) 
                if(os.path.exists(new_name)):print('This file alredy exist' +'\n')
                else: os.rename(old_name,new_name)
                
                i = i +1

        files = os.listdir(path)
        show_files(files)
        print()


def main():
    input_user=4
    while(True):
        print()
        menu()
        input_user = int(input('Option :'))

        if(input_user==1): path = input('Path :')
        elif(input_user==2):path = os.getcwd()
        else:sys.exit('Invalid Input')

        file_renamer(path)
main()
