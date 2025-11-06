from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        if museo is None and epoca is not None:
            return self._artefatto_dao.read_artifacts_for_era(epoca)
        elif museo is not None and epoca is None:
            return self._artefatto_dao.read_artifacts_for_museum(museo)
        elif museo is not None and epoca is not None:
            return self._artefatto_dao.read_all_artifacts_for_museum_and_era(museo, epoca)
        else:
            return self._artefatto_dao.read_all_artifacts()


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoche = self._artefatto_dao.read_all_era()
        lista_epoche.sort()
        return lista_epoche


    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        return self._museo_dao.read_all_museums()
