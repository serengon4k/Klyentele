from Lib.Client import Client as Client
from Lib.Visor import Visor as Visor
from Lib.User import User as User
from Lib.Project import Project as Project
import eel
import os
import sys

# Use the same static files as the original Example

eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
# defining the function for addition of two numbers
def add(data_1, data_2):
    int1 = int(data_1)
    int2 = int(data_2)
    output = int1 + int2
    return output

    # Defining Main


def main():
    # Visor.__init__(Visor)
    #Client.__init__(Client, "")
    #Project.__init__(Project, "")
    #Visor.Login(Visor, "Azura4k", "Speedy")
    # Visor.ListClients(Visor)

    eel.start('main.html', mode='edge',)


# Calling main
main()
