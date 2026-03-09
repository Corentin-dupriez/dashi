import argparse
from datasources import Datasources
from dashboard import Dashboard


def dashi_build():
    data_sources = Datasources()  # print(data_sources[0].data)
    dashboard = Dashboard(data_sources)
    print(dashboard.charts)
    for chart in dashboard.charts:
        print(chart.to_json())


def main():
    parser = argparse.ArgumentParser("dashi")
    parser.add_argument("build")
    args = parser.parse_args()

    if args.build:
        dashi_build()


if __name__ == "__main__":
    main()
