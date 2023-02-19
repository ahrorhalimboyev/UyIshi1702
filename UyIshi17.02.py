import mysql.connector
class Database():
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="kino"
        )
        self.cursor=self.mydb.cursor()
        self.create_table()
        self.insert_table()
        self.inner_join()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Janr(janr_id INT AUTO_INCREMENT, janr_name VARCHAR(20), PRIMARY KEY(janr_id))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Cinema(cinema_id INT PRIMARY KEY AUTO_INCREMENT, cinema_name VARCHAR(30), janr_id INT)")
        
    def insert_table(self):
        self.cursor.executemany("INSERT INTO Janr(janr_name) VALUES(%s)",
                                [("Komediya",),
                                 ("Melodramma",),
                                 ("Tragediya",),
                                 ("Triller",),
                                 ("Jangari",),
                                 ("Fantastik",),
                                 ("Hujjatli film",)
                                ])
        
        self.cursor.executemany("INSERT INTO Cinema(cinema_name,janr_id) VALUES(%s,%s)",
                                [("Kusto komandasi",7),
                                ("Afsun",1),
                                ("Lola",6),
                                ("Koinot siri",2),
                                ("Odamiylik",3),
                                ("Ada emas dada",1),
                                ("Izquvar",4),
                                ("Qoidalar",5),
                                ("Poyga",6),
                                ("Omad",4),
                                ("Jodugar",3),
                                ("Kim,Nima,QAyer",7),
                                ("SMS",2)
                                ])
        self.mydb.commit()
        
    def inner_join(self):
        print("Inner Join")
        self.cursor.execute(""" SELECT cinema_id,cinema_name,janr_name FROM Janr
                            INNER JOIN Cinema
                            ON Janr.janr_id=Cinema.janr_id
                            """)
        text=self.cursor.fetchall()
        for i in text:
            print(i)

        self.cursor.execute("DROP TABLE Janr")
        self.cursor.execute("DROP TABLE Cinema")
db=Database()