'''
패키지package - 관련있는 모듈을 그룹으로 관리할 수 있다.(모듈이 많아지면 구분하기 위해서 간단히 관리, 정리)
directory - package - module
'''

from CalculaotrForInt import addCal
from CalculaotrForInt import subCal
from CalculaotrForInt import mulCal
from CalculaotrForInt import divCal

print(addCal.add(10, 20))
print(subCal.sub(10, 20))
print(mulCal.mul(10, 20))
print(divCal.div(10, 20))

from CalculaotrForFloat import addCal
from CalculaotrForFloat import subCal
from CalculaotrForFloat import mulCal
from CalculaotrForFloat import divCal

print(addCal.add(10, 20))
print(subCal.sub(10, 20))
print(mulCal.mul(10, 20))
print(divCal.div(10, 20))