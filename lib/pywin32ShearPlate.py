# coding=utf-8
import win32clipboard as w
import win32con,time
import win32api

def _setImage(data):  # 写入剪切板
	import traceback, win32gui
	from PIL import Image
	from cStringIO import StringIO
	win32clipboard.OpenClipboard()
	try:
		# Unicode tests
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(win32con.CF_DIB, data)
	except:
		traceback.print_exc()
	finally:
		win32clipboard.CloseClipboard()

def _getText():  # 读取剪切板  
	w.OpenClipboard()
	d = w.GetClipboardData(win32con.CF_TEXT)
	w.CloseClipboard()
	return d


def _setText(String):  # 写入剪切板  
	w.OpenClipboard()
	w.EmptyClipboard()
	w.SetClipboardText(String) 
	w.CloseClipboard()

def _cuttingText(String,delay=0,cuttingType=1,pressEnterDelay=0,isPressEnter=False):  # 写入剪切板      
	_setText(String)                                         # 将“test”写入剪切板
	time.sleep(delay)
	if cuttingType:
		win32api.keybd_event(17, 0, 0, 0)                           # ctrl的键位码是17  
		win32api.keybd_event(86, 0, 0, 0)                           # v的键位码是86  
		win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)    # 释放按键  
		win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
		pass
		if isPressEnter:
			time.sleep(pressEnterDelay)
			print(pressEnterDelay)
			win32api.keybd_event(13,0,0,0) 
			win32api.keybd_event(13,0,0,0)
			#time.sleep(0.01)
			#win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
	else:win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0,0,0,0)

def _cuttingImage(String,className='',Title=''):  #           
	img = Image.open(String)
	output = StringIO()
	img.convert("RGB").save(output, "BMP")
	data = output.getvalue()[14:]
	output.close()
	_setImage(data)

	pwin = win32gui.FindWindow(className,Title)                           # 获取窗口句柄
	win32gui.ShowWindow(pwin, win32con.SW_RESTORE)
	win32gui.SetActiveWindow(pwin)
	win32gui.SetForegroundWindow(pwin)
	rect = win32gui.GetWindowRect(pwin)                                         # 获取窗口位置
	x ,y = (rect[0] + rect[2]) / 2, rect[3] - 50
	win32api.SetCursorPos((x, y))                                               # 设置鼠标位置
	win32api.mouse_event(0x0002, 0, 0, 0, 0)                                    # 模拟鼠标按下
	win32api.mouse_event(0x0004, 0, 0, 0, 0)                                    # 模拟鼠标弹起
	win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)                          # ctrl的键位码是17
	win32api.keybd_event(86, 0, 0, 0)                                           # v的键位码是86
	win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)                    # 释放按键
	win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)   # 释放按键
	win32api.keybd_event(13, 0, 0, 0)                                           # Enter的键位码是13
	win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  
#if __name__ == '__main__':
