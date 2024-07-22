import cv2
import numpy as np
import pyautogui
import keyboard
import time
import PIL

pyautogui.PAUSE = 0

left_log_img = cv2.imread("Left_log.png") # 335,650-> 450,680
left_log = left_log_img[650:675,335:450]


right_log_img = cv2.imread("Right_log.png")
right_log = right_log_img[650:675,535:625] #535 , 625


def augmentation_large(image):
    
    img = np.array(image)
    
    img.shape #(1080, 1920, 3)
    
    img = img[500:650,330:650]
    
    img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
#     cv2.imshow("screenshot", img)
#     if cv2.waitKey(1) == ord('q'):
#         cv2.destroyAllWindows()
    
    return img

go_right = 0
go_left = 1
    
def dodge(side):

    if side == go_right:
        # press right  625, 650
        pyautogui.click((550, 500))
    if side == go_left:
        # press left    335,650
        pyautogui.click((335,500))
        
        
threshold = 0.5
motion = go_right
num = 0
print("press s to start")
keyboard.wait("s")
while True:
    num+=1
    time.sleep(0.02)
    img = PIL.ImageGrab.grab()
    img = augmentation_large(img)
    

    #template matching

#     save_imgs()
#     print(left_match.max())
#     print(right_match.max())

    if motion == go_left:
        left_img = img [:,: int(img.shape[1]/2)]
        left_match = cv2.matchTemplate(left_img , left_log , cv2.TM_CCOEFF_NORMED)
        
        if left_match.max() > threshold:
            #press right

            motion = go_right
            
            
    if motion == go_right:
        right_img = img [:, int(img.shape[1]/2):]
        right_match = cv2.matchTemplate(right_img, right_log , cv2.TM_CCOEFF_NORMED)

        if right_match.max() > threshold:
            #press left
            motion = go_left
        
    dodge(motion)

    


    if keyboard.is_pressed("q"):
        break
    
    
