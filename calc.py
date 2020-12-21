import sqlite3

class calculation():
    def sqlbyreq(self, num_train):
        db = sqlite3.connect('checkfuel.db')
        sql = db.cursor()
        sql.execute(f"""SELECT *
                        FROM trains
                        WHERE tr_num = '{num_train}'
                        GROUP BY tr_station""")
        results = sql.fetchall()
        print(results)
        db.commit()
        db.close()
