import pandas as pd

data = [["665587", 2], ["669532", 1], ["669537", 2], ["669532", 1], ["665587", 1]]


def smart_counter(data):
    df = pd.DataFrame(data, columns=["id", "version"])
    df0 = df.groupby(by=["id", "version"])
    result = df0.agg({"id": ["count"], "version": ["count"]})

    return result


df = smart_counter(data)
print(df)
# df.to_csv('exmpl.csv')
