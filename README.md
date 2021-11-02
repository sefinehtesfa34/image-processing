# image-processing
import  cv2 as cv
import numpy as np
#intial image
initial_image=cv.imread("C:\\Users\\tesfasefineh34\\Desktop\\sefinehD\\__pycache__\\FOLDER\\image.jpg")
#show the initial_image image
cv.imshow("Initial image",initial_image)
#Write some text on the image
put_text_on_image=cv.putText(initial_image,text="Welcome to github",org=(0,100),fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,255,100),thickness=2)
cv.imshow("put text on image",put_text_on_image)
#color change
initial_image=cv.cvtColor(initial_image,cv.COLOR_BGR2RGB)
#initialized a blank_image
blank_image=np.zeros(initial_image.shape,dtype=np.uint8)
#show the blank_image image
cv.imshow("blank",blank_image)
#resized the initial_image
resized_image=cv.resize(initial_image,(0,0),fx=0.5,fy=0.5)
#show the resized_image image
cv.imshow("resized image",resized_image)
#show the shape of the resized_image image of the initial image
print(resized_image.shape)
#By array slicing method, initialize 
# the sliced array with the resized_image image
#Bear in mind!--->The shape of the sliced blank_image image 
# must be equal to the shape of the resized_image image
blank_image[:initial_image.shape[0]//2,:initial_image.shape[1]//2]=resized_image
blank_image[:initial_image.shape[0]//2,initial_image.shape[1]//2+1:]=resized_image
blank_image[initial_image.shape[0]//2+1:,:initial_image.shape[1]//2]=resized_image
blank_image[initial_image.shape[0]//2+1:,initial_image.shape[1]//2+1:]=resized_image
#Check whether the shapes of 
# the sliced blank_image image 
# is congruent to the resized_image image.
print(blank_image[:initial_image.shape[0]//2,:initial_image.shape[1]//2].shape)
print(blank_image[:initial_image.shape[0]//2,initial_image.shape[1]//2+1:].shape)
print(blank_image[initial_image.shape[0]//2+1:,:initial_image.shape[1]//2].shape)
print(blank_image[initial_image.shape[0]//2+1:,initial_image.shape[1]//2+1:].shape)
cv.imshow("The fourth quadrant edited image",blank_image)
saved_edited_image=cv.imwrite("C:\\Users\\tesfasefineh34\\Desktop\\sefinehD\\__pycache__\\FOLDER\\Fouth_quadrant_edited_image.jpg",blank_image)
print(saved_edited_image)
#Wait after desplayed the image until some one pressed any key 
# in a keyboard where the python code runs
cv.waitKey(0)
