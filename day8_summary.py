signal_state = "Red"
if signal_state == "Green":
    print("Walk")
else:
    print("Wait")
print("Look both ways")

class Points(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 
p1 = Points("A", "B") 
p1.print_point()

class Points(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 
p2 = Points(1, 2) 
p2.x = 'A' 
p2.print_point()