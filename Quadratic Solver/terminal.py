class Quadratic:
    def __init__(self):
        print("This is a quadratic solver")

        print("Type in help to see operations to perform on Q-Equation!")
        print("But first Put in Q-equation")
        self.get_values()
        self.solution("root",True)

    def get_values(self):
        self.a = self.format_value(input("a, coefficient of x^2: "))
        while self.a == False: self.a = self.format_value(input("a, coefficient of x^2: "))
        
        self.b = self.format_value(input("b, coefficient of x: "))
        while self.b == False: self.b = self.format_value(input("b, coefficient of x: "))
        
        self.c = self.format_value(input("c, constant: "))
        while self.c == False: self.c = self.format_value(input("c, constant: "))

        self.a = self.format_float(self.a)
        self.b = self.format_float(self.b)
        self.c = self.format_float(self.c)
        
    def format_value(self,data,data_type=float):
        try:
            data = data_type(data)
            if type(data) == data_type:
                return data
        except Exception as e:
            print("Invalid Input!")
            return False

    def format_float(self,value):
        if value%1 == 0:
            return int(value)
        else:
            return value
        
    def solution(self,solution_type="root",show_solution=False):
        if solution_type == "root":
            self.x1 = (((-1*self.b) + ((self.b**2)-(4*self.a*self.c))**0.5)/(2*self.a))
            self.x2 = (((-1*self.b) - ((self.b**2)-(4*self.a*self.c))**0.5)/(2*self.a))
            print(self.x1,self.x2)
            if show_solution ==  True:
                print()
                print("Solution")
                print("=============")
                print("{}x^2 + ({}x) + ({}) = 0".format(self.a,self.b,self.c))
                print()
                print("find sum and product for coefficient of x: {}".format(self.b))
                sp1 = self.format_float((-1*self.x1))
                sp2 = self.format_float((-1*self.x2))
                s = sp1 + sp2
                p = sp1 * sp2

                s = self.format_float(s)
                p = self.format_float(p)
                print("sum: {} + {} = {} and ".format(sp1,sp2,s))                
                print("product: {} X {} = {}".format(sp1,sp2,p))
                for n in [sp1,sp2]:
                    if n < self.a:
                        coeff1 = n
                    else:
                        coeff1 = n

                coeff2 = [sp1,sp2][(([sp1,sp2].index(coeff1)+1)%2)]
                print()
                print("break down {} to sum and product".format(self.b))
                print("{}x^2 + ({}x) + ({}x) + ({}) = 0".format(self.a,coeff1,coeff2,self.c))
                if abs(self.a) < abs(coeff1):
                    div1 = self.format_float(coeff1/self.a)
                    a = self.a
                    b = 1
                    c = div1
                else:
                    div1 = self.format_float(self.a/coeff1)
                    a = coeff1
                    b = div1
                    c = 1

                if abs(self.c) < abs(coeff2):
                    div2 = self.format_float(coeff2/self.c)
                    d = self.c
                    e = 1
                    f = div2
                else:
                    div2 = self.format_float(self.c/coeff2)
                    d = coeff2
                    e = div2
                    f = 1
                print()
                print("factorizing...")
                print("({}x)[({}x) + ({})] + ({})[({}x) + ({})] = 0".format(a,b,c,d,e,f))
                print("[({}x) + ({})][({}x) + ({})] = 0".format(a,d,b,c))
                print()
                print("spliting equation to obtain roots...")
                print("({}x) + ({}) = 0 and ({}x) + ({}) = 0".format(a,d,b,c))
                print("{}x = {} and {}x = {}".format(a,(-1*d),b,(-1*c)))
                print("x = {} / {} and x = {} / {}".format((-1*d),a,(-1*c),b))
                print("x = {} and x = {}".format(((-1*d)/a),((-1*c)/b)))
Quad = Quadratic()
