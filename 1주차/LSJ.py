class Calculator:
    def __init__(self): #self는 객체 자신을 가리킴 #self가 없으면 객체의 변수가 아니라 지역변수로 인식
        self.result = 0  #attribute 속성
    
    def add(self, num): #객체에 숫자를 더해주는 함수 #메소드
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        self.result *= num
        return self.result
    
    def div(self, num):
        self.result /= num
        return self.result
    