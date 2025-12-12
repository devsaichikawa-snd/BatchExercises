from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Prefecture(Base):
    """都道府県マスタ

    Columns:
        code: 都道府県コード (01-47)
        name: 都道府県名称 (例: 東京都)
    """

    __tablename__ = "m_prefecture"

    code: Mapped[str] = mapped_column(String(2), primary_key=True)
    name: Mapped[str] = mapped_column(String(10), nullable=False)


class Population(Base):
    """人口テーブル

    Columns:
        id: 主キー (都道府県コード + 西暦 例: 112012)
        prefecture_code: 都道府県コード (01-47)
        era: 元号 (令和, 平成,,,)
        era_year: 和暦年
        western_year: 西暦年
        note: 注
        total: 人口総数
        male: 人口(男)
        female: 人口(女)
    """

    __tablename__ = "t_populations"

    id: Mapped[str] = mapped_column(String(6), primary_key=True)
    prefecture_code: Mapped[str] = mapped_column(
        String(2), ForeignKey("m_prefecture.code")
    )
    era: Mapped[int] = mapped_column(Integer)
    era_year: Mapped[int] = mapped_column(Integer)
    western_year: Mapped[int] = mapped_column(Integer)
    note: Mapped[int] = mapped_column(Integer, nullable=True)
    total: Mapped[int] = mapped_column(Integer)
    male: Mapped[int] = mapped_column(Integer)
    female: Mapped[int] = mapped_column(Integer)
