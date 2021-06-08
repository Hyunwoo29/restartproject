class CommonService(object):
    @staticmethod
    def print_dframe(this):
        print('*' * 100)
        print(f'1. Crime 의 type \n {type(this)} ')
        print(f'2. Crime 의 column \n {this.columns} ')
        print(f'3. Crime 의 상위 1개 행\n {this.head()} ')
        print(f'4. Crime 의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)