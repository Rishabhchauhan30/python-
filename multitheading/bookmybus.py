from threading import *

class MyBus:
    def buy(self):
        print('confirming the seat')
        print('processing the payment')
        print('printing tha ticket')
        
obj = MyBus()
t1 = Thread(target=obj.buy())
t2 = Thread(target=obj.buy())
t3= Thread(target=obj.buy())

t1.start()
t2.start()
t3.start()

