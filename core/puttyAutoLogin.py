import sys
sys.path.append("..")
from lib.pywin32ShearPlate import _cuttingText
import time,win32api,win32con,win32com.client,win32gui,os

def puttyAutoLogin(server='202.182.999.135',user='root',pwd=123456789,puttyPath="D:/Program Files/SSH/putty.exe",delay=5,serverIndex=2,nextCommand='sudo apt-get update && sudo apt-get dist-upgrade -y'):
	#from os.path import *dirname(abspath(__file__))+'./okButton.png'
	result=win32com.client.GetObject('winmgmts:').ExecQuery('select * from Win32_Process where Name="PuTTY"')
	def _checkExsit(process_name='PuTTY.exe'):
		if '<C' in str(result):#windows10 seem not support it <COMObject <unknown>>
			if os.popen(f'tasklist /FI "IMAGENAME eq {process_name}"').read().count(process_name) :return True
	
	if not _checkExsit():
		win32api.ShellExecute(0,'open',puttyPath,'','',1);time.sleep(0.5)
		
	puttyHwnd=win32gui.FindWindow('PuTTY', server+' - PuTTY')
	win32gui.SetActiveWindow(puttyHwnd)#win32gui.ShowWindow(puttyHwnd, win32con.SW_RESTORE)
	[(win32api.keybd_event(9,0,0,0),time.sleep(0.05)) for i in range(4)]
	time.sleep(0.5)
	[win32api.keybd_event(40,0,0,0) for i in range(serverIndex)]
	win32api.keybd_event(13,0,0,0)
	time.sleep(delay)
	while not win32gui.FindWindow('PuTTY', server+' - PuTTY'):
		print('Waiting for PuTTY');time.sleep(0.5)
	_cuttingText(user,delay=0.05,cuttingType=0)
	time.sleep(0.05)
	win32api.keybd_event(13,0,0,0)
	time.sleep(0.5)
	_cuttingText(pwd,delay=0.05,cuttingType=0)
	time.sleep(0.05)
	win32api.keybd_event(13,0,0,0)
	if nextCommand:_cuttingText(nextCommand,cuttingType=0,isPressEnter=True)
	
	# def closePutty():
	# 	thread,processId =win32process.GetWindowThreadProcessId(puttyHwnd) 
	# 	os.kill(processId,signal.CTRL_C_EVENT) 
	# 	os.kill(processId,signal.CTRL_BREAK_EVENT) 
	# 	win32gui.CloseWindow(puttyHwnd)	
	os._exit(1)
