import  os

def rename():
    path = ".";

    fileList = os.listdir(path)
    for file in fileList:
        olddir = os.path.join(path,file);
        if(os.path.isdir(olddir)):
            continue;
        fileName = os.path.splitext(file)[0];
        fileType = os.path.splitext(file)[1];
        newDir = os.path.join(path,fileName+fileType[0:-1]);
        os.rename(olddir,newDir);

rename();
