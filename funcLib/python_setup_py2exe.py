#encoding=utf-8

from distutils.core import setup
import py2exe

options = {"py2exe":{"compressed": 1, #ѹ��   
	        "optimize": 2,  
	        "bundle_files": 1 # �����ļ������һ��exe�ļ� ��win64ϵͳ��ֻ����3�� 
	}}

setup(console=["ATLayerJtl.py"], options=options, zipfile=None)