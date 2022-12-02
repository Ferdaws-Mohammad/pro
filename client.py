class client:
    client_list=[]
    id_counter=0
    def __init__(self,fullName:str,age:str,id_no:str,phoneNumber:str):
        self.fullName=fullName
        self.age=int(age)
        self.id_no=int(id_no)
        self.phoneNumber=phoneNumber
    def addNewClient(self,fullName:str,age:str,id_no:str,phoneNumber:str):
        if fullName.isspace() or fullName==None and age.isspace() or age==None and id_no==None and id_no.isspace() and phoneNumber.isspace() or phoneNumber==None:
            print('invalid value')
        else:
            cLI = client(self, fullName=fullName, age=age, id_no=id_no, phoneNumber=phoneNumber, id=self.id_counter)
            self.id_counter += 1
            self.client_list.append(self, cLI)