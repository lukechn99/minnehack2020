import time
import random

#For generating unique IDs
def generateID(UserID):
    ID = '{0:11}{1:0>6}{2:0>2}'.format(int(time.time()*10**6),234743**(int(UserID)+10)%313853,random.randint(0,99))
    return ID

print(generateID(1))
print(generateID(1))


###DATABASES###

#Already Done: Database for Users
#Class for Users
#Store in Database as: UserName | UserID | Email | Password
#UserName and UserID should be UNIQUE for every user.

db1 = [['Alice',1,'alice001@umn.edu','a'],['Bob',2,'bob002@umn.edu','b'],['Charlene',3,'char003@umn.edu','c']]

#In Progress: Relating Users to their courses
#Class for Courses
#Store in Database as: UserID | Course Code (e.g.XXXX0000)

db2 = [[1,'XXXX0001'],[1,'XXXX0002'],[2,'XXXX0001'],[2,'XXXX0003'],[3,'XXXX0003']]



#Create a New Class For Groups, should have GroupID and Course Code
#Store in Database as: GroupName | GroupID | Course Code
db3 = [['Group1','0000001','XXXX0001'],['Group2','0000002','XXXX0002'],['Group3','0000003','XXXX0003']]

#Create a New Database Table to relate Group and Group Members
#Store in Database as: GroupID | UserID

db4 = [['0000001',1],['0000001',2],['0000002',1],['0000003',3]]

# Copy this for easy reference:
# db1: UserName | UserID | Email | Password
# db2: UserID | Course Code
# db3: GroupName | GroupID | Course Code
# db4: GroupID | UserID




###FUNCTIONS###

#Search Functionality

def getID(UserName, db1):
    #Search for ID
    UserID = False
    for n in range(len(db1)):
        if db1[n][0] == UserName:
            UserID = db1[n][1]
    return UserID

def getName(UserID, db1):
    #Search for Name
    UserName = False
    for n in range(len(db1)):
        if db1[n][1] == UserID:
            UserName = db1[n][0]
    return UserName


def findBuddies(CourseCode, db1, db2):
    #Search for Study Buddies
    Buddies = []
    for n in range(len(db2)):
        if db2[n][1] == CourseCode:
            Buddies.append(getName(db2[n][0], db1))
    return Buddies



#Already Done: Register
def register(UserName, UserID, Email, Password, db1):
    # Add a new user to the User Database
    # Check if User already exists.
    if not getName(UserID, db1) or not getID(UserName, db1):
        db1.append([UserName, UserID, Email, Password])
    

#In Progress: Add/Drop Courses

def add_course(UserName, CourseCode, db1, db2):
    
    # Add the new course
    db2.append([getID(UserName, db1), CourseCode])
    
def drop_course(UserName, CourseCode, db1, db2):
    UserID = getID(UserName, db1)
    
    #Delete the course
    for n in range(len(db2)):
        if db2[n][0] == UserID and db2[n][1] == CourseCode:
            db2.remove(db2[n])

            
#Create New: Create/Delete Group            
def create_group(GroupName, Creator, CourseCode, db1, db3):
    UserID = getID(Creator, db1)
    
    #Generate a unique GroupID
    GroupID = generateID(UserID)
    db3.append([GroupName, GroupID, CourseCode])
    
    #Automatically Join your own group
    join_group(GroupID, Creator, db1, db3, db4)
    
def del_group(GroupID, db3, d4):
    for n in range(len(db3)):
        if db3[n][1] == GroupID:
            db3.remove(db3[n])
    
    #Also Delete all Members in the Course
    for n in range(len(db4)-1,-1,-1):
        
        if db4[n][0] == GroupID:
            print(n)
            db4.remove(db4[n])


#Group Search
def getGroup(GroupID, db3):
    #Search for Name
    Group = False
    for n in range(len(db3)):
        if db3[n][1] == GroupID:
            Group = db3[n][0]
    return Group

#This should be a private function if we use GroupID as private group sharing code (see below join_group()).
def getGroupID(Group, db3):
    GroupID = False
    for n in range(len(db3)):
        if db3[n][0] == Group:
            GroupID = db3[n][1]
    return GroupID

def getMembers(GroupID, db1, db4):
    Members = []
    for n in range(len(db4)):
        if db4[n][0] == GroupID:
            Members.append(getName(db4[n][1],db1))
    return Members
        

#Create New: Join/Leave Group
#WE CAN USE THE GroupID AS A PRIVATE GROUP SHARING CODE
def join_group(GroupID, Name, db1, db3, db4):
    #Check if Group exists:
    if getGroup(GroupID, db3):
        db4.append([GroupID, getID(Name, db1)])

def leave_group(GroupID, Name, db1, db4):
    UserID = getID(Name, db1)
    
    #Delete the User
    for n in range(len(db3)):
        if db4[n][0] == GroupID and db4[n][1] == UserID:
            db4.remove(db4[n])
            
#EXAMPLES
print(getID('Alice',db1))
print(getName(1,db1))
print(findBuddies('XXXX0001', db1, db2))
register('David',4,'david004@umn.edu','d', db1)
print(db1[-1])
add_course('David','XXXX0001', db1, db2)
print(db2[-1])
drop_course('David','XXXX0001', db1, db2)
print(db2[-1])
create_group('Group4', 'David', 'XXXX0001', db1, db3)
print(db3[-1])
print(db3)
print(getGroup('0000001', db3))

a = getGroupID('Group4', db3)
print(a)
join_group(a, 'Alice', db1, db3, db4)
print(db4)
del_group(a, db3, db4)
print(db3)
print(getMembers('0000001', db1, db4))
leave_group(a, 'Alice', db1, db4)
