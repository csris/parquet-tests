import dask.dataframe as dd

iris = dd.read_parquet(
    'iris_partitioned.parquet', 
    filters=[('species', '==', 'setosa')]
).compute()

print(iris)
