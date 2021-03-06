from typing        import Tuple, Any
from labq.settings import OPEN_API_KEY


KEY  = OPEN_API_KEY
URL  = 'http://openAPI.seoul.go.kr:8088'
TYPE = 'json'


class GubnCode:
    """
    Assignee: 김동규
    
    param: gubn[구(지역)이름]
    return: 구분코드(code)
    detail: 구(지역) 이름을 입력받으면 구분코드(code)를 반환합니다. 
    """
    
    def get_gubn_code_n_check_err(gubn: str) -> Tuple[Any, str]:
        gubn_set = {
            '종로': '01',
            '중': '02',
            '용산': '03',
            '성동': '04',
            '광진': '05',
            '동대문': '06',
            '중랑': '07',
            '성북': '08',
            '강북': '09',
            '도봉': '10',
            '노원': '11',
            '은평': '12',
            '서대문': '13',
            '마포': '14',
            '양천': '15',
            '강서': '16',
            '구로': '17',
            '금천': '18',
            '영등포': '19',
            '동작': '20',
            '관악': '21',
            '서초': '22',
            '강남': '23',
            '송파': '24',
            '강동': '25',
        }
        code = gubn_set.get(gubn, None)
        if not code:
            return None, f'{gubn}구 지역은 존재하지 않습니다.'
        return code, None