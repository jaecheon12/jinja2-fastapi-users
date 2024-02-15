from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.mssql import BIGINT

Base = declarative_base()

class ModelTM(Base):
    __tablename__ = 'Model_TM'
    
    Code = Column(String, primary_key=True, nullable=False)
    Hash = Column(String, nullable=False)
    Folder = Column(String, nullable=True)  # Custom function 'LPAD' handling needed
    Name = Column(String, nullable=False)
    Name_ori = Column(String, nullable=False)
    Name_eng = Column(String, nullable=False)
    Birth = Column(String, nullable=False)
    Age = Column(Integer, nullable=True)  # Custom function 'GetAge' handling needed
    Sex = Column(BIGINT, nullable=False)
    Blood = Column(BIGINT, nullable=False)
    Height = Column(Integer, nullable=False)
    Weight = Column(Integer, nullable=False)
    Bust = Column(Integer, nullable=False)
    Waist = Column(Integer, nullable=False)
    Hip = Column(Integer, nullable=False)
    Job = Column(BIGINT, nullable=False)
    ExJob = Column(BIGINT, nullable=False)
    Feature = Column(BIGINT, nullable=False)
    Talent = Column(BIGINT, nullable=False)
    PartBody = Column(BIGINT, nullable=False)
    CorpCode = Column(String, nullable=False)
    CUserId = Column(String, nullable=False)
    Tel = Column(String, nullable=False)
    Homepage = Column(String, nullable=False)
    CDate = Column(DateTime, nullable=False)
    UDate = Column(DateTime, nullable=False)
    Hit = Column(Integer, nullable=False)
    Flag = Column(Integer, nullable=False)
    State = Column(Integer, nullable=False)
    Career = Column(String, nullable=False)
    Old_Genter = Column(Integer, nullable=True)
    Old_Idx = Column(Integer, nullable=True)
    Idx = Column(Integer, autoincrement=True, nullable=False)
    Flag2 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "Name": self.Name,
            "Name_ori": self.Name_ori,
            "Name_eng": self.Name_eng,
            "Birth": self.Birth,
            "Age": self.Age,
            "Sex": self.Sex,
            "Flag": self.Flag,
            "State": self.State,
            "Career": self.Career,
        }