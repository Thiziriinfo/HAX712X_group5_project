from pprint import pformat
import pyodide.http
from shiny import App, reactive, render, ui

villes = [
    "AGDE",
    "ALBI",
    "ALES",
    "ARGELES-GAZOST",
    "AUCH",
    "BELESTA-EN-LAURAGAIS",
    "BESSIERES",
    "BEZIERS",
    "BLAGNAC",
    "CASTRES",
    "CORNEILHAN",
    "GAUDONVILLE",
    "LA CALMETTE",
    "LATTES",
    "LOURDES",
    "LUNEL-VIEL",
    "MIRAMONT-DE-COMMINGES",
    "MONTAUBAN",
    "MONTGISCARD",
    "MONTPELLIER",
    "NIMES",
    "PERPIGNAN",
    "PEYRUSSE-VIEILLE",
    "RODEZ",
    "SAINT-ESTEVE",
    "SAINT-GAUDENS",
    "SAINT-GELY-DU-FESC",
    "SAINT-GIRONS",
    "SAZE",
    "TARBES",
    "TOULOUSE",
]

polluants = ["H2S", "NO", "NO2", "NOX", "O3", "PM10", "PM2.5", "SO2"]

app_ui = ui.page_fluid(
    ui.input_text("selection", "selection", placeholder="critère de selection"),
    ui.output_text_verbatim("info"),
    ui.input_date("x1", "Date de début"),
    ui.input_date_range("x2", "Période"),
    ui.input_selectize("x3", "Selectize (single)", villes),
    ui.input_selectize("x4", "Selectize (single)", polluants),
)

def server(input, output, session):
    @reactive.Calc
    def url():
        return f"https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?select={input.selection()}"

    @reactive.Calc
    async def data():
        response = await pyodide.http.pyfetch(url())
        dat = await response.json()
        return dat

    @output
    @render.text
    async def info():
        if input.selection() == "":
            return ""
        else:
            d=await data()
            data_str = pformat(d)
            return f"Request URL: {url()}\nResult type: {type(data())}\n{data_str}"

app = App(app_ui, server)

