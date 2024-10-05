class Fibonacci:
    def __init__(self, num, list = None):
        self.num = num
        self.list = list

    def generationFibonacci(self):

        num1= 1
        num2=1
        self.list = [0,num1,num2]

        for i in range(3, self.num):
            num3 = num1 + num2
            num1 = num2
            num2 = num3

            self.list.append(num2)


    def showInfo(self):

        print(f'{self.list}')


obj = Fibonacci(100)

obj.generationFibonacci()

obj.showInfo()
