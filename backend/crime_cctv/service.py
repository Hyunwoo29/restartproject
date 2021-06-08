from crime_cctv.models import CrimeDTO
from common.services import CommonService
import pandas as pd


class Crimeservice(CommonService):

    dto = CrimeDTO()

    def new_models(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)



