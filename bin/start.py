import sys
sys.path.append("..")
from core.puttyAutoLogin import puttyAutoLogin
import os,configparser
if os.access('../conf/conf.properties',os.R_OK):#import pathlib;pathlib.Path.exists('conf.properties'): 
	def getValue(nodeName,keyName,configObject=configparser.ConfigParser()):
		with open('../conf/conf.properties', 'r',encoding='utf-8') as cfg:  
			configObject.read_file(cfg)  
			return configObject.get(nodeName, keyName)
	config =configparser.ConfigParser()		
	puttyAutoLogin(
	server=getValue('serverConfig','server',configObject=config),\
	user=getValue('serverConfig','user',configObject=config),\
	pwd=getValue('serverConfig','pwd',configObject=config),\
	serverIndex=int(getValue('serverConfig','serverIndex',configObject=config)),\
	puttyPath=getValue('puttyConfig','puttyPath',configObject=config),\
	delay=int(getValue('puttyConfig','delay',configObject=config)),\
	nextCommand=getValue('puttyConfig','nextCommand',configObject=config),\
)
else:puttyAutoLogin()