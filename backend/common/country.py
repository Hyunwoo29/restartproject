#상속 클래스 연습

class Country(object):
    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('국가 클래스의 메소드입니다.')

class Korea(Country):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'국가 이름은 : {self.name}')

def main():
    k = Korea("대한민국")
    k.show_name()

main()