from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
import cv2
import numpy as np
import os
import PIL
from random import choice


def random_color():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code='#'
    for i in range(0,6):
        colour_code+=choice(hex_chars)
    return colour_code



tags=[]
Draw_temp_box=False
img_box=Image
video_chosen = False
LARGE_FONT = ("Verdana", 42)
videopath=''
myFrameNumber = 0
root=Tk()
myFrameNumber=0
jumpframes=5
root.configure(background='#b5ebeb')
videodims=[1000,1000]
left_clicked=False
left_hold=False
tag_count=0
start_box=[0,0]
end_box=[0,0]
defined_boxes=[]
fullscreen=True
tag_names=['']*40
tag_colors=['']*40
active_tag=-1
counter1=0
counter2=0
project_has_file=0
save_file_path=''
save_file_name=''
image_counts=[0]*40

jumpframesText= Text( root, height=1, width=4, font=LARGE_FONT)
jumpframesText.place(x=895,y=300)
jumpframesText.insert(END, "5")

label1 = Label( text="Jumped Frames Per Image",font=LARGE_FONT)
label1.place(x=590,y=150)

choosevideo = Button( command=lambda: choose_video(), text="Choose Video", height=20, width=30)
choosevideo.place(x=860, y=390)

Load_Data_Button =  Button( command=lambda: Load_Project(), text="Load Data", height=10, width=15)
Load_Data_Button.place(x=100,y=390)


def choose_video():
    global cap,jumpframes, videodims, video_chosen, frame_tracker, AddTagText, button_tag1,button_tag2,button_tag3,button_tag4,\
        button_tag5,button_tag6,button_tag7,button_tag8,button_tag9,button_tag10,button_tag11,button_tag12,button_tag13,button_tag14,button_tag15,\
        button_tag16,button_tag17,button_tag18,button_tag19,button_tag20,button_tag21,button_tag22,button_tag23,button_tag24,button_tag25,\
        button_tag26,button_tag27,button_tag28,button_tag29,button_tag30,button_tag31,button_tag32,button_tag33,button_tag34,button_tag35, \
        button_tag36,button_tag37,button_tag38,button_tag39,button_tag40,Save_textbox,save_file_name

    jumpframes=int(jumpframesText.get("1.0",END))
    filename = filedialog.askopenfilename(initialdir=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), title="Select A File", filetype=
    ( ("all files", "*.*"),("jpeg files", "*.jpg")))

    choosevideo.destroy()
    jumpframesText.destroy()
    label1.destroy()

    videopath=filename
    cap = cv2.VideoCapture(videopath)
    ret, img = cap.read()
    videodims[0]=(img.shape[1])
    videodims[1]=(img.shape[0])
    print(videodims)
    video_chosen=True

    Load_Data_Button.destroy()

    if(project_has_file==True):
        Save_label = Label(root,text=save_file_name, height=1, width=25, font=('Verdana', 12))
        Save_label.place(x=500, y=932)

        Tagged_photo_save_button = Button(command=lambda: Save_Images(), text='Save Images So Far', wraplength=200,
                                          justify=LEFT, height=3,
                                          width=18, font=('Verdana', 12, 'bold'))
        Tagged_photo_save_button.place(x=500, y=860)
    else:
        Save_textbox = Text(root, height=1, width=25, font=('Verdana', 12))
        Save_textbox.place(x=500, y=940)


    NextButton = Button(command=lambda: Next_frame(), text="Next Frame", height=4, width=15)
    NextButton.place(x=1150, y=900)

    PreviousButton = Button(command=lambda: Previous_frame(), text="Previous Frame", height=4, width=15)
    PreviousButton.place(x=950, y=900)

    frame_tracker = Label(root, font=LARGE_FONT, text=myFrameNumber,bg='#b5ebeb')
    frame_tracker.place(x=1600, y=10)

    tag_button= Button(command=lambda: create_tag(), text="Add Tag", height=3, width=9,font=('Verdana',15,'bold'))
    tag_button.place(x=10,y=950)

    AddTagText = Text(root, height=1, width=16, font=('Verdana',12))
    AddTagText.place(x=10, y=940)

    button_tag1 = Button(command=lambda: activate_tag(1), text=tag_names[0], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag1.place(x=1320,y=100)
    button_tag2 = Button(command=lambda: activate_tag(2), text=tag_names[1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag2.place(x=1320, y=145)
    button_tag3 = Button(command=lambda: activate_tag(3), text=tag_names[2], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag3.place(x=1320, y=190)
    button_tag4 = Button(command=lambda: activate_tag(4), text=tag_names[3], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag4.place(x=1320, y=235)
    button_tag5 = Button(command=lambda: activate_tag(5), text=tag_names[4], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag5.place(x=1320, y=280)
    button_tag6 = Button(command=lambda: activate_tag(6), text=tag_names[5], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag6.place(x=1320, y=325)
    button_tag7 = Button(command=lambda: activate_tag(7), text=tag_names[6], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag7.place(x=1320, y=370)
    button_tag8 = Button(command=lambda: activate_tag(8), text=tag_names[7], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag8.place(x=1320, y=415)
    button_tag9 = Button(command=lambda: activate_tag(9), text=tag_names[8], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag9.place(x=1320, y=460)
    button_tag10 = Button(command=lambda: activate_tag(10), text=tag_names[9], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag10.place(x=1320, y=505)
    button_tag11 = Button(command=lambda: activate_tag(11), text=tag_names[10], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag11.place(x=1320, y=550)
    button_tag12 = Button(command=lambda: activate_tag(12), text=tag_names[11], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag12.place(x=1320, y=595)
    button_tag13 = Button(command=lambda: activate_tag(13), text=tag_names[12], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag13.place(x=1320, y=640)
    button_tag14 = Button(command=lambda: activate_tag(14), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag14.place(x=1320, y=685)
    button_tag15 = Button(command=lambda: activate_tag(15), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag15.place(x=1320, y=730)
    button_tag16 = Button(command=lambda: activate_tag(16), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag16.place(x=1320, y=775)
    button_tag17 = Button(command=lambda: activate_tag(17), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag17.place(x=1320, y=820)
    button_tag18 = Button(command=lambda: activate_tag(18), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag18.place(x=1320, y=865)
    button_tag19 = Button(command=lambda: activate_tag(19), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag19.place(x=1320, y=910)
    button_tag20 = Button(command=lambda: activate_tag(20), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag20.place(x=1320, y=955)
    button_tag21 = Button(command=lambda: activate_tag(21), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag21.place(x=1620, y=100)
    button_tag22= Button(command=lambda: activate_tag(22), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag22.place(x=1620, y=145)
    button_tag23= Button(command=lambda: activate_tag(23), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag23.place(x=1620, y=190)
    button_tag24= Button(command=lambda: activate_tag(24), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag24.place(x=1620, y=235)
    button_tag25= Button(command=lambda: activate_tag(25), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                         width=22, font=('Verdana', 12,'bold'))
    button_tag25.place(x=1620, y=280)
    button_tag26 = Button(command=lambda: activate_tag(26), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag26.place(x=1620, y=325)
    button_tag27 = Button(command=lambda: activate_tag(27), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag27.place(x=1620, y=370)
    button_tag28 = Button(command=lambda: activate_tag(28), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag28.place(x=1620, y=415)
    button_tag29 = Button(command=lambda: activate_tag(29), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag29.place(x=1620, y=460)
    button_tag30 = Button(command=lambda: activate_tag(30), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag30.place(x=1620, y=505)
    button_tag31 = Button(command=lambda: activate_tag(31), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag31.place(x=1620, y=550)
    button_tag32 = Button(command=lambda: activate_tag(32), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag32.place(x=1620, y=595)
    button_tag33 = Button(command=lambda: activate_tag(33), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag33.place(x=1620, y=640)
    button_tag34 = Button(command=lambda: activate_tag(34), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag34.place(x=1620, y=685)
    button_tag35 = Button(command=lambda: activate_tag(35), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag35.place(x=1620, y=730)
    button_tag36 = Button(command=lambda: activate_tag(36), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag36.place(x=1620, y=775)
    button_tag37 = Button(command=lambda: activate_tag(37), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag37.place(x=1620, y=820)
    button_tag38 = Button(command=lambda: activate_tag(38), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag38.place(x=1620, y=865)
    button_tag39 = Button(command=lambda: activate_tag(39), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag39.place(x=1620, y=910)
    button_tag40 = Button(command=lambda: activate_tag(40), text=tag_names[-1], wraplength=200, justify=LEFT, height=1,
                          width=22, font=('Verdana', 12,'bold'))
    button_tag40.place(x=1620, y=955)


    Save_button = Button(command=lambda: Save_Project(), text='SAVE', wraplength=200, justify=LEFT, height=3,
                          width=9, font=('Verdana', 12,'bold'))
    Save_button.place(x=500, y=960)

    update_tag_buttons()




    TV()


def update_tag_buttons():
    global tag_names, AddTagText,tag_count,counter2
    counter2=0
    stop =update_tag_controller()
    if (stop == True): return
    button_tag1["text"]=tag_names[0]
    button_tag1["bg"] = tag_colors[0]
    stop=update_tag_controller()
    if(stop==True): return
    button_tag2["text"]=tag_names[1]
    button_tag2["bg"] = tag_colors[1]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag3["text"] = tag_names[2]
    button_tag3["bg"] = tag_colors[2]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag4["text"] = tag_names[3]
    button_tag4["bg"] = tag_colors[3]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag5["text"] = tag_names[4]
    button_tag5["bg"] = tag_colors[4]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag6["text"] = tag_names[5]
    button_tag6["bg"] = tag_colors[5]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag7["text"] = tag_names[6]
    button_tag7["bg"] = tag_colors[6]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag8["text"] = tag_names[7]
    button_tag8["bg"] = tag_colors[7]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag9["text"] = tag_names[8]
    button_tag9["bg"] = tag_colors[8]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag10["text"] = tag_names[9]
    button_tag10["bg"] = tag_colors[9]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag11["text"] = tag_names[10]
    button_tag11["bg"] = tag_colors[10]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag12["text"] = tag_names[11]
    button_tag12["bg"] = tag_colors[11]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag13["text"] = tag_names[12]
    button_tag13["bg"] = tag_colors[12]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag14["text"] = tag_names[13]
    button_tag14["bg"] = tag_colors[13]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag15["text"] = tag_names[14]
    button_tag15["bg"] = tag_colors[14]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag16["text"] = tag_names[15]
    button_tag16["bg"] = tag_colors[15]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag17["text"] = tag_names[16]
    button_tag17["bg"] = tag_colors[16]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag18["text"] = tag_names[17]
    button_tag18["bg"] = tag_colors[17]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag19["text"] = tag_names[18]
    button_tag19["bg"] = tag_colors[18]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag20["text"] = tag_names[19]
    button_tag20["bg"] = tag_colors[19]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag21["text"] = tag_names[20]
    button_tag21["bg"] = tag_colors[20]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag22["text"] = tag_names[21]
    button_tag22["bg"] = tag_colors[21]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag23["text"] = tag_names[22]
    button_tag23["bg"] = tag_colors[22]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag24["text"] = tag_names[23]
    button_tag24["bg"] = tag_colors[23]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag25["text"] = tag_names[24]
    button_tag25["bg"] = tag_colors[24]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag26["text"] = tag_names[25]
    button_tag26["bg"] = tag_colors[25]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag27["text"] = tag_names[26]
    button_tag27["bg"] = tag_colors[26]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag28["text"] = tag_names[27]
    button_tag28["bg"] = tag_colors[27]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag29["text"] = tag_names[28]
    button_tag29["bg"] = tag_colors[28]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag30["text"] = tag_names[29]
    button_tag30["bg"] = tag_colors[29]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag31["text"] = tag_names[30]
    button_tag31["bg"] = tag_colors[30]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag32["text"] = tag_names[31]
    button_tag32["bg"] = tag_colors[31]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag33["text"] = tag_names[32]
    button_tag33["bg"] = tag_colors[32]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag34["text"] = tag_names[33]
    button_tag34["bg"] = tag_colors[33]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag35["text"] = tag_names[34]
    button_tag35["bg"] = tag_colors[34]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag36["text"] = tag_names[35]
    button_tag36["bg"] = tag_colors[35]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag37["text"] = tag_names[36]
    button_tag37["bg"] = tag_colors[36]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag38["text"] = tag_names[37]
    button_tag38["bg"] = tag_colors[37]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag39["text"] = tag_names[38]
    button_tag39["bg"] = tag_colors[38]
    stop =update_tag_controller()
    if (stop == True): return
    button_tag40["text"] = tag_names[39]
    button_tag40["bg"] = tag_colors[39]

def update_tag_controller():
    global counter2
    if(tag_count==counter2):
        counter2=0
        return True
    else:
        counter2 += 1
        return False


def Save_Project():
    global Save_textbox, defined_boxes,tag_names,tag_colors,tag_count,project_has_file,save_file_path,save_file_name,image_counts
    if (project_has_file == True):
        pass
    else:
        save_name=Save_textbox.get("1.0",'end-1c')
        save_file_name=save_name
        Save_textbox.destroy()
        save_file_path=os.getcwd() + '/saves/'+save_name
        os.makedirs(save_file_path)
    savedata_path=save_file_path+'/save_data.txt'
    text=open(savedata_path,'w+')
    #--------------------------------
    text.write("%s\n" % str(defined_boxes))
    text.write("%s\n" % str(tag_names))
    text.write("%s\n" % str(tag_colors))
    text.write("%s\n" % str(tag_count))
    text.write("%s\n" % str(image_counts))
    text.close()
    #--------------------------------
    project_has_file=True

    Save_label = Label(root, text=save_file_name, height=1, width=25, font=('Verdana', 12))
    Save_label.place(x=500, y=932)

    Tagged_photo_save_button = Button(command=lambda: Save_Images(), text='Save Images So Far', wraplength=200,
                                      justify=LEFT, height=3,
                                      width=18, font=('Verdana', 12, 'bold'))
    Tagged_photo_save_button.place(x=500, y=860)
    TV()


def Load_Project():
    global defined_boxes,tag_names,tag_colors,tag_count, project_has_file,save_file_path,save_file_name,image_counts
    save_file_path = filedialog.askdirectory(initialdir=os.getcwd() +'/saves',title="Select Save Data")
    text = open(save_file_path+'/save_data.txt', 'r')
    save_file_name = Return_last_folder_of_path(save_file_path)
    lines = text.readlines()
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]
    defined_boxes = eval(lines[0])
    tag_names=eval(lines[1])
    tag_colors=eval(lines[2])
    tag_count=eval(lines[3])
    image_counts=eval(lines[4])
    print('Loaded Data: ----------------')
    print(defined_boxes)
    print(tag_names)
    print(tag_colors)
    print('Tag Count:',tag_count)
    print(image_counts)
    print('-----------------------------')

    project_has_file=True



def Return_last_folder_of_path(save_file_path):
    for i in range(0,len(save_file_path)):
        if(save_file_path[-i]=='/'):
            return save_file_path[1-i:]



def Save_Images():
    global tag_count,tag_names,defined_boxes,save_file_path,image_counts
    total_images_saved= sum(i for i in image_counts)
    print('Total images Found:',total_images_saved)
    if(os.path.exists(save_file_path+'/Images') == True):
        pass
    else:
        os.makedirs(save_file_path + '/Images')
    for i in range(total_images_saved,len(defined_boxes)):
        cur_tag_name=tag_names[defined_boxes[i][6]]

        cap.set(cv2.CAP_PROP_POS_FRAMES, defined_boxes[i][0])
        ret, img = cap.read()
        img = img[defined_boxes[i][2]:defined_boxes[i][4] , defined_boxes[i][1]:defined_boxes[i][3]]

        if (os.path.exists(save_file_path+'/Images/i_'+cur_tag_name) == True):
            image_counts[defined_boxes[i][6]] += 1
            print('file exists')
        else:
            os.makedirs(save_file_path+'/Images/i_'+cur_tag_name)
            image_counts[defined_boxes[i][6]]+=1
            print('file created')

        cv2.imwrite(save_file_path + '/Images/i_' + cur_tag_name + '/i_' + str(defined_boxes[i][6]) + '_' + str(image_counts[defined_boxes[i][6]])+'.png',img)
    total_images_saved_new=sum(i for i in image_counts)
    print('New images Saved:', total_images_saved_new-total_images_saved)




    Save_Project()



def Next_frame():
    global cap, myFrameNumber, frame_tracker

    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    if (totalFrames >= myFrameNumber+jumpframes):
        myFrameNumber += jumpframes
        print('Set frame',myFrameNumber)
        frame_tracker.destroy()
        frame_tracker = Label(root, font=LARGE_FONT, text=myFrameNumber)
        frame_tracker.place(x=1700, y=10)
        TV()

def Previous_frame():
    global cap, myFrameNumber, frame_tracker

    if(myFrameNumber-jumpframes>-1):
        myFrameNumber -= jumpframes
        print('Set frame', myFrameNumber)
        frame_tracker.destroy()
        frame_tracker=Label(root,font=LARGE_FONT,text=myFrameNumber)
        frame_tracker.place(x=1700,y=10)
        TV()


def create_tag():
    global AddTagText, tags, tag_names, tag_create_pos,tag_count,tag_colors
    tag_count+=1
    if (tag_count == 41):
        return
    tag_names[tag_count-1]=AddTagText.get("1.0",'end-1c')
    AddTagText.delete('1.0', END)
    tag_colors[tag_count-1]=random_color()
    update_tag_buttons()


def activate_tag(i):
    i-=1
    global active_tag, tags
    if(active_tag!=i):
    #---create tick-------
        active_tag=i
        for b in range(0,40):
            if(b<20):
                tick_pos=[1320,100+(b*45)]
            else:
                tick_pos = [1620, 100 + ((b-20) * 45)]
            if(active_tag!=b):
                img = Image.open(os.getcwd() + '/resources/x.png')
                img = ImageOps.fit(img, (40, 40), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(img)
                img = Label(root, image=render)
                img.image = render
                img.place(x=tick_pos[0] - 40, y=tick_pos[1])
            else:
                img = Image.open(os.getcwd()+'/resources/tick.png')
                img = ImageOps.fit(img, (40, 40), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(img)
                img = Label(root, image=render)
                img.image = render
                img.place(x=tick_pos[0]-40,y=tick_pos[1])
    TV()





    #---create tick----------



def rightKey(e):
    Next_frame()

def leftKey(e):
    Previous_frame()


def lefthold(e):
    global left_clicked, start_box, left_hold
    if(video_chosen==True and tag_colors[active_tag]!=''):
      if (e.x < videodims[0] and e.y < videodims[1]):
        if(left_clicked==False):
            start_box=[e.x,e.y]

        else:
            Draw_Box([e.x,e.y],tag_colors[active_tag])
        left_clicked=True
        left_hold = True
        TV()


def rightrelease(e):
    global defined_boxes
    if(video_chosen==True):
        for i in range(0,len(defined_boxes)):
            if(defined_boxes[i][0]==myFrameNumber):
                if(e.x<defined_boxes[i][3] and e.x>defined_boxes[i][1]):
                    if(e.y<defined_boxes[i][4] and e.y>defined_boxes[i][2]):
                        defined_boxes.pop(i)
                        TV()

def leftrelease(e):
   global end_box, left_clicked, Draw_temp_box, defined_boxes,cur_color, left_hold
   if (video_chosen == True and left_hold == True):
    left_hold=False
    kova=[]
    end_box=[e.x,e.y]
    Draw_Box(end_box,'#a26c1c')
    left_clicked=False
    Draw_temp_box=False
    #-------------------------
    if(abs(start_box[0]-end_box[0])*abs(start_box[1]-end_box[1])>180 and start_box[1]<end_box[1] and start_box[0]<end_box[0]):
        kova.append(myFrameNumber)
        kova.append(start_box[0])
        kova.append(start_box[1])
        kova.append(end_box[0])
        kova.append(end_box[1])
        kova.append(tag_colors[active_tag])
        kova.append(active_tag)
        defined_boxes.append(kova)

    #------------------------
    TV()


def Draw_Box(end_point,color):
    global cap, myFrameNumber, Draw_temp_box, img_box

    if (video_chosen == True):
        box_width = abs(end_point[0] - start_box[0])
        box_height = abs(end_point[1] - start_box[1])
        if(box_width*box_height<9):
            return
        img_box = Image.new('RGB', (60, 30), color=tag_colors[active_tag])
        img_box.putalpha(156)
        img_box = ImageOps.fit(img_box, (box_width,box_height), Image.ANTIALIAS)
        box_render = ImageTk.PhotoImage(img_box)
        img_box= box_render
        img_box.image= box_render
        Draw_temp_box=True
        TV()






def TV():
 global video_chosen,canvas,img_box,canvas_created, defined_boxes
 if video_chosen is True:
    cap.set(cv2.CAP_PROP_POS_FRAMES, myFrameNumber)
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    render = ImageTk.PhotoImage(img)
    img = Label(root, image=render)
    img.image = render


    canvas = Canvas(root, width=videodims[0], height=videodims[1])
    canvas.pack()
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor=NW, image=img.image)
    canvas_created=True
 if(Draw_temp_box==True):
    canvas.create_image(start_box[0], start_box[1], anchor=NW, image=img_box.image)

    #place defined boxes
 for box in defined_boxes:

    if(box[0]==myFrameNumber):
            box_width = abs(box[1] - box[3])
            box_height = abs(box[4] - box[2])
            img_box_defined = Image.new('RGB', (60, 30), color=box[5])
            img_box_defined.putalpha(156)
            img_box_defined = ImageOps.fit(img_box_defined, (box_width, box_height), Image.ANTIALIAS)
            box_render_defined = ImageTk.PhotoImage(img_box_defined)
            img_box_defined = box_render_defined
            img_box_defined.image = box_render_defined
            canvas.create_image(box[1], box[2], anchor=NW, image=img_box_defined.image)

def escape(e):
    global fullscreen
    fullscreen= not fullscreen
    root.attributes('-fullscreen',fullscreen)





root.attributes('-fullscreen',fullscreen)
root.bind("<Escape>",escape)
root.bind("<ButtonRelease-3>",rightrelease)
root.bind("<ButtonRelease-1>",leftrelease)
root.bind("<B1-Motion>",lefthold)
root.bind("<Right>", rightKey)
root.bind("<Left>", leftKey)
root.geometry('1920x1080')
root.title("DSS")
root.resizable(width=False,height=False)


root.mainloop()