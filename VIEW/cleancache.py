import shutil
import os

def cleancache():

    dircache = [os.getcwd()+r'/VIEW/__pycache__',os.getcwd()+r'/CONTROLLER/__pycache__',os.getcwd()+r'/MODEL/__pycache__']
    #Ali em cima é uma lista com os diretorios com cache
    for dir in dircache:
        
        try:
            
            shutil.rmtree(dir) #remove diretorio

        except:
            
            pass

