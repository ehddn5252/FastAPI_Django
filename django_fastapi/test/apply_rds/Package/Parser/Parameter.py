import copy
import json
from typing import Dict , Tuple , List


class Parameter:

    @classmethod
    def convertValue(cls , data: Dict):
        """
        @desc data에 있는 value 값이 string이라면 '' 쿼터를 넣어주는 역할을 수행한다
        @param data: 쿼리 입력값에 사용할 Dict 데이터
        @return: Dict
        """
        c: Dict = copy.deepcopy(x=data)

        for k, v in c.items():
            if isinstance(v, str): # str 객체이면 ''로 싱글쿼터를 감싸준다
                v: str = v.replace("\'", "\\'")
                data[k] = f"""'{v}'"""

            """
            elif isinstance(v, dict):
                prev_dict = json.dumps(v).replace("\'", "")
                prev_dict = f"""'{prev_dict}'"""
                data[k] = prev_dict
                print('DDD ', data[k])
            """

    @classmethod
    def extractKV(cls , data: Dict) -> Tuple[str , str]:
        """
        @desc data로 들어온 dict 데이터를 key와 values를 별도로 추출해서 뽑아내준다
        @param data: 쿼리 입력값에 사용할 Dict 데이터
        @return: Tuple[List[str],List[str]]
        """
        cls.convertValue(data=data)

        cols: str = ",".join(list(map(str , list(data.keys()))))
        vals: str = ",".join(list(map(str , list(data.values()))))

        return (cols , vals)

    @classmethod
    def mergeKV(cls , data: Dict) -> str:
        """
        @desc data로 들어온 dict 데이터를 key와 value를 매칭해서 update 쿼리에 활용할 수 있게 처리한다
        @param data: 쿼리 입력값에 사용할 Dict 데이터
        @return: 합쳐진 dict 데이터
        """
        ret: str = f""
        dict_length: int = len(data.items()) - 1

        for i , (key , value) in enumerate(data.items()):
            if dict_length == i:
                ret += f"{key}='{value}'"
            else:
                ret += f"{key}='{value}' AND "
            print(i , key , value)

        ret = ret.strip() if len(ret) != 0 else ret
        print("mergeKV " , data , ret)
        return ret
