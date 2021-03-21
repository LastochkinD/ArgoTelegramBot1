import fdb
from datetime import timedelta, datetime


class DataProvider:
    def __init__(self):
        self.con = fdb.connect(dsn='localhost:D:/dima/db/tempdb.fdb', user='sysdba', password='masterkey')
        self.cur = self.con.cursor()

    def get_zn_data(self, zn_num):
        self.cur.execute("select first 1 service.id, service.num, service.data_isp, service.avto_id, models.model_name, " +
                         "avto.nomer, marks.mark_name, avto.vin " +
                         "from service " +
                         "left outer join avto on (service.avto_id = avto.id)" +
                         "left outer join models on (avto.model_id = models.id)" +
                         "left outer join marks on (models.mark_id = marks.id) where num='" + str(zn_num) + "'")
        s = self.cur.fetchone()
        if s is None:
            return ""
        else:
            return s
