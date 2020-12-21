from lxml import etree

import sqlite3

class parsing5676(object):

    def __init__(self):
        pass

    def parsingxml(self, xmlFile):
        with open(xmlFile) as f:
            xml = f.read().encode('utf-8')
        parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
        root = etree.fromstring(xml, parser=parser)
        train_dict = {}
        lok_dict = {}
        brig_dict = {}
        for value in root.getchildren():
            if value.tag == "TRAIN":
                for train in value.getchildren():
                    if train.tag == 'LOKOMOTIV':
                        for lok in train.getchildren():
                            if lok.tag == 'BR':
                                for br in lok.getchildren():
                                    brig_dict[br.tag] = br.text
                            lok_dict[lok.tag] = lok.text
                    if not train.text:
                        text = 'None'
                    else:
                        text = train.text
                    train_dict[train.tag] = text
        self.ip = train_dict['IPP']
        self.num = train_dict['NP']
        self.station = train_dict['KSO']
        self.operation = train_dict['KOP']
        self.date = train_dict['DATOP']
        self.vagons = train_dict['KLGP']
        self.hvags = train_dict['KLGRVG']
        self.lvags = train_dict['KLPRVG']
        self.serloc = lok_dict['SER']
        self.numloc = lok_dict['NS']

    def gotosql(self):
        db  = sqlite3.connect('checkfuel.db')
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS trains (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tr_id VARCHAR(16),
                            tr_num VARCHAR(6),
                            tr_station VARCHAR(6),
                            tr_operation VARCHAR(6),
                            tr_date DATETIME,
                            tr_vagons ID,
                            tr_hvags ID,
                            tr_lvags ID,
                            tr_serloc VARCHAR(6),
                            tr_numloc VARCHAR(6))""")
        db.commit()
        sql.execute(f"""INSERT INTO trains (tr_id, tr_num, tr_station, tr_operation, tr_date, 
                    tr_vagons, tr_hvags, tr_lvags, tr_serloc, tr_numloc) VALUES 
                    ('{self.ip}',
                    '{self.num}',
                    '{self.station}',
                    '{self.operation}',
                    '{self.date}',
                    '{self.vagons}',
                    '{self.hvags}',
                    '{self.lvags}',
                    '{self.serloc}',
                     '{self.numloc}')""")
        db.commit()
        db.close()









