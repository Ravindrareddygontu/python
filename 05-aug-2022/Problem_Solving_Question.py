'''Problem Statement: Write a program to build a simple Student Management System using Python which can perform the following operations in oops concepts 

1.Accept
2.Display
3.Search
4.Delete
5.Update'''

class Student:
    def __init__(self,lst):
        self.lst = lst

    def accept(self, value):
        self.lst.append(value)

    def disp(self):
        print(self.lst)

    def search(self,value):
        if value in self.lst:
            print('it is there in the record')

        else:
            print('not there in the record')

    def delete(self,value):
        if value in self.lst:
            self.lst.remove(value)

        else:
            print('given record is not there')

    def update(self,value,update):
        
        for i in range(len(self.lst)):
            if self.lst[i]==value:
                self.lst[i]=update

obj = Student(['ram','sita','man','india','america'])
obj.disp()
obj.accept('krishna')
obj.disp()
obj.search('india')
obj.search('mango')
obj.delete('man')
obj.disp()
obj.update('ram', 'ramakrishna')
obj.disp()
