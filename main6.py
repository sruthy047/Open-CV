import os
import cv2
from PIL import Image
os.chdir("E:/Sruthi/Open CV/Lesson 6/images")
path="E:/Sruthi/Open CV/Lesson 6/images"

mean_height=0
mean_width=0
image_files=[file for file in os.listdir('.') if file.endswith(('.jpg', '.jpeg', '.png'))]
num_of_images=len(os.listdir("."))
print(num_of_images)

for file in image_files:
    img=Image.open(os.path.join(path,file))
    width,height=img.size
    mean_width=mean_width+width
    mean_height=mean_height+height

mean_width=mean_width//num_of_images
mean_height=mean_height//num_of_images

print(mean_width)
print(mean_height)

for file in image_files:
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img=Image.open(os.path.join(path,file))
        width,height=img.size
        print(width,height)

        imgResized=img.resize((mean_width,mean_height),Image.Resampling.LANCZOS)
        imgResized.save(file,'JPEG',quality=95)
        print(img.filename.split('\\')[-1]," is resized")

def videoGenerator():
    video_name="MyFirstVideo.avi"

    os.chdir("E:/Sruthi/Open CV/Lesson 6/images")
    #images = [img for img in os.listdir('.') if img.endswith(('.jpg', '.jpeg', '.png'))]
    images=[]
    for img in image_files:
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)
    print(images)

    frame = cv2.imread(os.path.join(".",images[0]))
    #frame = cv2.imread(images[0])
    height,width,layers=frame.shape
    video=cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'XVID'),1,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    cv2.destroyAllWindows()
    video.release()

videoGenerator()
        
