class Generator:
    def __init__(self, a, b, c, d, m):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.m = m
    
    
    def generate_num_cycle(self, am_of_int, default_num=0)->int:
        res = 0
        if default_num == 0:
            default_num = self.a + self.b + self.c + self.d + self.m
            
        for i in range(am_of_int+1):
            if i == 0:
                res = default_num
            else: 
                res = (self.a*(res**3) + self.b*(res**2) + 
                        self.c * res + self.d) % self.m
        return (res)
            
    def generate_list(self, size)->list[int]:
        result = list()
        for i in range(1,size):
            result.append(self.generate_num_cycle(i))
        return result
    