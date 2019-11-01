class displayNameAndAge():
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
        print("Hello world")

    def displayNameAge(self):
        print("My name is",self.Name,self.Age,"+ years of age." "Young,right" )
class displayMean():
    def dispMean(self):
        list1=[12,4,56,17,8,99]
        self.sum_of_list=sum(list1)
        print("")
        self.mean=(self.sum_of_list/6)
        print("The maximum number in this list: [12, 4, 56, 17, 8, 99] is",max(list1))
        print("The mean:[12, 4, 56, 17, 8, 99] is",self.mean,"\n")
    def Alphabet(self):
        print("A for Apple\n","\nB for Boy","\nC for Cow","\n...","\nZ for Zebra")

Obj= displayNameAndAge("Stan",20)
Obj.displayNameAge()
Obj2=displayMean()
Obj2.dispMean()
Obj2.Alphabet()
