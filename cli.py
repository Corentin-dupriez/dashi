import typer
from datasources import Datasources
from dashboard import Dashboard
from render import render_dashboard

app = typer.Typer()


@app.command()
def build():
    data_sources = Datasources()  # print(data_sources[0].data)
    dashboard = Dashboard(data_sources)
    charts = [
        {"id": f"chart_{i}", "spec": chart.to_dict()}
        for i, chart in enumerate(dashboard.charts)
    ]
    render_dashboard(dashboard, charts)


@app.command()
def serve():
    print("Serving")


if __name__ == "__main__":
    app()
