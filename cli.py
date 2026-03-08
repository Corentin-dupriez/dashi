import argparse
from datasources import Datasources


def dashi_build():
    data_sources = Datasources().load_sources()
    print(data_sources[0].data)


def main():
    parser = argparse.ArgumentParser("dashi")
    parser.add_argument("build")
    args = parser.parse_args()

    if args.build:
        dashi_build()


if __name__ == "__main__":
    main()
