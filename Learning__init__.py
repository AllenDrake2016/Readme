class Human():
    def __init__(self,name,gender,**kwargs):
        self.name=name
        self.gender=gender
        self.stream = False
        data = kwargs.pop("data", dict())
        files = kwargs.pop("files", dict())
        print(data)
        print(files)
        data = {'authenticity_token': 'y6O8mKZ7n/jjb4Oz98I3HAA4sckEZsX7nyfYBqg0cqua2HcfV20nJv75/IV6+L3enIpv9nRqu0N+fPE2pRE7+g==', 'login': 'Zihanghuang', 'password': 'xisuo18EX@', 'utf8': '✓', 'commit': 'Sign in'}
        kwargs["data"] = data
        print(kwargs)
        kwargs.setdefault('stream', self.stream)
        print(kwargs)
        #self.information=information

    def speak_name(self):
        print("my name is " + self.name)

    def math_task(self,operation,*args):
        val=operation(*args)
        return val

    def speak(self,text):
        print(text)

    # def input(self, data):
    #     for (name, value) in data.items():
    #         self.information.find("input", {"name": name})["value"] = value


# #will=Human("william","Male","<input class='input1' id='input2' name='input3'>")
# will=Human("william","Male")
# print(will.name,will.gender)
# will.speak_name()
# def add(a,b):
#     return a+b
# value=will.math_task(add,4,5)
# print(value)
#
# a=Human(["<input class='input1' id='input2' name='input3' value='choice'>","<input class='input4' id='input5' name='input6' value='choice'>"],"Male")
# b=a.name#.find("input",{"class":["input1"]})
# print(b)

# will.speak("Hi")

# will = 'asdkhbaksdbk'
#
# if isinstance(will, Human):
#     name = will.name
#     print(name)
# else:
#     print('what???')

Human("william","Male")