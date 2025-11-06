from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass  

    # TODO
    @staticmethod
    def read_all_artifacts():                          #Legge tutti gli artefatti dalla tabella artefatto
        print("Executing get_artifacts()")
        results = []

        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("No database connected")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                        FROM artefatto"""

            cursor.execute(query)

            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)

            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def read_all_era():                                #Legge tutte le epoche dalla tabella artefatto
        print("Executing get_era()")
        results = []

        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("No database connected")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT epoca
                       FROM artefatto"""

            cursor.execute(query)

            for row in cursor:
                results.append(row["epoca"])

            cursor.close()
            cnx.close()
            return results


    @staticmethod
    def read_artifacts_for_museum(museum):             #Legge gli artefatti filtrati per museo dalla tabella artefatto
        print("Executing read_artifacts_for_museum()")
        results = []

        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("No database connected")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT A.*
                    FROM artefatto A
                    JOIN museo M ON A.id_museo = M.id
                    WHERE M.nome = %s"""

            cursor.execute(query, (museum,))

            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)

            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def read_artifacts_for_era(epoca):               #Legge gli artfatti filtrati per epoca dalla tabella artefatto
        print("Executing read_artifacts_for_era()")
        results = []

        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("No database connected")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM artefatto
                    WHERE epoca = %s"""

            cursor.execute(query, (epoca,))

            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)

            cursor.close()
            cnx.close()
            return results

    @staticmethod
    def read_all_artifacts_for_museum_and_era(museum, era):              #Legge gli artefatti filtrati per museo e epoca dalla tabella artfatto
        print("Executing read_all_artifacts_for_museum_and_era()")
        results = []

        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("No database connected")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT A.*
                    FROM artefatto A
                    JOIN museo M ON A.id_museo = M.id
                    WHERE M.nome = %s AND A.epoca = %s"""

            cursor.execute(query, (museum, era))

            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatto)

            cursor.close()
            cnx.close()
            return results