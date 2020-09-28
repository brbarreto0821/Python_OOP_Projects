from IPython.display import clear_output

class Password:
    def __init__(self):
        self.password = input("Write a password: ")

    def caps(self, password):
        caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        global cc   # checks for caps
        cc = 0
        for i in self.password:
            if i in caps:
                cc += 1
        
    def special(self, password):
        special = "!@#$%&*"
        global cs   # checks for special characters
        cs = 0
        for i in self.password:
            if i in special:
                cs += 1

    def numbers(self, password):
        num = "0123456789"
        global cn   # checks for numbers
        cn = 0
        for i in self.password:
            if i in num:
                cn += 1

    def validator(self):
        valid = True
        while valid:
            self.caps(self.password)
            self.numbers(self.password)
            self.special(self.password)
            if cn >= 2 and cs >= 2 and cc > 0 and len(self.password) >= 7:
                clear_output()
                print(self.password)
                print("Strong")
                break
            else:
                clear_output()
                print(self.password)
                print("Weak")
                print("Password requires one cap, two special characters, and two numbers")
                self.password = input("Write a password: ")
                
password = Password()
password.validator()