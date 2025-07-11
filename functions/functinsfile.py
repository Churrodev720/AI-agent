import os.path
from functions.config import MAX_CHARS

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
    v = os.path.abspath(working_directory)
    l = os.listdir(path=f'{working_directory}')
    mel = f"{v}/{file_path}" 
    pow = os.path.isfile(mel)
    
    count = 0
    for i in l:
        if mel.startswith(i) == True:
            count += 1
        
    if count >= 1:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if pow == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    with open(mel, "r") as f:
        test = f.read()
        file_content_string = test[0:MAX_CHARS]
            
        if len(test) > MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
                
        return file_content_string
    

def write_file(working_directory, file_path, content):
    v = os.path.abspath(working_directory)
    l = os.listdir(path=f'{working_directory}')
    mel = f"{v}/{file_path}" 
    #pow = os.path.isfile(mel)
    
    count = 0
    if file_path[0] == "/":
            return f"Error: file path {file_path} has a '/' at the beginning"
    for i in l:
        if mel.startswith(i) == True:
            count += 1
        
    if count >= 1:
        fel = os.path.dirname(file_path)
        tel = f"{v}/{fel}"
        if os.path.exists(tel) == False:
            os.makedirs(tel, exist_ok=True)
            
        
        
    
    #if pow == True:
    #    return f'Error: File already exists: "{file_path}"'
   
    
    
    with open(mel, 'w') as file:
        file.write(f"{content}")
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    
def run_python_file(working_directory, file_path):
     pass 