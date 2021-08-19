#importing
import cv2
import pandas as pd


#importing image and resizing
img_path=r'image.jpg'
img=cv2.imread(img_path)
img=cv2.resize(img,(700,500))

#variables 
clicked=False
r=g=b=x_pos=y_pos=0

index=["color","color_name","hex","R","G","B"]

#importing colors daataset
csv=pd.read_csv('colors.csv',names=index,header=None)

#Defining functions

#Function to get the name of the color
def get_name(R,G,B):
    mini=10000
    for i in range(len(csv)):
        dis=abs(R-int(csv.loc[i,"R"]))+abs(G-int(csv.loc[i,"G"]))+abs(B-int(csv.loc[i,"B"]))
        if dis<=mini:
            mini=dis
            col_name=csv.loc[i,"color_name"]
    return col_name

#Getting color from the image on double clicking
def draw_fun(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,x_pos,y_pos,clicked
        clicked=True
        x_pos=x
        y_pos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_fun)

#mainloop
while True:
    cv2.imshow("image",img)
    if clicked:
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text=get_name(r,g,b)+'R='+str(r)+'G='+str(g)+'B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False

    if cv2.waitKey(20) & 0xFF==27:
        break

cv2.destroyAllWindows()



       
