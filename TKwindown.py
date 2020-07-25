# 1. -*- coding: utf-8 -*-

import tkinter
import tkinter.filedialog
from aip import AipOcr
from PIL import ImageGrab
import os



window = tkinter.Tk()
window.geometry("600x250")
window.title('图片文字识别')



""" 你的 APPID AK SK """
APP_ID = 'Input baidu_AI num'
API_KEY = 'KEY'
SECRET_KEY = 'KEY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def baidu_AI_text(file_path):
    with open(file_path, 'rb') as fp:
        image = fp.read()
        massage = client.basicGeneral(image)
    for mg in massage.get('words_result'):
        mg_content = mg.get('words')+'\n'
        text.insert(tkinter.INSERT,mg_content)
    fp.close()

def get_file_content():
    filename_path = tkinter.filedialog.askopenfilename()
    if filename_path != '':
        e1.delete(0,'end')
        e1.insert(0,filename_path)
    else:
        e1.delete(0,'end')
    baidu_AI_text(filename_path)

'''需配合Snipaste使用'''
def clipboard_image():
    file_path = os.getcwd()+'\\test.jpg'
    image = ImageGrab.grabclipboard()
    print(image,type(image))
    image.save(file_path)
    baidu_AI_text(file_path)
 

    

topFrame = tkinter.Frame(window,bd=1,width=300,height=200,relief='sunken')
lb1 = tkinter.Label(topFrame,text='File path:')
btn = tkinter.Button(topFrame,text='Choose file',command = get_file_content)
# 2. btn1 = tkinter.Button(topFrame,text='run',command = get_file_content)
btn2 = tkinter.Button(topFrame,text='GetClipImage',command = clipboard_image)
e1=tkinter.Entry(topFrame,width=40)
text = tkinter.Text(window,width=80,height=15)

topFrame.pack(fill = tkinter.BOTH)
lb1.grid(row=0,column=0,sticky=tkinter.W)
e1.grid(row=0,column=1,padx=5,sticky=tkinter.W)
# 3. btn1.grid(row=0,column=3,padx=3,sticky=tkinter.W)
btn.grid(row=0,column=2,padx=5,sticky=tkinter.W)
btn2.grid(row=0,column=4,padx=5,sticky=tkinter.W)
text.pack()

window.mainloop()
