from typing import Tuple , Dict , List , Union

import pymysql.cursors

from apply_rds.Package.Connector import Connector
from apply_rds.Package.Logger import Logger
from apply_rds.Package.Parser import Parameter


class DML:
    def __init__(self , db_name: str = None):
        self.db_instace = Connector(db_name=db_name)

        if not self.db_instace:
            Logger.logger.error("DB Connected Faile")
        else:
            Logger.logger.info("DML 클래스 초기화 함수 실행")

    def setServer(self , DBInfo: Dict):
        """
        @desc DBInfo에 접속을 시도합니다
        @param DBInfo: DB에 접속하기 위한 클래스 정보
        """
        ret: bool = False
        self.db_instace.connectModifyDB(DBInfo=DBInfo)

        ret = True
        return ret

    def select_one(self , *args , **kwargs) -> Tuple[bool , Dict]:
        """
        @desc 가변매개변수를 활용하여, 인자로 들어온 table_name과 where문을 활용하여 DB 스키마에 존재하는 데이터 검색 (단일행 검색)
                kwargs 매개변수에는 반드시 query 값을 넣어줘야한다
        @param args: Tuple 형태의 가변인자
        @param kwargs: Dict 형태의 가변인자
        @return: select한 쿼리의 결과값과 rowcount를 리턴한다
        """
        Logger.logger.info("DML::select_one function called")

        is_select: bool = False
        ret: Union[List[Dict] , Dict] = []
        query: str = kwargs["query"]

        cur = self.db_instace.getCursor()
        try:
            Logger.logger.info(f"select_one query {query}")

            result = cur.execute(query=query)
            if result and cur.rowcount > 0:
                is_select: bool = True
                ret: Dict = cur.fetchone()

        except Exception as ex:
            Logger.logger.error(ex)

        finally:
            cur.close()
        return (is_select , ret)

    def select_all(self , *args , **kwargs) -> Tuple[bool , List[Dict]]:
        """
        @desc 가변매개변수를 활용하여, 인자로 들어온 table_name과 where문을 활용하여 DB 스키마에 존재하는 데이터 검색
                kwargs 매개변수에는 반드시 query 값을 넣어줘야한다
        @param args: Tuple 형태의 가변인자
        @param kwargs: Dict 형태의 가변인자
        @return: select한 쿼리의 결과값과 rowcount를 리턴한다
        """
        Logger.logger.info("DML::select_all function called")
        is_select: bool = False
        ret: List[Dict] = []

        query: str = kwargs["query"]
        Logger.logger.info(f"select_all query {query}")

        cur = self.db_instace.getCursor()
        try:
            result = cur.execute(query=query)  # TODO 예외처리
            if result and cur.rowcount > 0:
                is_select: bool = True
                ret: List[Dict] = cur.fetchall()

        except Exception as ex:
            Logger.logger.error(ex)

        finally:
            cur.close()

        return (is_select , ret)

    def insert(self, *args, **kwargs) -> bool:
        """
        @desc: DB에 데이터를 입력하는 기능
                kwargs 매개변수에는 반드시 table, columns, values 값을 넣어줘야한다
        @param args: Tuple 형태의 가변인자
        @param kwargs: Dict 형태의 가변인자
        @return: True(Insert 성공), False(Insert 실패)
        """
        Logger.logger.info("DML::insert function called")
        is_insert: bool = False
        table_name: str = kwargs["table"] if kwargs.get("table") is not None else ""
        query_data: Dict = kwargs["query_data"] if kwargs.get("query_data") is not None else {}
        if table_name == "" or len(query_data) == 0:
            Logger.logger.error(f"DML::insert table_name:{table_name}, columns:{query_data}를 입력할 수 없습니다")
            return is_insert

        (cols, vals) = Parameter.extractKV(data=query_data)
        query = f"""INSERT INTO {table_name} ({cols}) VALUES ({vals})"""
        Logger.logger.info(f"insert - {query}")
        cur: pymysql.cursors.DictCursor = self.db_instace.getCursor()
        try:
            result: int = cur.execute(query=query)

            if result:
                is_insert: bool = True
                Logger.logger.info(f"({result}) - {query} 데이터 입력 완료!")

        except Exception as ex:
            Logger.logger.error(f"{ex}\n\t{query} 에러 발생!")

        finally:
            cur.close()

        return is_insert

    def update(self , *args , **kwargs) -> int:
        """
        @desc queyr에 대한 업데이트 기능 함수
        @param args: Tuple 형태의 가변인자
        @param kwargs: Dict 형태의 가변인자
        @return: True(update 성공), False(update 실패)
        """
        # def setParameter(columns)
        Logger.logger.info("DML::update function called")
        is_update: bool = False
        table_name: str = kwargs["table"] if kwargs.get("table") is not None else ""
        query_data: Dict = kwargs["query_data"] if kwargs.get("query_data") is not None else {}
        condition: str = kwargs["condition"] if kwargs.get("condition") is not None else ""

        if table_name == "" or len(query_data) == 0:
            Logger.logger.error(f"DML::update table_name:{table_name}, query_data:{query_data}를 변경할 수 없습니다")
            return is_update

        cur: pymysql.cursors.DictCursor = self.db_instace.getCursor()
        vals: str = Parameter.mergeKV(data=query_data)

        query = f"UPDATE {table_name} SET {vals}"
        try:
            if condition != "": query += f" WHERE {condition}"
            Logger.logger.info(f"update - {query}")
            result = cur.execute(query=query)

            if result > 0:
                is_update: bool = True
                Logger.logger.info(f"업데이트 완료")
            else:
                Logger.logger.warn(f"업데이트 된 데이터가 없습니다")

        except Exception as ex:
            Logger.logger.error(f"{ex}\n\t{query} 에러 발생!")

        finally:
            cur.close()

        return is_update
