There are 2 types of functions:

1.User provided functions
2.Program functions

Pseudocode:

Module showMessage()
print("Hello World")
End Module

call showMessage()

Nested Module Pseudocode:

Module main()
Display "I have a message for you"
call showMessage()
Display "That's all folks"
End Module

Module showMessage()
Display "Hello world"
End Module

////////////////////////////////////////////////////

Module main()
Display "The sum of 12 and 45 is:"
call showSum(12, 45)
Display "That's all folks"
End Module

Module showSum(Integer num1, Integer num2)
Declare Integer result
Set result = num1 + num2
Display result
End Module
