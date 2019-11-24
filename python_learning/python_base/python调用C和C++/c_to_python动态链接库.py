#1.创建 C语言文件：pycall.c
"""
#include <stdio.h>
#include <stdlib.h>
int add(int a, int b)
{
  printf("you input %d and %d\n", a, b);
  return a+b;
}

"""
# 2.gcc编译生成动态库libpycall.so文件 : gcc -o libpycall.so -shared -fPIC pycall.c

#3.python加载动态库文件，从而调用C语言代码块
"""
import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("/home/oldeleven/test_C_to_Python/libpycall.so")  # 加载c语言动态链接库
result = lib.add(1, 3) # 调用动态链接库中的方法模块
print(result)

"""