# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:10:01 2018

class test

@author: MCA
"""


class First(object):
    
    def __init__(self):
        
        self.A = "A"
    
    def method_first(self):
        
        print("method first", self.A)
    
class Second(First):
    
    def __init__(self, First):
        First.__init__(self)
        self.B = "B"
        self.method_sec()
        
    def method_sec(self):
        
        print(self.A)

        
def main():
    
    create_obj_class_first = First()
    create_obj_class_first.method_first()
    create_obj_class_sec = Second(First)
#    create_obj_class_sec.method_sec()
    
if __name__ == "__main__":
    main()