import glob
import codecs
import random
import os
import string
import math
from shutil import copyfile

LIST_OF_EXTEN = ('jpg','jpeg','gif','png','tiff')
list_to_copy = []
list_of_names = []

random.seed()
cur_dir = os.getcwd()

amount = input("How many? ")

if os.path.exists(cur_dir + "/Randomized"):    #cheking and creating folder
    pass
else:
    os.mkdir(cur_dir + "/Randomized")


names_dic_path = "/dic.txt"
names_dic_path = cur_dir + names_dic_path


for exten in LIST_OF_EXTEN:    #listing files
    path_to_list = glob.glob("".join(["**/*.",exten]),recursive=True)
    for in_put in path_to_list:
        list_to_copy.append(in_put)

if amount.isdigit():    #interpreting amount
    amount = int(amount)
    if amount<=len(list_to_copy):
        print(' '.join(("Will copy",str(amount),"files")))
    else:
        amount = len(list_to_copy)
        print("You have no this many files! Will copy all that you have.")
elif amount == "all" or amount == "All":
     amount = len(list_to_copy)
     print("Will copy all that you have.")
else:
    amount = 5
    print("Cant understand, will copy only five.")

if os.path.exists(names_dic_path):     #cheking dictionary existance, reading it and generating appropriate names list
    with codecs.open(names_dic_path,encoding="utf-8") as names_dic_source:
        names_dic = names_dic_source.readlines()
        names_dic = [line.rstrip() for line in names_dic]

    j = 0
    while j <= amount:
        for i in range (1,5):
            ran_name ="_".join(random.sample(names_dic,4))
        ran_suf = random.randrange(1,999,1)
        ran_name='_'.join((ran_name,str(ran_suf)))
        if ran_name in list_of_names:
            continue
        else:
            j += 1
            list_of_names.append(ran_name)
    input("Naming by dic")

else:   #generating name from scratch
    j = 0
    name_len = round(math.log(amount,len(string.ascii_letters+string.digits)))+ 1    #defining minimal reqired length
    while j <= amount:
        ran_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(name_len))
        if ran_name in list_of_names:
            continue
        else:
            list_of_names.append(ran_name)
            j += 1
    input("Naming by generator")

list_to_copy=random.sample(list_to_copy,amount)    #cutting down list to copy
counter = -1 
for file_name in list_to_copy:    #copying files
    counter += 1
    print("File " + file_name  )
    exten = file_name [-4:]
    exten = exten.replace(".","")
    out_put="".join([cur_dir,"/Randomized","/",list_of_names[counter],".",str(exten)]) 
    copyfile(file_name,out_put)
    print("has bean sucksexfully stripped of any regalia, shamed, stigmatized as lunatic, renamed and copied as " + out_put)