import cv2

source = "tom.jpg"
destination = "NewImage.jpeg"  
#can change formate jpeg, jpg, png the file will be made according to the formate given

scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow('title', src)
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)
output = cv2.resize(src, (new_width, new_height))
cv2.imwrite(destination, output)
# cv2.waitKey(0) 
