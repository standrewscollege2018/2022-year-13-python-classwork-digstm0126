''' This is a Student Management System using object orientation'''

class Student:
    ''' Student objects have a name, age, phone number, enrolment status
        and a list of their classes '''

    def __init__(self, name, age, phone, classes):
        ''' Set up new student object '''

        self._name = name
        self._age = age
        self._phone = phone
        self._classes = classes
        self._enrolled = True
        self._studintID = 1523
        
        # Append to student_list
        student_list.append(self)

    def get_name(self):
        ''' Return student name'''

        return self._name

    def get_age(self):
        ''' Return student age'''

        return self._age

    def get_phone(self):
        ''' Return student phone number'''

        return self._phone

    def get_enrolled(self):
        ''' Return student enrolment status'''

        return self._enrolled

    def get_classes(self):
        ''' Display a list of classes student is enrolled in '''

        class_list = ""
        for c in self._classes:
            class_list += c + " "
        return class_list

    def get_studintID(self):
        '''gets the studint id'''
    
# List to store students
student_list = []
# List to store all class codes
all_classes = []  


#Create students
Student("John", 16, 275044001,["MATH", "DIGI"])
Student("Jake", 17, 234567, ["DIGI", "PHYS", "BIOL"])

def display_students():
    ''' Display names of all students '''
    for s in student_list:
        print(f"{s.get_name()}")

def display_student(name):
    ''' Display details of selected student '''
    for s in student_list:
        if name in s.get_name():
            print("=" * 30)
            print(f"Name: {s.get_name()}")
            print(f"Age: {s.get_age()}")
            print(f"Phone: {s.get_phone()}")
            print(f"Classes: {s.get_classes()}")
            print("=" * 30)
            print("")

def generate_students():
    ''' Import students from a csv file'''
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('myRandomStudents.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # Loop through the csv, one row at a time
        
        for line in filereader:
            # For each row, we grab the classes in columns D-H and put them into a list
            # the classes therefore can be found in line[3] to line[7]
            classes = []
            i = 3
            while i in range(3,8):
                # Creating a master list of all class codes
                if line[i] not in all_classes:
                    all_classes.append(line[i])
                # Add class to student list of classes    
                classes.append(line[i])
                i += 1
                # Create a new student object
            
            Student(line[0], int(line[1]), int(line[2]), classes)

def class_search():
    ''' This function gets the user to choose a class code from a list and
        returns the names of all students enrolled in that class
        It should also return a count of the number of students found '''

    print("Select the class:")
    for c in range(len(all_classes)):
        print(f"{c+1}. {all_classes[c]}")
    selection = int(input("Class number: "))
    count = 0
    for s in student_list:
        if all_classes[selection-1] in s.get_classes():
            count += 1
            print(s.get_name())
    print(f"{count} students found")

def add_student():
    ''' Function enables us to add a new student '''

    name = input("Name: ")
    age = int(input("Age: "))
    phone = int(input("Phone: "))
    classes = []
    ask_class = True
    while ask_class == True:
        c = input("Enter class code (-1 to end): ")
        if c == "-1":
            ask_class = False
        else:
            classes.append(c)

    Student(name, age, phone, classes)
              
def delete_student():
    ''' Delete a student by finding them by name and deleting them from the student_list '''


def update_student():
    ''' Choose what to update (name, age, phone), then enter the new info.
        Then call a setter function on the object itself to set the new value '''

    
    

    

generate_students()

run_program = True
while run_program:
    print("1. Add student\n2. Class lists\n3. Search for student\n4. Display all students\n5. Quit")
    selection = int(input())
    if selection == 1:
        add_student()
    elif selection == 2:
        class_search()
    elif selection == 3:
        name = input("Enter name: ")
        display_student(name)
    elif selection == 4:
        display_students()
    else:
        run_program = False



