class MathDojo:
    def __init__(self):
        self.result = 0
        
    def add(self,num, *nums):
        self.result += num
        for numb in nums:
            self.result += numb
        return self
    def subtract(self,num, *nums):
        self.result -= num
        for numb in nums:
            self.result -= numb
        return self
    
md = MathDojo()

md.add(2,3,4).add(5,3,8).add(7,9,10).subtract(5,7,10).subtract(4,1,60).subtract(5,3,2)
print(md.result)
