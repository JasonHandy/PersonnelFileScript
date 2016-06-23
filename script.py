import os

folder_path = os.path.expanduser('~') + '/Desktop'
text_path = folder_path + 'list.txt'

if not os.path.exists(folder_path + '/PersonnelFiles'):
    os.mkdir(folder_path + '/PersonnelFiles')

folder_path += '/PersonnelFiles'


def make_dirs():
    file = open(text_path, 'r')

    for line in file:
        str = line
        words = str.split(" ")
        hall = '/' + words[1].strip("\n")
        
        if not os.path.exists(folder_path + hall):
            os.mkdir(folder_path + hall)
        
    pop_dirs()


def pop_dirs():
    file = open(text_path, 'r+')
    
    for line in file:
        str = line
        words = str.split(" ")
        hall = '/' + words[1].strip("\n")
        name = '/' + words[0].strip("\n")
        
        if not os.path.exists(folder_path + hall + name):
            os.mkdir(folder_path + hall + name)

    print("Folders successfully created!")

make_dirs()
