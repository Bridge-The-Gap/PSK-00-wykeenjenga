class displayNameAndAge():
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
        print("Hello world")

    def displayNameAge(self):
        print("My name is",self.Name,self.Age,"+ years of age." "Young,right?" )
class displayMean():
    def dispMean(self):
        list1=[12,4,56,17,8,99]
        print("")
        self.mean=(sum(list1)/6)
        print("The maximum number in this list: [12, 4, 56, 17, 8, 99] is",max(list1))
        print("The mean:[12, 4, 56, 17, 8, 99] is",self.mean,"\n")
        
    def Alphabet(self):
        Alp_dict={
            "a":"A for Apple",
            "b":"B for Boy",
            "c":"C for Cow",
            ".":"...",
            "z":"Z for Zebra"}
        
        for x in Alp_dict:
            print(Alp_dict[x])

Obj= displayNameAndAge("Stan",20)
Obj.displayNameAge()
Obj2=displayMean()
Obj2.dispMean()
Obj2.Alphabet()
