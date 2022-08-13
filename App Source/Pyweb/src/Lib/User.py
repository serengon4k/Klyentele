#
# Copyright 2021 Azura4k
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import date
import sqlite3 as sq
import random
import Lib.Visor as Visor

# Name of Database File
DataLocation = Visor.DataLocation


def DataCleaner(DataValue):
    DataValue = str(DataValue)
    DataValue = DataValue.replace("(", "")
    DataValue = DataValue.replace(")", "")
    DataValue = DataValue.replace("'", "")
    DataValue = DataValue.replace(",", "")
    DataValue = DataValue.replace("[", "")
    DataValue = DataValue.replace("]", "")
    DataValue = DataValue.replace("{", "")
    DataValue = DataValue.replace("}", "")
    DataValue = DataValue.lstrip()
    return DataValue


class User:
    def __init__(self, Username):
        self.Username = str()
        self.Password = str()
        self.UID = str()
        self.LoginDate = str()
        self.ClearanceLvl = str()
        self.Department = str()
        self.Title = str()
        # Database Connection
        try:
            # Attempt Connection
            self.DB = sq.connect(DataLocation)
            # For Logging and Debuging, To be removed from final
            print("Connection Success")
        except:
            # For Logging and Debuging, To be removed from final
            print("Connection Failure")
        self.Query = self.DB.cursor()
        # Load UID
        self.Query.execute(
            f"SELECT UID FROM Users WHERE Username='{DataCleaner(Username)}'"
        )
        # Set UID equal to self.Query result
        UID = self.Query.fetchall()
        self.UID = DataCleaner(UID)
        self.OldUID = DataCleaner(UID)
        # Load Username
        self.Query = self.DB.cursor()
        self.Query.execute(
            f"SELECT Username FROM Users WHERE _rowid_='{self.UID}'")
        AllData = self.Query.fetchall()
        self.Username = DataCleaner(AllData)
        # Load Password
        self.Query.execute(
            f"SELECT Password FROM Users WHERE _rowid_='{self.UID}'")
        AllData = self.Query.fetchall()
        self.Password = DataCleaner(AllData)
        # Load Password
        self.Query.execute(
            f"SELECT ClearanceLvl FROM Users WHERE _rowid_='{self.UID}'"
        )
        AllData = self.Query.fetchall()
        self.ClearanceLvl = DataCleaner(AllData)
        # Load Last Login
        self.Query.execute(
            f"SELECT LastLogin FROM Users WHERE _rowid_='{self.UID}'")
        AllData = self.Query.fetchall()
        self.LastLogin = DataCleaner(AllData)
        # Load Department
        self.Query.execute(
            f"SELECT Department FROM Users WHERE _rowid_='{self.UID}'")
        AllData = self.Query.fetchall()
        self.Department = DataCleaner(AllData)
        # Load Title
        self.Query.execute(
            f"SELECT Title FROM Users WHERE _rowid_='{self.UID}'")
        AllData = self.Query.fetchall()
        self.Title = DataCleaner(AllData)

    def SaveNewUserData(self):
        self.Query.execute(
            'UPDATE "Users" SET "Username"=' + "'" + self.Username + "', "
            '"Password"='
            + "'"
            + self.Password
            + "', "
            + '"LastLogin"='
            + "'"
            + self.LastLogin
            + "', "
            + '"ClearanceLvl"='
            + "'"
            + self.ClearanceLvl
            + "',"
            + '"UID"='
            + "'"
            + self.UID
            + "',"
            + '"Department"='
            + "'"
            + self.Department
            + "',"
            + '"Title"='
            + "'"
            + self.Title
            + "'"
            + ' WHERE "_rowid_"='
            + "'"
            + self.OldUID
            + "'"
        )
        self.DB.commit()

    def CreateUser(self, NewUsername, NewPassword, NewClearanceLvl, Department, Title):
        TodaysDate = str(date.today())
        self.Query.execute(
            'INSERT INTO "Users"'
            + ' ("Username", "Password", "LastLogin", "ClearanceLvl","Department","Title")'
            + " VALUES ("
            + "'"
            + DataCleaner(NewUsername)
            + "','"
            + DataCleaner(NewPassword)
            + "','"
            + DataCleaner(TodaysDate)
            + "','"
            + DataCleaner(NewClearanceLvl)
            + "','"
            + DataCleaner(Department)
            + "','"
            + DataCleaner(Title)
            + "')"
        )
        self.DB.commit()

    def DeleteUser(self, Username):
        self.Query.execute(
            f"SELECT UID FROM Users WHERE Username='{DataCleaner(Username)}'"
        )
        # Set UID equal to self.Query result
        UID = self.Query.fetchall()
        UID = DataCleaner(UID)
        self.Query.execute(
            'DELETE FROM "Users" WHERE _rowid_ IN (' + "'" + UID + "'" ")"
        )
        self.DB.commit()

    # Get and Set Parameters
    def GetUsername(self):
        return self.Username

    def SetUsername(self, NewUsername):
        self.Username = NewUsername
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)

    def GetPassword(self):
        return self.Password

    def SetPassword(self, NewPassword):
        self.Password = NewPassword
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)

    def GetLastLoginDate(self):
        return self.LastLogin

    def SetLastLoginDate(self, NewDate):
        self.LastLogin = NewDate
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)

    def GetUID(self):
        return self.UID

    def SetUID(self, NewUID):
        self.UID = NewUID
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)

    def GetClearanceLvl(self):
        return self.ClearanceLvl

    def SetClearanceLvl(self, NewLevel):
        self.ClearanceLvl = NewLevel
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)

    def GetDepartment(self):
        return self.Department

    def SetDepartment(self, NewDepartment):
        self.Department = NewDepartment
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)

    def GetTitle(self):
        return self.Title

    def SetTitle(self, NewTitle):
        self.Title = NewTitle
        self.SaveNewUserData(self)
        self.__init__(self, self.Username)
