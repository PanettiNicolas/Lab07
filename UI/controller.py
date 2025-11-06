import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_musei(self):
        lista_musei = self._model.get_musei()

        opzione_musei_default = [ft.dropdown.Option(key="nessun filtro", text="Nessun filtro")]
        opzioni_musei_dinamiche = [ft.dropdown.Option(key=museo.nome, text=museo.nome) for museo in lista_musei]

        opzioni_musei = opzione_musei_default + opzioni_musei_dinamiche
        self._view._dd_museo.options = opzioni_musei

        self._view._dd_museo.value = None
        self._view.update()


    def popola_dropdown_epoche(self):
        lista_epoche = self._model.get_epoche()

        opzione_epoche_default = [ft.dropdown.Option(key="nessun filtro", text="Nessun filtro")]
        opzioni_epoche_dinamiche = [ft.dropdown.Option(key=epoca, text=epoca) for epoca in lista_epoche]

        opzioni_epoche = opzione_epoche_default + opzioni_epoche_dinamiche
        self._view._dd_epoca.options = opzioni_epoche

        self._view._dd_epoca.value = None
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_museo(self, e):
        value = e.control.value
        if value is None or str(value).lower() == "nessun filtro":
            self.museo_selezionato = None
        else:
            self.museo_selezionato = value

    def seleziona_epoca(self, e):
        value = e.control.value
        if value is None or str(value).lower() == "nessun filtro":
            self.epoca_selezionata = None
        else:
            self.epoca_selezionata = value

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self, e):
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        self._view._list_results.controls.clear()

        try:
            artefatti = self._model.get_artefatti_filtrati(museo, epoca)

            if not artefatti:
                self._view.show_alert("Non sono stati trovati artefatti che soddisfino i filtri")
            else:
                for artefatto in artefatti:
                    self._view._list_results.controls.append(ft.Text(str(artefatto)))

        except Exception as ex:
            self._view.show_alert(ex)

        self._view.update()