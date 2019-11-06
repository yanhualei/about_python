#! /bin/bash
#! /usr/bin/python
from functools import reduce

result = reduce(lambda x, y: x + y, (i for i in range(1, (10**2)+1)))
print(result)
