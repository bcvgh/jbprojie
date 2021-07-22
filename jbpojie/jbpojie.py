import os
import sys
import win32api
import win32con
import configparser

root_dir = os.path.dirname(os.path.abspath(__file__))
conf = configparser.ConfigParser()
conf.read(root_dir+"\\config.ini")

python_ver = conf.get("Version","pycharm") #'PyCharm2021.1'
php_ver = conf.get("Version","phpstorm")#'PhpStorm2021.1'
java_ver = conf.get("Version","idea")#'IntelliJIdea2021.1'
r_ver = conf.get("Path","resigister")#'Software\\JavaSoft\\Prefs\\jetbrains'
parm = conf.get("Path","userpath")#'C:\\Users\\zll\\AppData\\Roaming\\JetBrains'

def delfile(path):
    if not os.path.isfile(path):
        for i in os.listdir(path):
            data_path=path+'\\'+i
            if os.path.isfile(data_path) ==True:
                os.remove(data_path)
            else:
                delfile(data_path)
    else:
        os.remove(path)

def delenkey(en_key,ver):
  en_key=win32api.RegEnumKeyEx(en_key)
  for i in en_key:
      ven=ver+'\\'+i[0]
      en_key=win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,ven,0,win32con.KEY_ALL_ACCESS)
      if win32api.RegEnumKeyEx(en_key):
          delenkey(en_key, ven)
      win32api.RegCloseKey(en_key)
      en_key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, ver, 0, win32con.KEY_ALL_ACCESS)
      win32api.RegDeleteKey(en_key, i[0])
      win32api.RegCloseKey(en_key)

def delkey(par):
    if par == 'java':
        r_name = 'idea'
    elif par == 'php':
        r_name = 'phpstorm'
    elif par == 'python':
        r_name = 'pycharm'
    ver = r_ver+'\\'+r_name
    kkey=win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,ver,0,win32con.KEY_ALL_ACCESS)
    if  win32api.RegEnumKeyEx(kkey):
        delenkey(kkey, ver)
    win32api.RegCloseKey(kkey)
    kkey = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, r_ver, 0, win32con.KEY_ALL_ACCESS)
    win32api.RegDeleteKey(kkey, r_name)
    win32api.RegCloseKey(kkey)

if __name__ == '__main__':
    par=sys.argv[1]
    if par == 'python':
        delfile(parm+'\\'+python_ver+'\\eval')
        delfile(parm+'\\'+python_ver+'\\options\other.xml')
        delkey(par)
        print('pycharm试用期重置成功！')
    elif par == 'php':
        delfile(parm + '\\' + php_ver+'\\eval')
        delfile(parm + '\\' + php_ver+'\\options\other.xml')
        delkey(par)
        print('phpstorm试用期重置成功！')
    elif par == 'java':
        delfile(parm + '\\' + java_ver+'\\eval')
        delfile(parm + '\\' + java_ver+'\\options\other.xml')
        delkey(par)
        print('idea试用期重置成功！')
    else:
        print('unknow')