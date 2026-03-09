import argparse
from datasources import Datasources
from dashboard import Dashboard
from render import render_dashboard


def dashi_build():
    data_sources = Datasources()  # print(data_sources[0].data)
    dashboard = Dashboard(data_sources)
    charts = [
        {"id": f"chart_{i}", "spec": chart.to_dict()}
        for i, chart in enumerate(dashboard.charts)
    ]
    render_dashboard(dashboard, charts)


def main():
    parser = argparse.ArgumentParser("dashi")
    parser.add_argument("build")
    args = parser.parse_args()

    if args.build:
        dashi_build()


if __name__ == "__main__":
    main()
