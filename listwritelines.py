import os

#jpg file name 가져오기
path = "./"
file_list = os.listdir(path)
file_list.sort()
file_list_jpg = [file for file in file_list if file.endswith(".jpg")]


#print
'''print ("file_list_jpg: {}".format(file_list_jpg))'''


#txt파일로 작성
def write_txt(list, flist, sep):
    file = open(flist, 'w')
    vstr =''

    for a in list:
        vstr = vstr + str(a) + sep
    vstr = vstr.rstrip(sep)

    file.writelines(vstr)
    file.close()
