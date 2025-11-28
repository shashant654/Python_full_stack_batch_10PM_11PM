0
1
2
3
4

i = 0

while(i < 5 ):
      print(i)
      i + = 1

NOTE: in Python , i++ OR ++i => are not supported , 
so we have write i = i + 1 OR i += 1

i ++ OR i = i + 1 OR i += 1

i++ => post increment operator
++i => pre increment operator  ( Higher Priority)

#include <stdio.h>

int main()
{
    
     int a = 5;
    //   printf("a = %d\n", ++a); // 6
    printf("a = %d\n", a++);  // 5
     printf("a = %d\n", a);  // 6
    return 0;
}

priority of print stmt is greater than post increment operator.



i = 0

while(i < 5 ):
      print(i)
      i + = 1

1. initialization , i = 0
2. condition check , ( i < 5 ) 
3. perform task , print(i)
4. increment loop variable , by 1 ( i = i+1)



i = 0

while(i < 5 ):
      print(i)
      i + = 1

phase 1

1. initialization , i = 0
2. condition check , ( i < 5 ) , 0 < 5 => TRUE
3. perform task , print(i)   , 
4. increment loop variable , 0 = 0 + 1 => 1

Phase 2

1. initialization , i = 1
2. condition check , ( i< 5) , 1 < 5 , => TRUE
3. perform task, print(i)
4. increment loop variable , 1 ++ => 2

Phase 3

1. initialization , i = 2
2. condition check , ( i< 5) , 2 < 5 => TRUE 
3. perform task , print(i)
4. increment loop variable, 2 ++ => 3

PHase 4
1. initialization , i = 3
2. condition check , ( i< 5) , 3 < 5 => TRUE 
3. perform task , print(i)
4. increment loop variable, 3++ => 4

Phase 5 
1. initialization , i = 4
2. condition check , ( i< 5) ,4 < 5 => TRUE 
3. perform task , print(i)
4. increment loop variable, 4++ => 5

Phase 6

1. initialization , i = 5
2. condition check , ( i< 5) , 5 < 5 => FALSE 
3. we exit from the loop



