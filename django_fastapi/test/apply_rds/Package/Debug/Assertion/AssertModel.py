from apply_rds.Package import Logger


class AssertModel:
    # debug = True # debug가 True일 경우에만 assert 기능을 활성화 한다
    debug = False  # debug가 True일 경우에만 assert 기능을 활성화 한다
    isPrintable = False

    @classmethod
    def chkDbgMode(cls):
        """
        @desc 디버깅모드인지 아닌지를 확인한다
        :return: True, False
        """
        return AssertModel.debug

    @classmethod
    def EqualAssert(cls, assert_obj: object, assert_cond: object, exp_cond="=="):
        """
        @desc 프로그램 실행 중 디버깅 모드에서만 assert 기능을 수행하고, release 모드시에는 assert 기능을 비활성화 시킨다
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert 조건을 지정해준다
        @param exp_cond: 확인을 위한 조건식
        :return: assert True, False
        """
        # if not AssertModel.chkDbgMode(): return

        assert assert_obj == assert_cond
        if AssertModel.isPrintable:
            Logger.logger.info("{assert_obj} == {assert_cond} assert 검사 완료")

    @classmethod
    def NonEqualAssert(cls , assert_obj: object, assert_cond: object, exp_cond="!=") -> None:
        """
        @desc 프로그램 실행 중 디버깅 모드에서만 assert 기능을 수행하고, release 모드시에는 assert 기능을 비활성화 시킨다
                조건식의 비교연산은 != 로 통일
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert 조건을 지정해준다
        @param exp_cond: 확인을 위한 조건식
        :return: assert True, False
        """
        # if not AssertModel.chkDbgMode(): return

        assert assert_obj != assert_cond
        if AssertModel.isPrintable:
            Logger.logger.info(f"{assert_obj} == {assert_cond} assert 검사 완료")

    @classmethod
    def lte(cls , assert_obj: int , assert_cond: int):
        """
        @desc
                프로그램 실행 중 디버깅 모드에서만 assert 기능을 수행하고, release 모드시에는 assert 기능을 비활성화 시킨다
                조건식은 > 로 왼쪽 피연산잔의 값이 더 클경우 지정
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert_obj에 비교할 integer 값
        :return: assert True, False
        """
        # if not AssertModel.chkDbgMode(): return

        assert assert_obj > assert_cond
        if AssertModel.isPrintable:
            Logger.logger.info(f"{assert_obj} > {assert_cond} assert 검사 완료")

    @classmethod
    def gte(cls, assert_obj: int, assert_cond: int) -> None:
        """
        @desc
                프로그램 실행 중 디버깅 모드에서만 assert 기능을 수행하고, release 모드시에는 assert 기능을 비활성화 시킨다
                조건식은 < 로 왼쪽 피연산잔의 값이 더 클경우 지정
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert_obj에 비교할 integer 값
        :return: assert True, False
        """
        # if not AssertModel.chkDbgMode(): return
        assert assert_obj < assert_cond
        if AssertModel.isPrintable:
            Logger.logger.info(f"{assert_obj} < {assert_cond} assert 검사 완료")

    @classmethod
    def IsInstanceEqual(cls, assert_obj: object, assert_cond: object) -> bool:
        """
        @desc 프로그램 실행 중 디버깅 모드에서만 assert 기능을 수행하고, release 모드시에는 assert 기능을 비활성화 시킨다
                조건식의 비교연산은 isinstance로 통일
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert 조건을 지정해준다
        @param exp_cond: 확인을 위한 조건식
        :return: assert True, False
        """
        # if not AssertModel.chkDbgMode(): return ret
        ret: bool = True
        assert isinstance(assert_obj , assert_cond)
        if AssertModel.isPrintable:
            Logger.logger.info(f"isinstance({assert_obj},{assert_cond}) assert 검사 완료")
        return ret

    @classmethod
    def NotIsInstanceEqual(cls, assert_obj: object, assert_cond: object) -> bool:
        """
        @desc 프로그램 실행 중 디버깅 모드에서만 assert 기능을 수행하고, release 모드시에는 assert 기능을 비활성화 시킨다
                조건식의 비교연산은 isinstance로 통일
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert 조건을 지정해준다
        @param exp_cond: 확인을 위한 조건식
        :return: assert True, False
        """
        ret: bool = False
        # if not AssertModel.chkDbgMode(): return ret
        isCondition = isinstance(assert_obj , assert_cond)
        assert not isCondition  # assert_object가 assert_condtion과 동일하지 않다면 pass
        if AssertModel.isPrintable:
            Logger.logger.info(f"isinstance({assert_obj},{assert_cond}) assert 검사 완료")
        ret = True
        return ret

    @classmethod
    def IsInObject(cls, assert_obj: object, assert_cond: object) -> bool:
        """
        @desc assert_obj에 assert_cond가 is in 인지 체크하는 기능
        @param assert_obj: assert를 확인할 object 객체
        @param assert_cond: assert 조건을 지정해준다
        @param exp_cond: 확인을 위한 조건식
        :return: assert True, False
        """
        ret: bool = False
        # if not AssertModel.chkDbgMode(): return ret

        if not isinstance(assert_cond , list):
            assert assert_cond in assert_obj
        elif isinstance(assert_cond , list):
            for cond in assert_cond:
                assert cond in assert_obj
                break

        if AssertModel.isPrintable:
            Logger.logger.info(f"IsInObject({assert_obj},{assert_cond}) assert 검사 완료")
        return ret
