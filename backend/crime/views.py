from crime.services import CrimeService


class Crime_Api(object):

    @staticmethod
    def main():
        crimeService = CrimeService()
        while 1:
            menu = input('0-Exit\n1-서울CCTV DF\n2-서울범죄 DF\n'
                         '3-경찰서위치 DF\n4-실업율 DF\n5-엑셀POP')

            if menu == '0':
                break
            elif menu == '1':
                crimeService.show_file({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif menu == '2':
                pass
            else:
                continue


Crime_Api.main()