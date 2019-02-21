import os, shutil, glob

src_fldr = "C:/Users/Deodat/Desktop/Metermate_v1.0/Database/Input" ## Edit this

dst_fldr = "C:/Users/Deodat/Desktop/Metermate_v1.0/Database/Archive" ## Edit this

try:
  os.makedirs(dst_fldr) ## it creates the destination folder
except:
  print ("Folder already exist or some error")


for txt_file in glob.glob(src_fldr+"\\*.txt"):
    print(txt_file)
    shutil.move(txt_file,dst_fldr)







# import os
#
# folder = "C:\\Users\\Deodat\\Desktop\Metermate_v1.0\\Database\\Input"
#
# for file in os.listdir(folder):
#     #print(file)
#     filepath = os.path.join(folder,file)
#     f = open(filepath,'r')
#     print(f.read())
#     os.rename("C:/Users/Deodat/Desktop/Metermate_v1.0/Database/Input", "C:/Users/Deodat/Desktop/Metermate_v1.0/Database/Archive")
#     f.close()
