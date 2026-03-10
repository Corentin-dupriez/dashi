import typer
import plotly.io as pio
from .datasources import Datasources
from .dashboard import Dashboard
from .render import render_dashboard
from .serve import serve as serve_dashboard

app = typer.Typer()


@app.command()
def init():
    print("Initializing dashi")


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


if __name__ == "__main__":
    app()
