from crime_cctv.models import CrimeDTO
from crime_cctv.service import Crimeservice



class CrimeApi(object):

    @staticmethod
    def main():
        util = Crimeservice()
        dto = CrimeDTO()
        while 1:
            menu = input('0-Exit 1- 데이터프레임생성 \n'
                         '2\n'
                         '3')
            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_models('cctv_in_seoul.csv')
                util.print_dframe(dto.dframe)
            elif menu == '2':
                pass
            else:
                continue


CrimeApi.main()