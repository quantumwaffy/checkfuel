import sqlite3
import random as rd
class calculation():
    db = sqlite3.connect('checkfuel.db')
    sql = db.cursor()
    results = []
    def sqlbyreq(self, num_train):
        self.sql.execute(f"""SELECT *
                        FROM trains
                        WHERE tr_num = '{num_train}'
                        GROUP BY tr_station""")
        self.results = self.sql.fetchall()
        print(self.results)
        self.db.commit()
        self.db.close()

    def maketrainsql(self):
        for i in range(0,100,1):
            j = rd.randrange(0,9,1)
            self.sql.execute(f"""INSERT INTO trains (tr_id, tr_num, tr_station, tr_operation, tr_date, 
                    tr_vagons, tr_hvags, tr_lvags, tr_serloc, tr_numloc) VALUES 
                    ('9999999999999999999999999',
                    '2609',
                    '13850{j}',
                    'P0002',
                    '2020-10-19-06.52.00.000000',
                    '61',
                    '32',
                    '29',
                    '240',
                     '06151')""")
            print(j)
        self.db.commit()
        self.db.close()

    def seestation(self):
        for el in self.results:
            print(el[3])


