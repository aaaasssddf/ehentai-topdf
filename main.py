import os
import os.path
import zipfile
import img2pdf
import shutil

#./zips --放置压缩源文件
#./temp --临时文件夹
#./output --输出pdf文件夹

zipfiles=os.listdir(os.getcwd()+"\\zips")
temppath=os.getcwd()+"\\temp"
#解压文件夹
for file in zipfiles:
    print(file)
    out=zipfile.ZipFile(os.getcwd()+"\\zips\\"+str(file),"r")
    out.extractall(temppath+"\\"+str(file).replace(".zip",""))
    out.close()
    
    
temps=os.listdir(os.getcwd()+"\\temp")
#将解压后的图片合成pdf
for folder in temps:
    name=str(folder)
    if os.path.isdir(temppath+"\\"+folder)==True:
        tempfolder=os.listdir(temppath+"\\"+folder)
        for imagefolder in tempfolder:
            with open(os.getcwd()+"\\output\\"+name+".pdf","wb") as f:
                imgs=[]
                for image in os.listdir(temppath+"\\"+folder+"\\"+imagefolder):
                    if image.endswith(".jpg") or image.endswith(".png"):
                        imgs.append(temppath+"\\"+folder+"\\"+imagefolder+"\\"+image)
                imgs.sort(key=lambda x:os.stat(x).st_ctime_ns)                
                f.write(img2pdf.convert(imgs))
                f.close()

shutil.rmtree(temppath)
os.mkdir(temppath)

  
    
    