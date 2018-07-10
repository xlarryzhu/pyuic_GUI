# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:29:59 2018

@author: xinlei.zhu
"""
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
from MainWidget import Ui_Main
from os import path
import subprocess
import sys

class MainWidget(QWidget):
    
    def __init__(self):
        super(MainWidget, self).__init__()
        self.welcomemessage = ['PyQt user interface converter',
                       'Version 0.1',
                       'By ZXL','to do list:',
                       '1. support for xtra args(xargs) and debug etc. config buttons',
                       '2. search and check version for python exective path',
                       '3. support for linux/mac os',
                       '4. reconstruction',
                       '5. metadata']
        self.initPath = ""
        self.uiFilePath = ""
        self.pyFilePath = ""
        self.UI = Ui_Main()
        self.UI.setupUi(self)
        self._setup()
        self.pyexecpath = path.abspath('C:\Anaconda3\python.exe')
        
    def _setup(self):
        self._displist2tb(self.welcomemessage)
        self.UI.toolButton_in.clicked.connect(self._UIgetdotuifile)
        self.UI.toolButton_out.clicked.connect(self._UIsetdotpyfile)    
        self.UI.pushButton_OK.clicked.connect(self._Convert)    

    def _UIgetdotuifile(self):
        file = QFileDialog.getOpenFileName(None,"Select .ui File:",self.initPath,\
                                           ".ui Files(*.ui);;All Files(*.*)")
        self.uiFilePath = file[0]
        self.initPath = path.dirname(self.uiFilePath)
        self.pyFilePath = self._setdotpyfile()
        self._refreshIOPaths()
        return

    def _UIsetdotpyfile(self):

        file = QFileDialog.getSaveFileName(None,"Save .py File as:",self.pyFilePath,".py Files(*.py);;All Files(*.*)")
        self.pyFilePath = file[0]
        self._refreshIOPaths()
        return
    
    def _setdotpyfile(self):
        if self.initPath != '':
            return str(self.initPath+'/'+path.splitext(path.basename(self.uiFilePath))[0]+'.py')
        else:
            return ''
        
    def _refreshIOPaths(self):
        self.UI.lineEdit_in.setText(self.uiFilePath)
        self.UI.lineEdit_out.setText(self.pyFilePath)

    def _run(self):
        self.show()
        
    def _Convert(self):
        self.UI.textBrowser.clear()
        
        if not any(self.uiFilePath):
            self._UIgetdotuifile()
            return
        if not any(self.pyFilePath):
            self._UIsetdotpyfile()
            return
        
        xargs = self.UI.lineEdit_op.text().strip().split(' ')
        
        cmd_list = [self.pyexecpath.strip(),'-m','PyQt5.uic.pyuic','--output='+self.UI.lineEdit_out.text().strip(),self.UI.lineEdit_in.text().strip()]
        si = subprocess.STARTUPINFO
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        sp = subprocess.Popen(cmd_list,stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True,startupinfo=si)
        while True:
            bytedata_out = sp.stdout.readlines()
            bytedata_err = sp.stderr.readlines()
            if len(bytedata_err) != 0:
                strlist_err = self._bytelist2strlist(bytedata_err)
                self._displist2tb(strlist_err) 
                break
        
            if len(bytedata_out) == 0:
                if sp.poll() is not None:
                    str_out = 'Convertion complete!'
                    self._disp2tb(str_out)
                    break
            else:
                strlist_out = self._bytelist2strlist(bytedata_out)
                self._displist2tb(strlist_out) 


                        
    def _bytelist2strlist(self,bytelist,coding = 'gb2312'):
        strlist = []
        for bt in bytelist:
            strlist.append(bt.decode(coding))
        return strlist  
    
    def _disp2tb(self,strdata):
        self.UI.textBrowser.append(strdata)
        
    def _displist2tb(self,listdata):
        for str_data in listdata:
            self._disp2tb(str_data)

def _main():
    app = QApplication(sys.argv)
    main = MainWidget()
    main._run()
    app.exec_()
    sys.exit

if __name__ == "__main__":
    _main()

