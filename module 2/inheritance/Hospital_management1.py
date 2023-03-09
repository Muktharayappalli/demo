#Define Multilevel Inheritance in Hospital management
class Hospital:             #Parent Class
    def __init__(self):
        self.hname = ""
    def setHospitalname(self):
        self.hname = input("Enter Hospital Name:")
    def showHospitalname(self):
        print("HOSPITAL NAME:", self.hname)

class HospitalLocation(Hospital):
    def __init__(self):
        self.hlocation = ""
    def setHospitalLocation(self):
        self.setHospitalname()
        self.hlocation = input("Enter Hospital Location:")
    def showHospitalLocation(self):
        self.showHospitalname()
        print("HOSPITAL LOCATION:", self.hlocation)

class PatientSection(HospitalLocation):
    def __init__(self):
        self.sname = ""
        self.sdoctor = ""
    def setSection(self):
        self.setHospitalLocation()
        self.sname = input("Enter Section Name:")
        self.sdoctor = input("Enter Doctor Name:")
    def showSection(self):
        self.showHospitalLocation()
        print("SECTION NAME:", self.sname)
        print("DOCTOR NAME:", self.sdoctor)

class PatientDetails(PatientSection):
    def __init__(self):
        self.pname = ""
        self.pgender = ""
    def setPatient(self):
        self.setSection()
        self.pname = input("Enter Patient Name:")
        self.pgender = input("Enter Patient Gender:")
    def showPatient(self):
        self.showSection()
        print("PATIENT NAME:", self.pname)
        print("PATIENT GENDER:", self.pgender)

obj2 = PatientDetails()
obj2.setPatient()
obj2.showPatient()