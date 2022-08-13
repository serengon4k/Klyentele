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
    return DataValue


class Client:
    def __init__(self, ClientID):
        self.FirstName = str()
        self.LastName = str()
        self.Address = str()
        self.PhoneNumber = str()
        self.Email = str()
        self.ClientID = str()
        self.Notes = str()
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

        # Load ClientID
        self.Query.execute(
            f"SELECT ClientID FROM Clients WHERE ClientID ='{DataCleaner(ClientID)}'"
        )
        # Set ClientID equal to self.Query result
        ClientID = self.Query.fetchall()
        self.ClientID = DataCleaner(ClientID)
        self.OldClientID = DataCleaner(ClientID)

        # Load Name
        self.Query.execute(
            f"SELECT FirstName FROM Clients WHERE _rowid_='{self.ClientID}'")
        AllData = self.Query.fetchall()
        self.FirstName = DataCleaner(AllData)
        self.Query.execute(
            f"SELECT LastName FROM Clients WHERE _rowid_='{self.ClientID}'")
        AllData = self.Query.fetchall()
        self.LastName = DataCleaner(AllData)
        # Load Address
        self.Query.execute(
            f"SELECT Address FROM Clients WHERE _rowid_='{self.ClientID}'")
        AllData = self.Query.fetchall()
        self.Address = DataCleaner(AllData)
        # Load Phone Number
        self.Query.execute(
            f"SELECT PhoneNumber FROM Clients WHERE _rowid_='{self.ClientID}'"
        )
        AllData = self.Query.fetchall()
        self.PhoneNumber = DataCleaner(AllData)
        # Load Email
        self.Query.execute(
            f"SELECT Email FROM Clients WHERE _rowid_='{self.ClientID}'")
        AllData = self.Query.fetchall()
        self.Email = DataCleaner(AllData)
        # Load Notes
        self.Query.execute(
            f"SELECT Notes FROM Clients WHERE _rowid_='{self.ClientID}'")
        AllData = self.Query.fetchall()
        self.Notes = DataCleaner(AllData)
        # Load Standing
        self.Query.execute(
            f"SELECT Standing FROM Clients WHERE _rowid_='{self.ClientID}'")
        AllData = self.Query.fetchall()
        self.Standing = DataCleaner(AllData)

    def SaveAll(self):
        self.Query.execute(
            'UPDATE "Clients" SET "FirstName"=' + "'" + self.FirstName +
            "', " '"LastName"=' + "'" + self.LastName + "', "
            + '"Address"='
            + "'"
            + self.Address
            + "', "
            + '"Email"='
            + "'"
            + self.Email
            + "',"
            + '"ClientID"='
            + "'"
            + self.ClientID
            + "',"
            + '"PhoneNumber"='
            + "'"
            + self.PhoneNumber
            + "',"
            + '"Notes"='
            + "'"
            + self.Notes
            + "'"
            + ","
            + '"Standing"='
            + "'"
            + self.Standing
            + "'"
            + ' WHERE "_rowid_"='
            + "'"
            + self.OldClientID
            + "'"
        )
        self.DB.commit()

    def CreateNewClient(self, FirstName, Lastname, Address, PhoneNumber, Email, Standing, Notes):
        ClientID = T.strftime("%H%M%S")
        self.Query.execute(
            'INSERT INTO "Clients"'
            + ' ("FirstName", "LastName", "Address", "PhoneNumber","Email","ClientID", "Standing", Notes)'
            + " VALUES ("
            + "'"
            + DataCleaner(FirstName)
            + "','"
            + DataCleaner(Lastname)
            + "','"
            + DataCleaner(Address)
            + "','"
            + DataCleaner(PhoneNumber)
            + "','"
            + DataCleaner(Email)
            + "','"
            + DataCleaner(ClientID)
            + "','"
            + DataCleaner(Standing)
            + "','"
            + DataCleaner(Notes)

            + "')"
        )
        self.DB.commit()

    def DeleteClient(self, ClientID):
        self.Query.execute(
            'DELETE FROM "Clients" WHERE _rowid_ IN (' +
            "'" + ClientID + "'" ")"
        )
        self.DB.commit()

    def GetFirstName(self):
        return self.FirstName

    def SetFirstName(self, NewFirstName):
        self.FirstName = NewFirstName
        self.SaveAll(self)

    def GetLastName(self):
        return self.LastName

    def SetLastName(self, NewLastName):
        self.FirstName = NewLastName
        self.SaveAll(self)

    def GetClientID(self):
        return self.ClientID

    def SetClientID(self, NewID):
        self.ClientID = NewID
        self.SaveAll(self)
        self.__init__(self, self.ClientID)

    def GetAddress(self):
        return self.Address

    def SetAddress(self, NewAddress):
        self.Address = NewAddress
        self.SaveAll(self)

    def GetPhoneNumber(self):
        return self.PhoneNumber

    def SetPhoneNumber(self, NewPhoneNumber):
        self.PhoneNumber = NewPhoneNumber
        self.SaveAll(self)

    def GetEmail(self):
        return self.Email

    def SetEmail(self, NewEmail):
        self.Email = NewEmail
        self.SaveAll(self)

    def GetNotes(self):
        return self.Notes

    def SetNotes(self, NewNotes):
        self.Notes = NewNotes
        self.SaveAll(self)

    def GetStanding(self):
        return self.Standing

    def SetStanding(self, NewStanding):
        self.Standing = NewStanding
        self.SaveAll(self)
