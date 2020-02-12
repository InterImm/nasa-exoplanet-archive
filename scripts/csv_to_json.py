import pandas as pd
import json

cwd = "."


df_exo = pd.read_csv(
    os.path.join(
        cwd, "dataset", "confirmed_exoplanets.csv"
    ),
    comment='#'
)

exo_dict = df_exo.to_dict(orient="record")

with open(
    os.path.join(
        cwd, "dataset", "confirmed_exoplanets.json"
    ),
    "w+"
) as fp:
    json.dump(exo_dict, fp)