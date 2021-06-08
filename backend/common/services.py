class CommonService(object):

    def print_dframe(self):
        print('*' * 100)
        print(f'1. Crime 의 type \n {type(self)} ')
        print(f'2. Crime 의 column \n {self.columns} ')
        print(f'3. Crime 의 상위 1개 행\n {self.head()} ')
        print(f'4. Crime 의 null 의 갯수\n {self.isnull().sum()}개')
        print('*' * 100)