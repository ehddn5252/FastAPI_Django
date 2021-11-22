

class ValidateRDS(Exception):
    """ AWS-Package_RDS 관련 예외클래스 """
    def __init__(self, message=None, errors=None):
        """
        :param message:
        :param errors:
        """
        # 필요한 매개변수로 기본 클래스 생성자 호출
        super().__init__(message)

        # 새로운 사용자 정의 코드
        self.errors = errors