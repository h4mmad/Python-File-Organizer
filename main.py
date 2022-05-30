import os
import shutil
import uuid
from datetime import datetime

def get_unique_file(file):
    new_file = file.split('.')
    new_file.insert(-1, str(uuid.uuid4()))
    new_file = '.'.join(new_file)
    return new_file

#directories to send the files to, create the directories if they do not exist
target_dir = "C:/Users/Hammad/Downloads/"
target_dir_contents = os.listdir(target_dir)

pictures_dir = "Pictures/"
docs_dir = "Documents/"
videos_dir = "Videos/"
audio_dir = "Audios/"
other_dir = "Other Files/"

if not os.path.isdir(os.path.join(target_dir, pictures_dir)):
    os.mkdir(os.path.join(target_dir, pictures_dir))
    print("Pictures directory created")
if not os.path.isdir(os.path.join(target_dir, docs_dir)):
    os.mkdir(os.path.join(target_dir, docs_dir))
    print("Documents directory created")
if not os.path.isdir(os.path.join(target_dir, videos_dir)):
    os.mkdir(os.path.join(target_dir, videos_dir))
    print("Videos directory created")
if not os.path.isdir(os.path.join(target_dir, audio_dir)):
    os.mkdir(os.path.join(target_dir, audio_dir))
    print("Audio directory created")
if not os.path.isdir(os.path.join(target_dir, other_dir)):
    os.mkdir(os.path.join(target_dir, other_dir))
    print("Other directory created")


# filters between files and directories
dirs_list = []
files_list = []

for x in target_dir_contents:
    if os.path.isdir(os.path.join(target_dir, x)):
        dirs_list.append(x)
        
    if os.path.isfile(os.path.join(target_dir, x)):
        files_list.append(x)


#Moving files into their respective directories
#Check if a file with the same name is present in the directory to be moved, if found, then append the file with a uuid and then move
for file in files_list:
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        if os.path.isfile(os.path.join(target_dir, pictures_dir, file)):
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, pictures_dir, get_unique_file(file)))
        else:
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, pictures_dir, file))

    elif file.lower().endswith(('.pdf', '.docx', '.txt', '.doc', '.pptx', '.xlsx')):
        if os.path.isfile(os.path.join(target_dir, docs_dir, file)):
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, docs_dir, get_unique_file(file)))
        else:
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, docs_dir, file))

    elif file.lower().endswith(('.mp4', '.mov', '.mkv', '.wmv')):
        if os.path.isfile(os.path.join(target_dir, videos_dir, file)):
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, videos_dir, get_unique_file(file)))
        else:
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, videos_dir, file))

    elif file.lower().endswith(('.mp3', '.m4a', '.wma', '.flac', '.aac')):
        if os.path.isfile(os.path.join(target_dir, audio_dir, file)):
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, audio_dir, get_unique_file(file)))
        else:
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, audio_dir, file))

    else:
        if os.path.isfile(os.path.join(target_dir, other_dir, file)):
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, other_dir, get_unique_file(file)))
        else:
            shutil.move(os.path.join(target_dir, file), os.path.join(target_dir, other_dir, file))