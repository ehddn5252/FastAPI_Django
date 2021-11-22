import copy

import pymysql
from typing import Dict

from apply_rds.Package.Connector.Info import Info
from apply_rds.Package.Logger import Logger


class Connector:

    def __init__(self , db_name: str=None):
        Logger.logger.info("DB 연결 클래스 초기화 함수 실행")
        self.connectDB()
        if self.connection is not None and db_name is not None:
            self.connection.select_db(db=db_name)

    def connectDB(self , DBInstace_Info: Dict = None):
        """
        @desc DB 객체에 연결하고, 클래스 매개변수에 접속 정보를 저장한다
        @param DBInstace_Info DB 접속 정보를 Dict로 전달한다
        @reutnr None
        """
        ret: bool = False

        if DBInstace_Info is not None:
            # connection_info: Dict = copy.deepcopy(Info.DB.DBInstance2_CONNECTION_INFO)
            Info.DB.DBInstance2_CONNECTION_INFO.update(DBInstace_Info)

        try:
            self.connection: pymysql.connections.Connection = pymysql.connect(host=Info.DB.DBInstance2_CONNECTION_INFO["HOST"] , user=Info.DB.DBInstance2_CONNECTION_INFO["USER"] ,
                                                                              password=Info.DB.DBInstance2_CONNECTION_INFO["PASSWORD"] ,
                                                                              port=Info.DB.DBInstance2_CONNECTION_INFO["PORT"] , charset=Info.DB.DBInstance2_CONNECTION_INFO["CHARSET"] ,
                                                                              autocommit=Info.DB.DBInstance2_CONNECTION_INFO["AUTOCOMMIT"] , database=Info.DB.DBInstance2_CONNECTION_INFO["DATABASE"] ,
                                                                              read_timeout=30 , connect_timeout=30 ,
                                                                              cursorclass=pymysql.cursors.DictCursor)
            Logger.logger.info(f"접속완료 {Info.DB.DBInstance2_CONNECTION_INFO}")
            ret = True

        except pymysql.err.OperationalError as ex:
            Logger.logger.error(f"연결접속 오류, {ex}")

        return ret

    def connectModifyDB(self , DBInfo: Dict , *args , **kwargs):
        """
        @desc DB 연결을 변경하거나 다른곳으로 접속하기 위해서 시도한다
        @param DBInfo: 변경할 DB 연결 객체
       @return None
        """

        if self.connection is not None:
            self.closeDB()
        self.connectDB(DBInstace_Info=DBInfo)

    def closeDB(self) -> None:
        """
        @desc DB 연결 객체를 종료한다
        @return: None
        """
        try:
            self.connection.close()

        except pymysql.err.Error as ex:
            Logger.logger.error(f"{self.__class__} :: {ex}")

    def getCursor(self) -> pymysql.cursors.DictCursor:
        """
        @desc DB 쿼리 커서 객체를 얻는다
        @return: DB 쿼리 커서 객체
        """
        # TODO cursor class 지정해줘야할 수 있음 ( 학제님 말에 의하면 DictCursor가 아니라 일반화 되어 있는 리스트 형태로 뿌려주거나 하는 형태로 할 수 있음)
        return self.connection.cursor() #cursor=pymysql.cursors.SSDictCursor)

    def closeCursor(self , cur: pymysql.cursors.DictCursor) -> None:
        """
        @desc DB 쿼리 커서 객체를 닫는다
        @param cur: DB 쿼리 커서 객체
        @return: None
        """
        Logger.logger.info(f"{cur} 커서 객체 종료")
        cur.close()

    def __del__(self):
        Logger.logger.info("소멸자호출 - DB 연결 객체 해제")
        self.closeDB()
