'''
lecture 9
'''

'''
class car:
    maker = 'toyota'
    def report_maker(self):
        return self.maker
    
my_car = car()
print(my_car.maker)
print(my_car.report_maker())
'''

class car:
    maker = 'toyota'
    def __init__(self, input_model):
        self.model = input_model
    def report(self):
        return self.maker, self.model
        
#my_corolla = car('corolla')
#my_highlander = car('highlander')

#print(my_corolla.maker, my_corolla.model)
#print(my_highlander.maker, my_highlander.model)

#call the method
#print(my_corolla.report())

#change the attribute
#my_corolla.maker = 'ford'

#print(my_corolla.maker)
#print(my_corolla.report())
