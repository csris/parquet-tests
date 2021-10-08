import dask.dataframe as dd

iris = dd.read_parquet('iris_partitioned.parquet').compute()

print(iris)
