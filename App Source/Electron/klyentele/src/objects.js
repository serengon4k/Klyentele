export class User{
    constructor(firstName, lastName, Dob, UID, PhoneNumber, Email, Permissions) { 
        this.firstName = new String(firstName);
        this.lastName = new String(lastName);
        this.Dob = new Date(Dob);
        this.UID = new String(UID);
        this.PhoneNumber = new String(PhoneNumber);
        this.Email = new String(Email);
        this.Permissions = new Map();
    }

    getFullName() { 
        return `${this.firstName} ${this.lastName}`
    }

    getCurrentAge() { 
        const TodaysDate = new Date()
        var Difference_In_Time = this.Dob.getTime() - TodaysDate.getTime;
        // To calculate the no. of days between two dates
        var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);

        // Return Years
        return Difference_In_Days / 365
    }
}

export class Project { 
    constructor(AssignedUsers, ClientID, ClosingDate, CreationDate, DueDate, ExpenseLog, ProjectBudget, ProjectManagerUID, ProjectName, isComplete, ProjectID) {
        this.AssignedUsers = new Array(AssignedUsers);
        this.ClientID = new String(ClientID);
        this.ClosingDate = new Date(ClosingDate);
        this.CreationDate = new Date(CreationDate);
        this.DueDate = new Date(DueDate);
        // TODO Figure this out
        this.ExpenseLog = new Array(ExpenseLog);
        this.ProjectBudget = new Number(ProjectBudget);
        this.ProjectManager = new String(ProjectManagerUID);
        this.ProjectName = new String(ProjectName);
        this.isComplete = new Boolean(isComplete);
        this.ProjectID = new String(ProjectID)
    }
}

export class Client { 
    constructor(Budget, Comments, Dob, Email, FirstName, LastName, IsInGoodStanding, PhoneNumber) {
        this.Budget = new Number(Budget);
        this.Comments = new String(Comments);
        this.Dob = new Date(Dob);
        this.Email = new String(Email)
        this.FirstName = new String(FirstName);
        this.LastName = new String(LastName);
        this.IsInGoodStanding = new Boolean(IsInGoodStanding);
        this.PhoneNumber = new String(PhoneNumber);
    }
    getFullName() { 
        return `${this.FirstName} ${this.LastName}`
    }

    getCurrentAge() { 
        const TodaysDate = new Date()
        var Difference_In_Time = this.Dob.getTime() - TodaysDate.getTime;
        // To calculate the no. of days between two dates
        var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);

        // Return Years
        return Difference_In_Days / 365
    }
}