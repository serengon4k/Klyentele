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

import sqlite3 as sq
import Lib.Visor as Visor
import time as T
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
    if DataValue == "":
        return 0
    else:
        return DataValue


class Project:
    def __init__(self, ProjectID):
        self.ProjectName = str()
        self.Description = str()
        self.Catogory = str()
        self.ProjectID = str()
        self.ClientID = str()
        self.AssignedUsers = str()
        self.TotalInvoice = float()
        self.PayedHours = float()
        self.UnpaidHours = float()
        self.HourlyPayRate = float()
        self.CompletionPercent = float()
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

        # Load ProjectID
        self.Query.execute(
            f"SELECT ProjectID FROM Projects WHERE ProjectID ='{DataCleaner(ProjectID)}'"
        )
        # Set ProjectID equal to self.Query result
        ProjectID = self.Query.fetchall()
        self.ProjectID = DataCleaner(ProjectID)
        self.OldProjectID = DataCleaner(ProjectID)

        # Load Name
        self.Query.execute(
            f"SELECT ProjectName FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.ProjectName = DataCleaner(AllData)

        # Load Description
        self.Query.execute(
            f"SELECT Description FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.Description = DataCleaner(AllData)

        # Load TotalInvoice
        self.Query.execute(
            f"SELECT TotalInvoice FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.TotalInvoice = float(DataCleaner(AllData))

        # Load AssignedUsers
        self.Query.execute(
            f"SELECT AssignedUsers FROM Projects WHERE _rowid_='{self.ProjectID}'"
        )
        AllData = self.Query.fetchall()
        self.AssignedUsers = DataCleaner(AllData)

        # Load ClientID
        self.Query.execute(
            f"SELECT ClientID FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.ClientID = DataCleaner(AllData)

        # Load CompletionPercent
        self.Query.execute(
            f"SELECT CompletionPercent FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.CompletionPercent = float(DataCleaner(AllData))

        # Load Catogory
        self.Query.execute(
            f"SELECT Catogory FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.Catogory = DataCleaner(AllData)

        # Load PayedHours
        self.Query.execute(
            f"SELECT PayedHours FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.PayedHours = float(DataCleaner(AllData))

        # Load Unpaid hours
        self.Query.execute(
            f"SELECT UnpaidHours FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.UnpaidHours = float(DataCleaner(AllData))

        # Load Hourly Pay Rate
        self.Query.execute(
            f"SELECT HourlyPayRate FROM Projects WHERE _rowid_='{self.ProjectID}'")
        AllData = self.Query.fetchall()
        self.HourlyPayRate = float(DataCleaner(AllData))

    def SaveAll(self):
        self.Query.execute(
            'UPDATE "Projects" SET "ProjectName"=' + "'" + self.ProjectName +
            "', " '"Description"=' + "'" + self.Description + "', "
            + '"TotalInvoice"='
            + "'"
            + self.TotalInvoice
            + "', "
            + '"ClientID"='
            + "'"
            + self.ClientID
            + "',"
            + '"ProjectID"='
            + "'"
            + self.ProjectID
            + "',"
            + '"AssignedUsers"='
            + "'"
            + self.AssignedUsers
            + "',"
            + '"CompletionPercent"='
            + "'"
            + str(self.CompletionPercent)
            + "'"
            + ","
            + '"TotalInvoice"='
            + "'"
            + str(self.TotalInvoice)
            + "'"
            + ","
            + '"PayedHours"='
            + "'"
            + str((self.PayedHours))
            + "'"
            + ","
            + '"UnpaidHours"='
            + "'"
            + str(self.UnpaidHours)
            + "'"
            + ","
            + '"HourlyPayRate"='
            + "'"
            + str(self.HourlyPayRate)
            + "'"
            + ","
            + '"Catogory"='
            + "'"
            + self.Catogory
            + "'"
            + ' WHERE "_rowid_"='
            + "'"
            + self.OldProjectID
            + "'"
        )
        self.DB.commit()

    def CreateNewProject(self, ProjectName, Description, AssignedUsers, ClientID, Catogory, HourlyPayRate):
        ProjectID = T.strftime("%H%M%S")
        self.Query.execute(
            'INSERT INTO "Projects"'
            + ' ("ProjectName", "Description", "AssignedUsers","ClientID","ProjectID", "Catogory", HourlyPayRate)'
            + " VALUES ("
            + "'"
            + str(DataCleaner(ProjectName))
            + "','"
            + str(DataCleaner(Description))
            + "','"
            + str(DataCleaner(AssignedUsers))
            + "','"
            + str(DataCleaner(ClientID))
            + "','"
            + str(DataCleaner(ProjectID))
            + "','"
            + str(DataCleaner(Catogory))
            + "','"
            + str(DataCleaner(HourlyPayRate))


            + "')"
        )
        self.DB.commit()

    def DeleteProject(self, ProjectID):
        self.Query.execute(
            'DELETE FROM "Projects" WHERE _rowid_ IN (' +
            "'" + ProjectID + "'" ")"
        )
        self.DB.commit()

    def GetProjectName(self):
        return self.ProjectName

    def SetProjectName(self, NewProjectName):
        self.ProjectName = NewProjectName
        self.SaveAll(self)

    def GetDescription(self):
        return self.Description

    def SetDescription(self, NewDescription):
        self.ProjectName = NewDescription
        self.SaveAll(self)

    def GetProjectID(self):
        return self.ProjectID

    def SetProjectID(self, NewID):
        self.ProjectID = NewID
        self.SaveAll(self)
        self.__init__(self, self.ProjectID)

    def GetTotalInvoice(self):
        return self.TotalInvoice

    def SetTotalInvoice(self, NewTotalInvoice):
        self.TotalInvoice = NewTotalInvoice
        self.SaveAll(self)

    def GetAssignedUsers(self):
        return self.AssignedUsers

    def SetAssignedUsers(self, NewAssignedUsers):
        self.AssignedUsers = NewAssignedUsers
        self.SaveAll(self)

    def GetClientID(self):
        return self.ClientID

    def SetClientID(self, NewClientID):
        self.ClientID = NewClientID
        self.SaveAll(self)

    def GetCompletionPercent(self):
        return self.CompletionPercent

    def SetCompletionPercent(self, NewCompletionPercent):
        self.CompletionPercent = NewCompletionPercent
        self.SaveAll(self)

    def GetCatogory(self):
        return self.Catogory

    def SetCatogory(self, NewCatogory):
        self.Catogory = NewCatogory
        self.SaveAll(self)

    def GetHourlyPayRate(self):
        return self.HourlyPayRate

    def SetCompletionPercent(self, NewHourlyPayRate):
        self.HourlyPayRate = NewHourlyPayRate
        self.SaveAll(self)

    def GetPayedHours(self):
        return self.PayedHours

    def SetPayedHours(self, NewPayedHours):
        self.PayedHours = NewPayedHours
        self.SaveAll(self)

    def GetUnpaidHours(self):
        return self.UnpaidHours

    def SetUnpaidHours(self, NewUnpaidHours):
        self.UnpaidHours = NewUnpaidHours
        self.SaveAll(self)
