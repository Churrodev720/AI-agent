import os.path

def get_files_info(working_directory, directory=None):
    
    l = os.listdir(path=f'{working_directory}')
    f = os.path.abspath(directory)
    v = os.path.abspath(working_directory)
    mel = f"{v}/{directory}"    
    
    if directory == None:
        size = os.path.getsize(working_directory)
        boo = os.path.isdir(working_directory)
        borus = ""
        borus += f"- {working_directory}: file_size={size} bytes, is_dir={boo}  {l}\n"
        
        fun = os.path.abspath(working_directory)
        
        for word in l:
            rel = f"{fun}/{word}"
            size = os.path.getsize(rel)
            boo = os.path.isdir(rel)
            borus += f"- {word}: file_size={size} bytes, is_dir={boo}\n"
        
        return borus
    
    if directory not in l:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory {f} {v}'
    
    if os.path.isdir(mel) == False and os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory is_dir=False'
    
    try:
        jel = os.listdir(path=f'{mel}')
        size = os.path.getsize(mel)
        boo = os.path.isdir(mel)
    except:
        raise FileNotFoundError("No file")
        
    borus = ""
    borus += f"- {working_directory}: file_size={size} bytes, is_dir={boo}  {l}\n"
    borus += f"- {directory}: file_size={size} bytes, is_dir={boo}  {jel}\n"
    
    fun = os.path.abspath(mel)
    
    for word in jel:
        rel = f"{fun}/{word}"
        try:
            size = os.path.getsize(rel)
            boo = os.path.isdir(rel)
        except:
            raise FileNotFoundError("No file")
        borus += f"- {word}: file_size={size} bytes, is_dir={boo}\n"
        
    
    return borus



def get_file_content(working_directory, file_path):
    l = os.listdir(path=f'{working_directory}')
    
    if file_path not in l:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    