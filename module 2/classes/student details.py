class studentdetails:
    def __init__(self,name,mob_no,course,address,collage):
        self.Name=name
        self.Mob_no=mob_no
        self.Course=course
        self.Address=address
        self.Collage=collage
    def displaydata(self):
        print("name=",self.Name)
        print("mob_no=",self.Mob_no)
        print("course=",self.Course)
        print("address=",self.Address)
        print("collage=",self.Collage)
obj=studentdetails("mukthar",994335533,"python","ayappali","mes")
obj.displaydata()
