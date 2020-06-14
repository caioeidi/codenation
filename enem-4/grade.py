import pandas as pd
from json import dumps


eq = lambda x,y: x == y

def score():
    answer = pd.read_csv("answer.csv")
    truth = pd.read_csv("truth.csv")
    return (
        truth
        .set_index("NU_INSCRICAO")
        .join(answer.drop_duplicates(subset=["NU_INSCRICAO"]).set_index("NU_INSCRICAO"), how="left", rsuffix="_")        
        [["IN_TREINEIRO", "IN_TREINEIRO_"]]
        .fillna("?")
        .pipe(lambda df: df["IN_TREINEIRO"] == df["IN_TREINEIRO_"])
        .pipe(lambda df: dumps({"score": 100*df.mean()}))
    )

if __name__ == "__main__":
    print(score())
