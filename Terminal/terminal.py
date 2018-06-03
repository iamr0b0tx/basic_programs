import subprocess

class terminal:
    def __init__(self):
        self.cmd = input(">>> ")
        self.end = ["quit","exit","end"]
        while self.cmd not in self.end or cmd.lower() not in self.end:
            try:
                self.run_cmd = subprocess.check_output(self.cmd,shell=True)
                self.output = self.run_cmd.decode()
            except Exception as e:
                self.output = self.run(self.cmd)
                if self.output == False:
                    self.output = "Command is not recognized"
            print()    
            print(self.output)
            self.cmd = input("\n>>> ")

    def run(self,cmd):
        try:
            return eval(cmd)
        except Exception as e:
            return False

TERMINAL = terminal()
