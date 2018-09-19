#This a part of making_douyin_vedio
#import OpenCV
import cv2
def video2txtimage(video_file):
	VIpath='videoimages\\'
	video=cv2.VideoCapture(video_file)
	if video.isOpened():
		total_num=video.get(7)
		for num in range(int(total_num)-1):
			r,frame=video.read()
			cv2.imwrite(VIpath+str(num)+'.jpg',frame)
			print('The No. %d image made' %num)
			get_txt_image(VIpath,str(num)+'.jpg')
		fps=video.get(cv2.CAP_PROP_FPS)
		video.release()
		return fps
	else:
		print('fail to reading video')

import PIL
#import Pillow
def get_char(r,g,b,alpha=256):
	if alpha == 0:
		return ''
	length = len(ascii_char)
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)
	unit = (256.0+1)/length
	return ascii_char[int(gray/unit)]


def get_txt_image(path,filename):
	im = Image.open(path+filename).convert('RGB')
	raw_width=im.raw_width
	raw_height=im.raw_height
	im_txt=Image.new("RGB",(raw_width,raw_height),(255,255,255))
	dr=ImageDraw.Draw(im_txt)

	font=ImageFont.load_default().font
	char=''
	font_w,font_h=font.getsize(char)

	h_dis=1.5
	w_dis=1.2
	width=int(raw_width/font_w/w_dis) 
	im=im.resize((width,height),Image.NEAREST)
	txt=""
	for row in range(height):
		for col in range(width):
			pixel=im.getpixel((col,row))
			txt+=get_char(*pixel)
		txt+='\n'


def image2video(out_file,fps):
 	Ipath='new_Images'
 	fourcc=cv2.VideoWriter_fourcc(*"MJPG")
 	images=os.listdir(Ipath)
 	im=Image.open(Ipath+'\\'+images[0])
 	new_video=cv2.VideoWriter(out_file+'.avi',fourcc,fps,im.size)
 	os.chdir(Ipath)
 	for image in range(1,len(images)+1):
 		frame=cv2.imread(str(image)+'.jpg')
 		new_video.write(frame)
 	print('finish making video')
 	new_video.release()

