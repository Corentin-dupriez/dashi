import polars as pl


def apply_transforms(dataframe: pl.DataFrame, transforms: dict) -> pl.DataFrame:
    groupby = transforms.get("groupby")
    metrics = transforms.get("metrics")

    if not groupby:
        return dataframe

    aggs = []

    for col, op in metrics.items():
        if op == "sum":
            aggs.append(pl.col(col).sum())
        if op == "count":
            aggs.append(pl.col(col).count())
        if op == "average":
            aggs.append(pl.col(col).mean())
        if op == "median":
            aggs.append(pl.col(col).median())

    return dataframe.group_by(groupby).agg(aggs)
