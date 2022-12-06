import os
import numpy as np
import shutil




def unique(list1):
    x=np.array(list1)
    return (np.unique(x))

##Function that identifies file types from a certain directory
def figure_file_types(source_dir):
    file_type_list = []
    for file in os.listdir():
        file_type = file.split(".")[-1:]##Get the last element form the file name which is the type
        file_type_list.append(file_type)
    types = unique(file_type_list)#[0:(len(file_type_list))]
    return(list(types))

##Move folders to created directories
def create_target_files(source):
    types = figure_file_types(source)
    for ex in types:
        try:
            print(ex,end=",")
            os.mkdir(source + "\\"+ex)
            path = os.getcwd()
            for file in os.listdir():
                if ex in file :
                    shutil.move(file,path+"\\"+ex)
        except:
            continue

def main():
     create_target_files(source_dir)

if __name__=='__main__':
    ##Chosse location for the script to be applied
    #source_dir = r"C:\Users\stdia\Desktop\PythonScripting\data"
    ##Make sure that the directory is the chosen one
    source_dir = os.getcwd()
    main()

