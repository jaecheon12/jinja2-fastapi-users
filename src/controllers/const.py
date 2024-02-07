from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.Const_TM import Const_TM, Const_TM_insert
from src.models.Const import NochulMeche, GenreTopic
from datetime import datetime
from sqlalchemy.orm import Session
from src.models.Const_TM import Const_TM, Const_TM_insert
from icecream import ic
import logging

class CConst:
    def __init__(self, db: Session):
        self.db = db

    def selectLastCValue(self, gName: str) -> int:
        try:
            result = self.db.query(Const_TM.CValue).filter(Const_TM.GName == gName).order_by((Const_TM.CValue).desc()).first()
            return result[0]
        except SQLAlchemyError as e:
            ic(f"ERR CConst selectLastCValue: {str(e)}")
            logging.error(f"ERR selectLastCValue: {e}")
            return 1
        
        
    def selectLastSunse(self, gName: str) -> int:
        try:
            result = self.db.query(Const_TM.CValue).filter(Const_TM.GName == gName).order_by((Const_TM.Sunse).desc()).first()
            return result[0]
        except SQLAlchemyError as e:
            ic(f"ERR CConst selectLastSunse: {str(e)}")
            logging.error(f"ERR selectLastSunse: {e}")
            return 1
        

    def insertItem(self, name: str, engName: str, group: str, target: str) -> bool:
        try:
            resIndex = self.selectLastCValue(group)
            resOrder = self.selectLastSunse(group)

            constItem = Const_TM_insert(GName = group, 
                                        CName = name,
                                        CNameASP = engName,
                                        CValue = resIndex + 1,
                                        Sunse = resOrder + 1,
                                        Target = target)
            self.db.add(constItem)
            return True
        except SQLAlchemyError as e:
            ic(f"ERR CConst insertItem: {str(e)}")
            logging.error(f"ERR insertItem: {e}")
            return False
        
    
    def selectCountryChannel(self, channelCountry: str) -> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter( Const_TM.State == 1,
                                                Const_TM.GName == "Country",
                                                Const_TM.CNameASP == channelCountry
                                                ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CConst selectCountryChannel: {str(e)}")
            logging.error(f"ERR selectCountryChannel: {e}")
            return None
        

    def selectCountry(self, country: str) -> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == "Country",
                                                    Const_TM.CValue == country
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CConst selectCountry: {str(e)}")
            logging.error(f"ERR selectCountry: {e}")
            return None
        

    def selectLanguage(self, language: str) -> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == "MediaLang",
                                                    Const_TM.CValue == language
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CConst selectLanguage: {str(e)}")
            logging.error(f"ERR selectLanguage: {e}")
            return None
        

    def selectAllMeche(self, meche: int, mediaType: int) -> list[dict]:
        try:
            ic(meche)
            result = self.db.query(Const_TM).filter(Const_TM.GName == ("VideoMeche" if mediaType == 1 else "ImageMeche"),
                                                    Const_TM.CValue.op('&')(meche) > 0
                                                    ).all()
            if not result:
                return []
            
            mecheList = []
            for item in result:
                ic(item.to_dict())
                mecheList.append(NochulMeche(   item.CValue,
                                                item.CName,
                                                item.UpJong,
                                                item.Flag).to_dict())
            return mecheList

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectAllMeche: {str(e)}")
            logging.error(f"ERR selectAllMeche: {e}")
            return []
        

    def selectAllNochul(self, nochul: int, mediaType: int) -> list[dict]:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == ("VideoNochul" if mediaType == 1 else "ImageNochul"),
                                                    Const_TM.CValue.op('&')(nochul) > 0
                                                    ).all()
            if not result:
                return []
            
            nochulList = []
            for item in result:
                ic(item.to_dict())
                nochulList.append(NochulMeche(  item.CValue,
                                                item.CName,
                                                item.UpJong,
                                                0).to_dict())
            return nochulList

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectAllNochul: {str(e)}")
            logging.error(f"ERR selectAllNochul: {e}")
            return []
        
        
    def selectAllGenre(self, genre: int) -> list[dict]:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == "Genre",
                                                    Const_TM.CValue.op('&')(genre) > 0
                                                    ).all()
            if not result:
                return []
            
            genreList = []
            for genre in result:
                genreList.append(GenreTopic(genre.CValue,
                                            genre.CName,
                                            genre.GName).to_dict())
            return genreList

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectAllGenre: {str(e)}")
            logging.error(f"ERR selectAllGenre: {e}")
            return []
        

    def selectAllTopic(self, topic: int) -> list[dict]:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == "Topic",
                                                    Const_TM.CValue.op('&')(topic) > 0
                                                    ).all()
            if not result:
                return []
            
            genreTopic = []
            for genre in result:
                genreTopic.append(GenreTopic(   genre.CValue,
                                                genre.CName,
                                                genre.GName).to_dict())
            return genreTopic
        
        except SQLAlchemyError as e:
            ic(f"ERR CConst selectAllTopic: {str(e)}")
            logging.error(f"ERR selectAllTopic: {e}")
            return []
        

    def selectJobType(self, GeekJong: str)-> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter( Const_TM.State == 1, 
                                                Const_TM.GName == "GeekJong", 
                                                Const_TM.CValue == GeekJong
                                                ).first()
            return result

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectJobType: {str(e)}")
            logging.error(f"ERR selectJobType: {e}")
            return None
        

    def selectConstList(self) -> list[Const_TM]|None:
        constList = ["Country", "MediaLang", "VideoMeche", "ImageMeche", "VideoNochul", "ImageNochul", "Genre", "Topic", "PumOne", "PumTwo", "PumThree"]
        try:
            result = []
            for const in constList:
                result += self.db.query(Const_TM).filter(   Const_TM.State == 1, 
                                                            Const_TM.GName == const
                                                            ).all()
            return result

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectConstList: {str(e)}")
            logging.error(f"ERR selectConstList: {e}")
            return None
        

    def selectPommok_1(self, Pummok1: str)-> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == "PumOne", 
                                                    Const_TM.CValue == Pummok1
                                                    ).first()
            return result

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectPommok_1: {str(e)}")
            logging.error(f"ERR selectPommok_1: {e}")
            return None
        

    def selectPommok_2(self, Pummok2: str)-> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter(Const_TM.GName == "PumTwo", 
                                                    Const_TM.CValue == Pummok2
                                                    ).first()
            return result

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectPommok_2: {str(e)}")
            logging.error(f"ERR selectPommok_2: {e}")
            return None
        

    def selectPommok_3(self, Pummok3: str)-> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter( Const_TM.GName == "PumThree", 
                                                Const_TM.CValue == Pummok3
                                                ).first()
            return result

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectPommok_3: {str(e)}")
            logging.error(f"ERR selectPommok_3: {e}")
            return None
    
    def selectMakerPart(self, makerPartID: int)-> Const_TM|None:
        try:
            result = self.db.query(Const_TM).filter( Const_TM.State == 1, 
                                                Const_TM.GName == "MakerPart", 
                                                Const_TM.CValue == makerPartID
                                                ).first()
            return result

        except SQLAlchemyError as e:
            ic(f"ERR CConst selectMakerPart: {str(e)}")
            logging.error(f"ERR selectMakerPart: {e}")
            return None
        