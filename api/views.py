import re, statistics, datetime

from itertools                  import groupby
from rest_framework.permissions import AllowAny
from rest_framework.views       import APIView
from rest_framework.response    import Response

from core.api_settings import GubnCode
from core.sewer_pipe   import SewerPipeOpenAPI
from core.rainfall     import RainfallOpenAPI
from api.serializers   import SeoulOpenDataSerializer

from drf_yasg          import openapi
from drf_yasg.utils    import swagger_auto_schema


class SeoulOpenDataVeiw(APIView):
    permission_classes = [AllowAny]
    
    query_param = openapi.Parameter('gubn', openapi.IN_QUERY, required=True, pattern='?gubn=', type=openapi.TYPE_STRING)
    @swagger_auto_schema(responses={200: SeoulOpenDataSerializer}, manual_parameters=[query_param])
    def get(self, request):
        """
        writer: 김동규
        query param: gubn
        return: json
        detail: 구(지역) 이름을 입력받으면 서울시 하수관, 강우량 데이터를 수집/가공하여 결합된 데이터를 반환합니다.
        """
        try:
            gubn = request.GET.get('gubn', None)
            if not gubn:
                return Response({'detail': '구이름을 입력하세요.'}, status=400)
            
            code, err = GubnCode.get_gubn_code_n_check_err(gubn)
            if err:
                return Response({'detail': err}, status=400)
            
            sewer_pipe_data, err = SewerPipeOpenAPI.get_sewer_pipe_data(code)
            if err:
                return Response({'detail': err}, status=400)
            
            gu_name            = sewer_pipe_data[0]['GUBN_NAM']
            rainfall_data, err = RainfallOpenAPI.get_rainfall_data(gu_name)
            if err:
                return Response({'detail': err}, status=400)
            
            """
            최근 1시간을 기준으로 서울시 해당 구(지역)의 하수관로 수위 데이터의 평균값을 구합니다.
            """
            latest_one_hour_sewer_level = round(
                statistics.mean([i['MEA_WAL'] for i in sewer_pipe_data]),
                2
            )
            
            """
            최근 1시간을 기준으로 서울시 해당 구(지역)의 강우량 데이터를 RAINGAUGE_NAME 단위로 가공하고,
            RAINGAUGE별로 강우량의 총 합계를 구합니다.
            """
            rainfall_groupby_raingauge = groupby(
                sorted(rainfall_data, key=lambda x: x['RAINGAUGE_CODE']),
                lambda x: x['RAINGAUGE_NAME']
            )
            
            rainfall_by_raingauge_dict = {
                i: round(sum(map(
                            lambda x: float(x['RAINFALL10'])
                            if re.sub('[-:\s]', '', x['RECEIVE_TIME'])[:10]\
                            == (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y%m%d%H')\
                            else 0,
                            j)
                        ),
                    2)
                for i, j in rainfall_groupby_raingauge
            }

            rainfall_by_raingauge = []

            for i, j in rainfall_by_raingauge_dict.items():
                rainfall_by_raingauge.append({'raingauge_name': i, 'sum_rain_fall': j})
            
            data = {
                'gu_name'         : gu_name,
                'avg_water_level' : latest_one_hour_sewer_level,
                'raingauge_info'  : rainfall_by_raingauge
            }
            
            """
            Serializer를 활용하여 데이터의 Validation 여부를 체크합니다.
            """
            serializer = SeoulOpenDataSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        
        except KeyError:
            return Response({'detail': 'key error'}, status=400)   