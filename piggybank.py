
# coding: utf-8

# In[7]:

class piggybank:
    balance = 0.00
    yourname = 'XXX'
    
    def __init__(self):
        pass
    
    def setname(self,nm):
        self.yourname = nm
        
    def getname(self):
        return self.yourname
        
    def add(self,add_amt):
        self.balance = self.balance + add_amt
        
    
    def takeout(self,with_amt):
        self.balance = self.balance - with_amt
        
    
    def check_balance(self):
        return self.balance
    
    


# In[ ]:



