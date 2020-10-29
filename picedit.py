import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def change_brightness(image, value):

    img = image.copy()
    change = int(value)
    img = img + change
    img = np.where(img > 255, 255, img) #uses the np.where function - I found this online lmao
    img = np.where(img < 0, 0, img)
    
    #attempt no.1 at replacing values 
    #for x in image: 
    #    for y in x:
    #        for z in y:
    #            if z > 255:
    #                img[enumerate(img[z])] = 255
    #            if z < 0:
    #                img[enumerate(img[z])] = 0
    return img

    
    # return np.array([]) # to be removed when filling this function

  
def change_contrast(image, value):
    img = image.copy()
     
    F = (259 * (value+255)) / (255*(259-value))  
     
    for r in range(len(img)):
        for c in range(len(img[0])):
            
            R = img[r][c][0]
            R_new=F*(R-128) + 128
            img[r][c][0] = R_new
           
            G= img[r][c][1]
            G_new=F*(G-128) + 128 
            img[r][c][1] = G_new
            
            B= img[r][c][2]
            B_new= F*(B-128) + 128
            img[r][c][2]=B_new
    
    img = np.where(img > 255, 255, img) 
    img = np.where(img < 0, 0, img)
     
    return img

def grayscale(image):
    img = image.copy()
    
    for r in range(len(img)):
        for c in range(len(img[0])):
            
            R= img[r][c][0]
            G= img[r][c][1]
            B= img[r][c][2]
            
            img[r][c][0] = (0.3*R + 0.59*G + 0.11*B)
            img[r][c][1] = (0.3*R + 0.59*G + 0.11*B)
            img[r][c][2] = (0.3*R + 0.59*G + 0.11*B)
            
    img = np.where(img > 255, 255, img) 
    img = np.where(img < 0, 0, img)
    
    return img
            

def blur_effect(image):
    return np.array([]) # to be removed when filling this function

def edge_detection(image):
    return np.array([]) # to be removed when filling this function

def embossed(image):
    return np.array([]) # to be removed when filling this function

def rectangle_select(image, x, y):
    img = image.copy()
    r1 = x[0]
    c1 = x[1]
    r2 = y[0]
    c2 = y[1]

        
        
    #for r in range(len(img)):
    #    for c in range(len(img[0])):
    

    return np.array([]) # to be removed when filling this function

def magic_wand_select(image, x, thres):                
    return np.array([]) # to be removed when filling this function

def compute_edge(mask):           
    rsize, csize = len(mask), len(mask[0]) 
    edge = np.zeros((rsize,csize))
    if np.all((mask == 1)): return edge        
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c]!=0:
                if r==0 or c==0 or r==len(mask)-1 or c==len(mask[0])-1:
                    edge[r][c]=1
                    continue
                
                is_edge = False                
                for var in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0<=r_temp<rsize and 0<=c_temp<csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break
    
                if is_edge == True:
                    edge[r][c]=1
            
    return edge

def save_image(filename, image):
    img = image.astype(np.uint8)
    mpimg.imsave(filename,img)

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    mask = np.ones((len(img),len(img[0]))) # create a mask full of "1" of the same size of the laoded image
    img = img.astype(np.int32)
    return img, mask

def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0]=255
                tmp_img[r][c][1]=0
                tmp_img[r][c][2]=0
 
    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))

def menu():
    img = mask = np.array([])
    u = 0
    choice = 0
    flag = 1 
    while img.size == 0 or mask.size == 0 or flag == 1:
        while u != 'e' or u != 'l':
            u = input("What do you want to do ?\n"
                      "                e - exit\n"
                      "                l - load a picture\n"
                      "                Your choice:")
            if u == "e":
                    return
            elif u == "l":
                    filename = input("Enter filename here: ")
                    img, mask = load_image(filename)
                    flag = 0
                    break
            else:
                    u = input("Error: insert a valid choice\n"
                              "What do you want to do ?\n"
                              "                    e - exit\n"
                              "                    l - load a picture\n"
                              "                    Your choice:")  
    else:
        while choice != 'e' or choice != 'l' or  choice != 's' or  choice != '1' or choice != '2' or choice != '3' or choice != '7': 
            display_image(img, mask)
            choice = input("What do you want to do ?\n"
                          "            e - exit\n"
                          "            l - load a picture\n"
                          "            s - save the current picture\n"
                          "            1 - adjust brightness\n"
                          "            2 - adjust contrast\n"
                          "            3 - apply grayscale\n"
                          "            4 - apply blur\n"
                          "            5 - edge detection\n"
                          "            6 - embossed\n"
                          "            7 - rectangle select\n"
                          "            8 - magic wand select\n"
                          "            Your choice:")
            if choice == "e":
                return
            elif choice == "l":
                filename = input("Enter filename here: ")
                img, mask = load_image(filename)
            elif choice == 's':
                filename = input("Enter filename to save image with:")
                save_image(filename, img)
            elif choice == '1':
                value = int(input("Enter brightness change:"))
                while value > -255 and value < 255:
                    img = change_brightness(img, value)
                    break
                else:
                    print("Please enter a value between -255 to 255")
                    value = int(input("Enter brightness change:"))
            elif choice == '2':
                value = int(input("Enter contrast change:"))
                while value > -255 and value < 255:
                    img = change_contrast(img, value)
                    break
                else:
                    print("Please enter a value between -255 to 255")
                    value = int(input("Enter brightness change:"))
            elif choice == '3':
                img = grayscale(img)
            elif choice == '7':
                 x1, x2 = input("Enter the coordinates for the top-left most pixel of the mask: ").split(',')
                 y1, y2 = input("Enter the coordinates for the bottom-right most pixel of the mask: ").split(',')
                 while x2 + y2 < len(img) or x2 + y2 < len(img[0]):
                     top_left = list[x1, x2]
                     bottom_right = list[y1, y2]
                     rectangle_select(img, top_left, bottom_right)
                 else:
                     print("Error: the defined limits exceed the size of the image! Please Retry.")
                     x1, x2 = input("Enter the coordinates for the top-left most pixel of the mask: ").split(',')
                     y1, y2 = input("Enter the coordinates for the bottom-right most pixel of the mask: ").split(',')
            else:
                choice = input("Error - invalid choice, please retry:")


if __name__ == "__main__":
    menu()












