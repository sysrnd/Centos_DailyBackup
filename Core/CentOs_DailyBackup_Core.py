# -*- coding: utf-8 -*-
import sys
import os
import json
import time

from shutil import copytree
from shutil import ignore_patterns
from shutil import rmtree
from shutil import copy2



"""
if sys.platform == WINDOWS:
    print "Holis estoy en windows"
"""



class DailyBackupFunctions:

    def __init__(self, pathToConfigFile):
        """
        """
        self.DataPathKey = 'DataPath'
        self.BackupPathKey = 'BackupPath'
        self.Frequency = 'Frequency'
        self.JsonFile = pathToConfigFile

    def SaveConfigFile(self, dataPath, backupPath):
        """
        """
        #dataPath = 'D:/CentOS_FilesPathTest/CurrentFolder'
        #backupPath = 'D:/CentOS_FilesPathTest/BackUpFolder'

        data = {
            self.Frequency: 5,
            self.DataPathKey: dataPath,
            self.BackupPathKey: backupPath
            }

        with open(self.JsonFile, 'w') as outfile:
            json.dump(data, outfile, indent = 4, sort_keys = True)


        # Modificacion del cron solo si esta en linux
        if sys.platform != "win32":
            crontabPath = "/etc/crontab"
            
            crontab_file = open(crontabPath, 'r')
            todoTexti = ""

            # Minuto hora diaMes mes diaSemana
            header = "# # # # # # # # # #\n#  CentOs Backup  #\n"
            header = header + "# # # # # # # # # # \n"

            cronTime = "30 2 * * * "
            cronLine = "python /media/Storage/MASTER/RnD/"
            cronLine = cronLine + "SystemTools/Centos_DailyBackup/Core/"
            cronLine = cronLine + "CentOs_DailyBackup_Core.py\n"

            ender  = "# # # # # # # # # # # #\n#  CentOs Backup End  #\n"
            ender = ender + "# # # # # # # # # # # #\n"
            
            for line in crontab_file:
                todoTexti = todoTexti + str(line)
            crontab_file.close()

            todoTexti = todoTexti+ header + cronTime + cronLine + ender

            if todoTexti.count(header) >0:
                # actualizar informacion de cron
                oldText = todoTexti.split(header)
                endCronText = oldText[1].split(ender)[1]
                todoTexti = oldText[0] + header + cronTime + cronLine + ender + endCronText
            else:
                todoTexti = todoTexti+ header + cronTime + cronLine + ender

            """
            # Todo listo para actualizar el server
            nfileo=open(crontabPath,'w')
            nfileo.write(todoTexti)
            nfileo.close()
            """


    def ReadConfigFile(self):
        self.data_loaded = []
        with open(self.JsonFile) as data_file:
            self.data_loaded = json.load(data_file)

    def CopyFiles(self):
        source =  self.data_loaded[self.DataPathKey]
        destination = self.data_loaded[self.BackupPathKey]
        self.copyTree_F(source = source, destination = destination)


    def DeleteFiles(self):
        """
        """

    def copyTree_F(self,source, destination):
        if os.path.isdir(source):
            try:
                copytree(source, destination, ignore=ignore_patterns("*.pyc","*.tmp"))
            except:
                allElements = os.listdir(source)
                for aE in allElements:
                    s = source + "/"+ unicode(aE)
                    d = destination + "/" + unicode(aE)
                    if s.count("/A_Borrar") == 0:
                        self.copyTree_F(source = s, destination = d)

        else:
            if not os.path.exists(unicode(destination)):
                try:
                    copy2(unicode(source), unicode(destination))
                except:
                    print "error en: " + destination
            else:
                d_modTime = time.ctime(os.path.getmtime(unicode(destination)))
                o_modTime = time.ctime(os.path.getmtime(unicode(source)))

                if (d_modTime != o_modTime):
                    copy2(unicode(source), unicode(destination))


if __name__ == "__main__":
    #sys.setdefaultencoding('utf8')
    pathJson = ""
    dPath = ""
    backPath = ""

    if sys.platform == "win32":
        #
        #   WINDOWS
        #
        pathJson = "D:/AllDocuments/Desktop/RnD/Centos_DailyBackup/sysconfig/ConfigJsonFile.json"
        dPath = "D:/CentOS_FilesPathTest/CurrentFolder"
        backPath = "D:/CentOS_FilesPathTest/BackUpFolder"
        
    else:
        #
        #  LINUX
        #
        pathJson = "/media/Storage/MASTER/RnD/SystemTools/Centos_DailyBackup/sysconfig/ConfigJsonFile.json"
        dPath = "/media/Storage/MASTER/MKF_MotionGraphics"
        backPath = "/run/media/soporte/Respaldo/MASTER/MKF_MotionGraphics"

        dPath = "/media/Storage/MASTER/RnD/Sandbox/Fidel"
        backPath = "/run/media/soporte/Respaldo/MASTER/RnD/Sandbox/Fidel"

    coreFunctions = DailyBackupFunctions (pathJson)

    coreFunctions.SaveConfigFile(dataPath = dPath, backupPath = backPath)
    coreFunctions.ReadConfigFile()
    coreFunctions.CopyFiles()
    print "Termine papi"
