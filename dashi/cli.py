import typer
import plotly.io as pio

from dashi.structure.cleaner import clean_builds
from .datasources import Datasources
from .dashboard import Dashboard
from .render import render_dashboard
from .serve import serve as serve_dashboard
from .structure.initializer import (
    create_dashboard_template,
    structure_already_present,
    create_structure,
)

app = typer.Typer()


@app.command()
def init() -> None:
    """
    Initializes dashi folder structure.
    If the structure is already present, it will be skipped.
    After creating the structure, creates the dashboard template, which will be used to generate new dashboards.
    """
    if not structure_already_present():
        create_structure()
    else:
        print("Structure is already present, skipping creation")

    create_dashboard_template()


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
    """
    Creates a simple server to display the generated dashboards
    """
    serve_dashboard()


@app.command()
def clean() -> None:
    """
    Cleans the dashboard folder from the generated dashboards.
    """
    clean_builds()


if __name__ == "__main__":
    app()
