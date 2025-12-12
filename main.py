"""TODO

2. csvファイルのインポート
3. 任意の条件でデータを抽出し、別表にてデータ操作を行う。
"""

import csv

from model import Population, Prefecture
from settings import SessionLocal


def main():
    file = "data/population_by_gender.csv"
    encode = "shift-jis"

    # DBに接続する
    with SessionLocal() as session:
        # データを読み込んでインポートする
        with open(file, mode="r", newline="", encoding=encode) as csvfile:

            # csvファイルの読み込み
            reader = csv.DictReader(csvfile)

            # データをインポートする
            populations: list[Population] = []
            for index, row in enumerate(reader):
                # 都道府県コードがマスタに存在するかチェックする
                prefecture = (
                    session.query(Prefecture)
                    .filter_by(code=row["都道府県コード"])
                    .first()
                )
                if not prefecture:
                    print("都道府県コードが存在しません。スキップします。")
                    continue

                # データobjectをリストに格納する。
                try:
                    population: Population = Population(
                        id="".join([row["都道府県コード"], row["西暦（年）"]]),
                        prefecture_code=row["都道府県コード"],
                        era=row["元号"],
                        era_year=row["和暦（年）"],
                        western_year=int(row["西暦（年）"]),
                        note=row["注"] if row["注"] else None,
                        total=(
                            int(row["人口（総数）"])
                            if row["人口（総数）"]
                            else None
                        ),
                        male=(
                            int(row["人口（男）"])
                            if row["人口（男）"]
                            else None
                        ),
                        female=(
                            int(row["人口（女）"])
                            if row["人口（女）"]
                            else None
                        ),
                    )
                except ValueError:
                    # TODO: 例外処理を決めておく。一先ずは該当データはスキップする。
                    print(index, row)
                    continue
                populations.append(population)

            # Bulk-INSERTおよびコミット
            session.add_all(populations)
            session.commit()
            print("人口データをインポートしました。")


if __name__ == "__main__":
    main()
