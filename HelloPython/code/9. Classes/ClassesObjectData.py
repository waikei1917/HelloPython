class Example:
    def __init__(self, **kwargs): #two stars for dict, one star for tuple
        self.variables = kwargs
        
    def set_vars(self,k,v):
        self.variables[k] = v
        
    def get_vars(self,k):
        return self.variables.get(k, None)
    
var = Example(age=17, gender='male')
var.set_vars('name', 'alex')

print(var.get_vars('name'))
print(var.get_vars('age'))
print(var.get_vars('gender'))