import typer
import plotly.io as pio

from dashi.structure.cleaner import clean_builds
from .datasources import Datasources
from .dashboard import Dashboard
from .render import render_dashboard
from .serve import serve as serve_dashboard
from .structure.initializer import structure_already_present, create_structure
from pprint import pprint

app = typer.Typer()


@app.command()
def init() -> None:
    if not structure_already_present():
        create_structure()
    else:
        print("Structure is already present, skipping creation")


@app.command()
def build() -> None:
    data_sources = Datasources()
    dashboard = Dashboard(data_sources)
    charts = [
        {"id": f"chart_{i}", "figure": pio.to_json(chart)}
        for i, chart in enumerate(dashboard.charts)
    ]
    render_dashboard(dashboard, charts)


@app.command()
def serve() -> None:
    serve_dashboard()


@app.command()
def clean() -> None:
    clean_builds()


if __name__ == "__main__":
    app()
