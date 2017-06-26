import  os

path = ".";

def recursion(path):
    fileList = os.listdir(path)
    for file in fileList:
        fi_d = os.path.join(path, file);
        if (os.path.isdir(fi_d)):
            recursion(fi_d);
        else:
            rename(fi_d);


def rename(file):
    fileName = os.path.splitext(file)[0];
    fileType = os.path.splitext(file)[1];
    newFile = os.path.join(path,fileName+fileType[0:-1]);
    os.rename(file,newFile);

rename();
