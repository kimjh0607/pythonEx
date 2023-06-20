'''
상위클래스(선언만)에서 하위클래스(구현)에 매서드 구현(구체화)을 강요한다.
구현하지않으면 에러 꼭 구현하도록 강요?한다.
이유 - 비행기를(전투기, 여객기 등등) 상속받아서 각자 알아서 입맛에 맞게 고쳐써라.
'''
#추상클래스 문법
from abc import ABCMeta
from abc import abstractmethod
class Airplane(metaclass=ABCMeta):

    @abstractmethod
    def flight(self):
        pass

class Airliner(Airplane):

    def flight(self):
        print('400km/h fly!!')

class Airforce(Airplane):

    def flight(self):
        print('900km/h fly!!')

air1 = Airliner()
air2 = Airforce()
air1.flight()
air2.flight()