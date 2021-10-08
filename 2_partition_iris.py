import pandas as pd


iris = pd.read_parquet('iris.parquet')
iris.to_parquet('iris_partitioned.parquet', partition_cols=['species'])
