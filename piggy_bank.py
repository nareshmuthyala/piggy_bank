#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Account:
    
    def __init__(self, bal):
        self.bal = 0.0
        
    def deposit(self, amount):
        self.bal+=amount
        print('After adding, your updated balance is {} rupees'.format(self.bal))
        
    def withdraw(self, amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('After withdrawing, balance amount is {} rupees'.format(self.bal))
        else:
            print('Insufficient amount to withdraw')
            
    def check_balance(self):
        print('Your current balance is {} rupees.'.format(self.bal))
     
acc = Account(0)    
while(True):
    x = input('Start or End : ').lower()
    print('')
    if(x=='start'):
        ops = input('Add, Withdraw or Check : ').lower()
        print('')
        if(ops=='add'):
            add_amt = float(input('Add amount : '))
            acc.deposit(add_amt)
        elif(ops=='withdraw'):
            withdraw_amt = float(input('Withdraw amount : '))
            acc.withdraw(withdraw_amt)
        elif(ops=='check'):
            acc.check_balance()
    else:
        break

