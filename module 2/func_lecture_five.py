'''
assume joe makes $10,000 in salary. he spends equal time in california and in pennsylvania. 
therefore, he would be liable to pay state tazes in both states for 1/2 time in california and 1/2 in pennsylvania.
california has 10% state tax while pennsylvania has 3% state tax.
calculate his state taxes
'''

def cali_tax():
    rate = 0.1
    return rate
    
def penn_tax(): 
    rate = 0.03
    return rate

joe_taxes = (1/2*(10000.0)*penn_tax()) + (1/2*(10000.0)*cali_tax())

print("joe owes: ", joe_taxes)