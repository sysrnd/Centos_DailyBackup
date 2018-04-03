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
        self.WINDOWS = "win32"
        self.LINUX = ""

        self.DataPathKey = 'DataPath'
        self.BackupPathKey = 'BackupPath'
        self.DaysToPurgeKey = 'Days to purge'

        self.ReadConfigFile(pathToConfigFile)
        self.CopyFiles()

    def SaveConfigFile(self, filePath):
        """
        """
        dataPath = 'D:/CentOS_FilesPathTest/CurrentFolder'
        backupPath = 'D:/CentOS_FilesPathTest/BackUpFolder'

        data = {
            self.DaysToPurgeKey: 5,
            self.DataPathKey: dataPath,
            self.BackupPathKey: backupPath
            }

        with open(filePath, 'w') as outfile:
            json.dump(data, outfile, indent = 4, sort_keys = True)

    def ReadConfigFile(self, filePath):
        self.data_loaded = []
        with open(filePath) as data_file:
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
                copytree(source, destination, ignore=(ignore_patterns("*.pyc","*.tmp"), ignorePath('*/A_Borrar/*')))
            except:
                allElements = os.listdir(source)
                for aE in allElements:
                    s = source + "/"+str(aE)
                    d = destination + "/"+str(aE)
                    self.copyTree_F(source = s, destination = d)

        else:
            if not os.path.exists(destination):
                copy2(source, destination)
            else:
                d_modTime = time.ctime(os.path.getmtime(destination))
                o_modTime = time.ctime(os.path.getmtime(source))

                if (d_modTime != o_modTime):
                    copy2(source, destination)


coreFunctions = DailyBackupFunctions("D:/CentOS_FilesPathTest/ConfigJsonFile.json")
