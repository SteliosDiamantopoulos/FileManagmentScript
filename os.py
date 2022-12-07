import os
import numpy as np
import shutil



def increment():
    global COUNT
    COUNT = COUNT+1
    return COUNT



def unique(list1):
    x=np.array(list1)
    return (np.unique(x))

##Function that find all the unique projectNO in a folder of FILE TYPES
def find_project_no (source):
    #print(source)
    projectList=[]
    for file in os.listdir(source):
        get_file_type = file.split('.')
        #print((get_file_type))
        if len(get_file_type)>1:
            projectno=file.split('-')[1]
            #print(projectno)
            projectList.append(str(projectno))
    #print(projectList)
    return (projectList)


##Function that create folder
def create_targetfile(source):
    projects = find_project_no(source)
    #print(projects)
    for project in projects:
        os.makedirs(os.path.join(source,project),exist_ok=True)
        
##Function that moves the files from source to projectNO folders
def move_files(source):
    files=[]
    folders=[]
    for file in os.listdir(source):
        get_file_type = file.split('.')
        #print(len(get_file_type))
        if len(get_file_type) == 2:
            files.append(file)
        else:
            folders.append(file)
        #print(files)
        #print(folders)
    for file in files:
        get_projectNO = file.split('-')[1]
        create_source_path = os.path.join(source,file)
        create_target_path = os.path.join(source,get_projectNO,file)
        shutil.move(create_source_path,create_target_path)

##Function that generalizes the move_files for any file with the spesiffic format
def manage_files_in_folder(userChoice):
    #print(os.getcwd())
    #path=os.path.join(os.getcwd())
    
    path = os.path.join(os.getcwd(),userChoice)
    create_targetfile(path)
    move_files(path)
##Function that split by folder type from main file
def list_of_extensions(source):
    os.chdir(source)
    ex_list=[]
    for file in os.listdir():
        ex=file.split('.')
        if len(ex)==2:
            ex_list.append(ex[-1])
    return ex_list



def create_extension_files(source):
    ex_list=list_of_extensions(source)
    for ex in ex_list:
        os.makedirs(os.path.join(source,ex),exist_ok=True)
    
        


def move_files_to_extension(source):
    files=[]
    folders=[]
    try:
        for file in os.listdir(source):
            for ex in list_of_extensions(source):
                get_file_type = file.split('.')
                    #print(len(get_file_type))
                if len(get_file_type) == 2:
                    files.append(file)
                else:
                    folders.append(file)
                #print(files)
                #print(folders)
            
            get_file_type = file.split('.')[-1]
            create_source_path = os.path.join(source,file)
            create_target_path = os.path.join(source,str(get_file_type)+'\\'+file)
            print(create_target_path)
            shutil.copy(create_source_path,create_target_path)
    except:
        pass
def main():
    #1st sort the new entries
    ##The app should be in the same folder as database
    path=os.getcwd()
    create_extension_files(path)
    move_files_to_extension(path)
    userChoices = unique(list_of_extensions(path))
    for userChoice in userChoices:
        manage_files_in_folder(userChoice)
    #move_files(path)
    
if __name__=='__main__':
    main()
    