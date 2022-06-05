import os
from datetime import datetime
import shutil
import requests  # allow code to make http requests
import threading


def get_pic(name,d1 = 0,d2=0):
    image_url = "https://source.unsplash.com/3840x2160/?random"
    if(name):
        image_url = "https://source.unsplash.com/384{}x216{}/?{}".format(d1,d2,name)
    print(image_url)
    # print("Generator : "+date_time)
    response = requests.get(image_url, stream=True)
    image_name = str((10*d1)+d2)+name+"_" + current_time + ".jpg"
    # print("Generator : "+image_name)
    file = open(image_name, "wb")
    response.raw_decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


if __name__ == "__main__":
    a = input("Image Name : ")
    # Directory
    now = datetime.now()

    current_time = now.strftime("%d%M%Y%H%M%S")
    directory = a+'_'+current_time
    
    # Parent Directory path
    parent_dir = "./"
    
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print(os. getcwd())
    print("Directory '% s' created" % directory)
    os.chdir(directory)
    print(os. getcwd())

    # creating thread
    tot=10
    for i in range(tot):
        t = threading.Thread(target=get_pic, args=(a,i//10,i%10))
        t.start()
    print("Done!")


