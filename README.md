# dashi

dashi is a dashboard-as-code application that allows you to create dashboards
from yaml files. It used Polars for fast and efficient dataframe processing,
and Altair for visualisation.

## Status

⚠️ dashi is currently in early development.
The API and configuration format may change.

## Philosophy

dashi follows a **dashboard-as-code** approach.

Instead of building dashboards through a GUI, dashboards are defined
as YAML files that can be versioned, reviewed, and deployed like code.

This allows dashboards to be:

- version controlled
- reproducible
- easy to review in pull requests

## How to use

### Configuring data sources

The first step of creating visualisations is done by defining data sources.
This should be done in the data_sources folder as yaml files.
The file should contain the datasource name, type and columns
(containing the name of the column and the data type)

```yaml
datasource:
  name: sample_data
  type: csv
  columns:
    - name: id
      type: integer
    - name: name
      type: string
```

For the moment, only the csv datasource type is supported,
but more formats will be supported soon.
The datasource name must match the filename (without the extension)
of the data file stored in the `staging_data` folder.
When using the `dashi build` command, dashi
will then look within the staging_data folder, and generate a polars dataframe
by using the defined schema.

### Configuring the dashboards

Once the datasources are defined, the dashboard itself can be defined within the
`dashboards` folder as a yaml file. Each yaml file should correspond to
one dashboard, but each dashboard is composed of several charts.
The file should contain the dashboard name, as well as a list of charts.
Each chart should be defined with:

- title
- chart type (ex: line, bar)
- datasource (corresponding to a datasource defined in `data_sources`)
- x (corresponding to a column defined for the datasource)
- y (corresponding to a column defined for the datasource)

```yaml
dashboard: 
  title: sample_dashboard

  charts: 
    - name: sample_chart
      type: line
      datasource: sample_data
      x: time
      y: profit
```

### dashi build

Once both datasources and dashboards have been defined, the `dashi build`
command can be used to create the dashboards based on the provided definitions
