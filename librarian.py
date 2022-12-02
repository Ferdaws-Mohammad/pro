class librarian():
    librarian_list = []
    idCounter = 0
    def __init__(self,fullName:str,age:str,id_no:str,employmentType:bool):
        self.employmentType=employmentType
        self.fullName = fullName
        self.age = int(age)
        self.id_no = int(id_no)
        self.phoneNumber = phoneNumber
        def addNewlibrarian(self, fullName: str, age: str, id_no: str, phoneNumber: str,employmentType:bool):
            if fullName.isspace() or fullName == None and age.isspace() or age == None and id_no == None and id_no.isspace() and phoneNumber.isspace() or phoneNumber == None:

                print('invalid value')
            else:
                lib = librarian(self, fullName=fullName, age=age, id_no=id_no, phoneNumber=phoneNumber, id=self.id_counter)
                self.idCounter += 1
                self.librarian_list.append(self, lib)
