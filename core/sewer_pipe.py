import json, requests, datetime

from typing            import Tuple, Any
from core.api_settings import URL, KEY, TYPE


class SewerPipeOpenAPI:
    """
    writer: 김동규
    param: CODE(구분코드)
    return: json
    detail: 구분(지역)코드를 입력받으면 서울시 하수관로의 수위 데이터를 반환합니다.
    """
    
    SERVICE     = 'DrainpipeMonitoringInfo'
    START_INDEX = 1
    END_INDEX   = 1000
    
    def get_sewer_pipe_data(CODE: str) -> Tuple[Any, str]:
        try:
            NOW             = datetime.datetime.now()
            BEFORE_ONE_HOUR = (NOW - datetime.timedelta(hours=1)).strftime('%Y%m%d%H')
            
            url = URL + '/{}/{}/{}/{}/{}/{}/{}/{}'.format(
                KEY,
                TYPE,
                SewerPipeOpenAPI.SERVICE,
                SewerPipeOpenAPI.START_INDEX,
                SewerPipeOpenAPI.END_INDEX,
                CODE,
                BEFORE_ONE_HOUR,
                BEFORE_ONE_HOUR
            )
            
            res  = requests.get(url)
            data = json.loads(res.content)
            return data['DrainpipeMonitoringInfo']['row'], None
        except KeyError:
            return None, '서울시 해당지역의 공공데이터를 찾지 못했습니다.'