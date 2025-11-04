from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def read_all_museums():
        print("Executing get_museo()")
        results = []

        cnx = ConnessioneDB().get_connection()

        if cnx is None:
            print("No database connected")
            return None
        else:
            cursor = cnx.cursor(type=dict)
            query = """SELECT *
                    FROM museo"""

            cursor.execute(query)

            for row in cursor:
                museo = Museo(row["id"], row["nome"], row["tipologia"])
                results.append(museo)

            cursor.close()
            cnx.close()
            return results

