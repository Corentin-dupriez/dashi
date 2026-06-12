import polars as pl
import pytest
from dashi.transforms.transforms import apply_transforms


@pytest.fixture
def sample_df():
    return pl.DataFrame(
        {"category": ["a", "b", "a", "b", "a"], "value": [1.0, 2.0, 3.0, 4.0, 5.0]}
    )


def test_no_groupby_returns_dataframe_unchanged(sample_df):
    result = apply_transforms(sample_df, {"metrics": {"value": "sum"}})
    assert result.equals(sample_df)


def test_groupby_sum(sample_df):
    result = apply_transforms(
        sample_df, {"groupby": "category", "metrics": {"value": "sum"}}
    )
    assert sorted(result["category"].to_list()) == ["a", "b"]
    assert sorted(result["value"].to_list()) == [6.0, 9.0]


def test_groupby_count(sample_df):
    result = apply_transforms(
        sample_df, {"groupby": "category", "metrics": {"value": "count"}}
    )

    assert sorted(result["category"].to_list()) == ["a", "b"]
    assert sorted(result["value"].to_list()) == [2, 3]


def test_groupby_avg(sample_df):
    result = apply_transforms(
        sample_df, {"groupby": "category", "metrics": {"value": "average"}}
    )

    assert sorted(result["category"].to_list()) == ["a", "b"]
    assert result["value"].to_list() == [3.0, 3.0]


def test_groupby_median(sample_df):
    result = apply_transforms(
        sample_df, {"groupby": "category", "metrics": {"value": "median"}}
    )

    assert sorted(result["category"].to_list()) == ["a", "b"]
    assert result["value"].to_list() == [3.0, 3.0]


def test_groupby_multiple_metrics(sample_df):
    df = sample_df.with_columns(pl.lit(1).alias("count_col"))
    result = apply_transforms(
        df,
        {"groupby": "category", "metrics": {"value": "sum", "count_col": "count"}},
    )

    assert sorted(result["category"].to_list()) == ["a", "b"]
    assert sorted(result["value"].to_list()) == [6.0, 9.0]
    assert sorted(result["count_col"].to_list()) == [2, 3]
