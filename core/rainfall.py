import json, requests

from typing            import Tuple, Any
from core.api_settings import URL, KEY, TYPE

 
class RainfallOpenAPI:
    """
    Assignee: 김동규
    
    param: GU_NAME[구(지역)이름]
    return: json
    detail: 구(지역) 이름을 입력받으면 서울시 강우량 데이터를 반환합니다.
    """
    
    SERVICE     = 'ListRainfallService'
    START_INDEX = 1
    END_INDEX   = 100
    
    def get_rainfall_data(GU_NAME: str) -> Tuple[Any, str]:
        try:
            url = URL + '/{}/{}/{}/{}/{}/{}'.format(
                KEY,
                TYPE,
                RainfallOpenAPI.SERVICE,
                RainfallOpenAPI.START_INDEX,
                RainfallOpenAPI.END_INDEX,
                GU_NAME
            )
            
            res  = requests.get(url)
            data = json.loads(res.content)
            return data['ListRainfallService']['row'], None
        except KeyError:
            return None, '서울시 해당지역의 공공데이터를 찾지 못했습니다.'