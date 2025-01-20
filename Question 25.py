'''Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance
    parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later'''

class MyClass:
    
    class_parameter = "I am a class parameter"

    def __init__(self, instance_parameter):
       
        self.instance_parameter = instance_parameter


my_instance = MyClass("I am an instance parameter")


print(MyClass.class_parameter)  


print(my_instance.instance_parameter) 


my_instance.instance_parameter = "New instance parameter value"
print(my_instance.instance_parameter)  
