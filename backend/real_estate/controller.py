from real_estate.dataset import Dataset
from real_estate.housing import Housing


class Controller(object):

    @staticmethod
    def main():
        while 1:
            menu = input('0.Exit 1.모델생성 2.DF 생성')
            if menu == '0':
                break
            elif menu == '1':
                housing = Housing()
                dataset = Dataset()
                dataset.housing = housing.new_model('housing')
                print(dataset.housing)
            elif menu == '2':
                print('*' * 100)
                print(f'1. Housing 의 type 은 \n {type(this)} 이다.')
                print(f'2. Housing 의 column 은 \n {this.columns} 이다.')
                print(f'3. Housing 의 상위 1개 행은 \n {this.head()} 이다.')
                print(f'4. Housing 의 null 의 갯수\n {this.isnull().sum()}개')
            else:
                continue



Controller.main()