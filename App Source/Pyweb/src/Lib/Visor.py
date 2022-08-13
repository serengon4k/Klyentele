#
# Copyright 2021 Azura LLC
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
import pyrebase
import random

# Impalement Github Killswitch, if github killswitch repo returns false, program cannot run. Also implement hard authorization with developer Password which is hard encoded
# Program will check with firebase for authorization number

# Name of Database File
DataLocation = "data.db"


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


class Visor:
    def __init__(self):
        # Database Connection
        try:
            # Attempt Connection
            self.DB = sq.connect(DataLocation)
            # For Logging and Debuging, To be removed from final
            print("Connection Success")
        except:           # For Logging and Debuging, To be removed from final
            print("Connection Failure")
            print("Attempting to Create New Database")
            self.CreateDataTables(self)

        try:
            self.CreateDataTables(self)
        except:
            print("Attempted to Create Tables")
        self.Query = self.DB.cursor()
        self.AuthenticityCheck(self)

    def AuthenticityCheck(self):
        # Grab stored key from storage and check against server to ensure authenticity
        # If false at most 3 times, close program without saving
        # Do not work without pinging server first and ensuring response
        # If true, allow program to remain open.
        # Add Killswitch Check
        return True

    def Login(self, Username, Password):
        Query = self.DB.cursor()
        # For every right match, a point is awarded
        SecureIncrementChecksum = int(0)
        # Check for Username Match
        Query.execute("SELECT Username FROM Users")
        AllData = Query.fetchall()
        for Data in AllData:
            if DataCleaner(Data) == Username:
                SecureIncrementChecksum += 1
        # Check for Password Match
        Query.execute("SELECT Password FROM Users")
        AllData = Query.fetchall()
        for Data in AllData:
            if DataCleaner(Data) == Password:
                SecureIncrementChecksum += 1
        # Tally Points and see if true
        if SecureIncrementChecksum >= 2:
            TodaysDate = str(date.today())
            self.Query.execute(
                f"SELECT UID FROM Users WHERE Username='{DataCleaner(Username)}'"
            )
            # Set UID equal to self.Query result
            UID = self.Query.fetchall()
            UID = DataCleaner(UID)
            # Attempt to write new login date to database
            try:
                Query.execute(
                    f"UPDATE Users SET LastLogin='{TodaysDate}' WHERE _rowid_='{UID}'"
                )
            except:
                print("Failed Login")
            print("Passed Login")

            # Commit Database Changes
            self.DB.commit()
            return True

        else:
            print("Failed Login")
            return False

    def ListUsers(self):
        Query = self.DB.cursor()
        # Select all from Users Table and Go from there
        Query.execute("SELECT Username, LastLogin FROM Users")
        AllData = Query.fetchall()
        # For all data within query, print each line
        for Data in AllData:
            print(DataCleaner(Data))

        # Return all data for separate callers.
        return DataCleaner(AllData)

    def ListClients(self):
        Query = self.DB.cursor()
        # Select all from Clients Table and Go from there
        Query.execute("SELECT FirstName, LastName, ClientID FROM Clients")
        AllData = Query.fetchall()
        # For all data within query, print each line
        for Data in AllData:
            print(DataCleaner(Data))

        # Return all data for separate callers.
        return DataCleaner(AllData)

    def ListProjects(self):
        Query = self.DB.cursor()
        # Select all from Clients Table and Go from there
        Query.execute(
            "SELECT ProjectName, Description, ClientID, ProjectID, AssignedUsers FROM Projects")
        AllData = Query.fetchall()
        # For all data within query, print each line
        for Data in AllData:
            print(DataCleaner(Data))

        # Return all data for separate callers.
        return DataCleaner(AllData)

    def CorruptedDB(self):
        pass

    def CreateDataTables(self):
        # Create User Storage Table
        Query = self.DB.cursor()
        # Query to create new table for Users
        try:
            Query.execute(
                "CREATE TABLE 'Users' ('Username' TEXT NOT NULL UNIQUE,'Password' TEXT NOT NULL,'LastLogin' TEXT,'UID' INTEGER NOT NULL UNIQUE,'ClearanceLvl'	TEXT,'Department' TEXT,'Title' TEXT, PRIMARY KEY('UID'));"
            )
        except:
            print("Failed to Create Users Table")

        try:
            # Query to create new table for Clients
            Query.execute(
                "CREATE TABLE 'Clients' ('FirstName' TEXT NOT NULL,'LastName' TEXT NOT NULL ,'Notes' TEXT NOT NULL, 'Address' TEXT,'PhoneNumber' TEXT,'Email' TEXT NOT NULL,'ClientID' INTEGER NOT NULL UNIQUE,'Standing'	TEXT, PRIMARY KEY('ClientID'));"
            )
        except:
            print("Failed to Create Clients Table")
        try:
            # Query to create new table for Clients
            Query.execute(
                "CREATE TABLE 'Projects' ('ProjectName'	TEXT NOT NULL,'Description'	TEXT,'Catogory'	TEXT,'ProjectID' INTEGER NOT NULL UNIQUE,'ClientID'	TEXT NOT NULL,'AssignedUsers'	TEXT,'TotalInvoice'	NUMERIC,'PayedHours'	NUMERIC,'UnpaidHours'	NUMERIC,'HourlyPayRate'	NUMERIC,'CompletionPercent'	NUMERIC,PRIMARY KEY('ProjectID'));"
            )
        except:
            print("Failed to Create Projects Table")
            self.DB.commit()

    def DeEncryptData(self):
        pass

    def EncryptData(self):
        pass

    def UpdateCheck(self):
        # Check for Latest Github Release
        pass
