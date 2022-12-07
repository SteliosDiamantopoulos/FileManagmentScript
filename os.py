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

def rename_files_in_folder(source,user_input):
    counter=0
    for file in os.listdir():
        print(file)
        path = os.getcwd()
        old_path = os.path.join(path,file)
        if counter is 0:
            customVariable = 'ONE'
        elif counter is 1:
            customVariable = 'TWO'
        else:
            customVariable = "THREE"
        new_path = os.path.join(path,str(counter)+str(customVariable)+'.'+str(user_input))
        counter+=1
        os.rename(old_path,new_path)
        
        


        
    #print(oldname)
    

def main():
    path = os.getcwd()
    userchoice='png'
    a = path + "\\" + userchoice
    source_dir = os.chdir(a)
    rename_files_in_folder(source_dir,userchoice)
     #create_target_files(source_dir)


if __name__=='__main__':
    ##Chosse location for the script to be applied
    #source_dir = r"C:\Users\stdia\Desktop\PythonScripting\data"
    ##Make sure that the directory is the chosen one
    #path = os.getcwd()
    #userchoice=str(input("Enter File_Name TO Operate On:"))
    #userchoice='png'
    #a = path + "\\" + userchoice
    # source_dir = os.chdir(a)
    # print(source_dir)
    main()

