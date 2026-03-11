import typer
import plotly.io as pio
from .datasources import Datasources
from .dashboard import Dashboard
from .render import render_dashboard
from .serve import serve as serve_dashboard
from .project_initializer import structure_already_present, create_structure

app = typer.Typer()


@app.command()
def init():
    if not structure_already_present():
        create_structure()
    else:
        print("Structure is already present, skipping creation")


@app.command()
def build():
    data_sources = Datasources()
    dashboard = Dashboard(data_sources)
    charts = [
        {"id": f"chart_{i}", "figure": pio.to_json(chart)}
        for i, chart in enumerate(dashboard.charts)
    ]
    render_dashboard(dashboard, charts)


@app.command()
def serve():
    serve_dashboard()


@app.command()
def clean():
    pass


if __name__ == "__main__":
    app()
