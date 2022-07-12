import json

from unittest      import mock
from unittest.mock import patch

from rest_framework.test import APITestCase


class SeoulOpenDataTest(APITestCase):
    """
    Assignee: 김동규
    
    Test Case Description
    
    1. 케이스 설정 방법
        1) success test case
            - 성공 응답코드 확인
            - 구(지역) 이름 일치여부 확인
            - 평균 하수관로 수위 타입 확인
            - 총 강우량 타입 확인
            - API 반환 데이터에 구(지역) 이름 포함유무 확인
            - API 반환 데이터에 평균 하수관로 수위 데이터 포함유무 확인
            - API 반환 데이터에 강우량 정보 포함유무 확인
            - API 반환 데이터에 강우량 측정기 이름 포함유무 확인
            - API 반환 데이터에 총 강우량 데이터 포함유무 확인
        2) fail test case 
            - 에러 응답코드 확인
            - API 요청 시 QueryString 존재유무 확인
            - 특정 구(지역) 이름이 서울시에 존재하는지 확인
            - 서울시 하수관로 Open API가 에러를 반환할 경우 예외처리 확인(mock 활용)
            - 서울시 강우량 Open API가 에러를 반환할 경우 예외처리 확인(mock 활용)
    2. 케이스 종류
        1) 필수 요소 1개 (구분 코드 GUBN)
            - 구분 코드(gubn: QueryString) 
            - Success Test Case 25개
            - Error Test Case 4개 
    3. Parameters
        1) 서울시 하수관로 Open API 응답 데이터
            - IDN : String
            - GUBN : Int
            - GUBN_NAM : String
            - MEA_YMD : YYYYMMDDHH24
            - MEA_WAL : Float
            - SIG_STA : String
        2) 서울시 강우량 Open API 응답 데이터
            - RAINGAUGE_CODE : Float,
            - RAINGAUGE_NAME : String,
            - GU_CODE : Float,
            - GU_NAME : String,
            - RAINFALL10 : Float,
            - RECEIVE_TIME : YYYYMMDDHH24
    """
    
    maxDiff = None
    
    """
    success test case
    """
    
    def test_success_seoul_data_gubn_code_01(self):
        gubn     = '종로'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
    
    def test_success_seoul_data_gubn_code_02(self):
        gubn     = '중'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_03(self):
        gubn     = '용산'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_04(self):
        gubn     = '성동'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_05(self):
        gubn     = '광진'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_06(self):
        gubn     = '동대문'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_07(self):
        gubn     = '중랑'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_08(self):
        gubn     = '성북'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_09(self):
        gubn     = '강북'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_10(self):
        gubn     = '도봉'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_11(self):
        gubn     = '노원'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_12(self):
        gubn     = '은평'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_13(self):
        gubn     = '서대문'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])

    def test_success_seoul_data_gubn_code_14(self):
        gubn     = '마포'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_15(self):
        gubn     = '양천'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_16(self):
        gubn     = '강서'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_17(self):
        gubn     = '구로'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_18(self):
        gubn     = '금천'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_19(self):
        gubn     = '영등포'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_20(self):
        gubn     = '동작'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_21(self):
        gubn     = '관악'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_22(self):
        gubn     = '서초'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_23(self):
        gubn     = '강남'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_24(self):
        gubn     = '송파'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
        
    def test_success_seoul_data_gubn_code_25(self):
        gubn     = '강동'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(gubn, response.json()['gu_name'])
        self.assertEqual(float, type(response.json()['avg_water_level']))
        self.assertEqual(float, type(response.json()['raingauge_info'][0]['sum_rain_fall']))
        self.assertIn('gu_name', response.json())
        self.assertIn('avg_water_level', response.json())
        self.assertIn('raingauge_info', response.json())
        self.assertIn('raingauge_name', response.json()['raingauge_info'][0])
        self.assertIn('sum_rain_fall', response.json()['raingauge_info'][0])
    
    """
    fail test case
    """
    
    def test_fail_seoul_data_due_to_no_gubn_param(self):
        response = self.client\
                       .get('/api/seoul/sewerlevel-rainfall?gubn=', content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {
                'detail': '구이름을 입력하세요.'
            }
        )
        
    def test_fail_seoul_data_due_to_gubn_param_not_existed(self):
        gubn     = '우리집'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {
                'detail': f'{gubn}구 지역은 존재하지 않습니다.'
            }
        )
    
    @patch('core.sewer_pipe.requests')
    def test_fail_seoul_data_due_to_sewer_pipe_open_api_error(self, mocked_requests):
        
        class MockedResponse:
            data = {
                'DrainpipeMonitoringInfo':
                    {'RESULT': 
                        {'CODE': 'ERROR-500',\
                            'MESSAGE': '서버 오류입니다. 지속적으로 발생시 열린 데이터 광장으로 문의(Q&A) 바랍니다.'
                    }
                }
            }
            content = json.dumps(data)
            
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        
        gubn     = '종로'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {
                'detail': '서울시 해당지역의 공공데이터를 찾지 못했습니다.'
            }    
        )
        
    @patch('core.rainfall.requests')
    def test_fail_seoul_data_due_to_rainfall_open_api_error(self, mocked_requests):
        
        class MockedResponse:
            data = {
                'ListRainfallService':
                    {'RESULT': 
                        {'CODE': 'ERROR-500',\
                            'MESSAGE': '서버 오류입니다. 지속적으로 발생시 열린 데이터 광장으로 문의(Q&A) 바랍니다.'
                    }
                }
            }
            content = json.dumps(data)
            
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        
        gubn     = '종로'
        response = self.client\
                       .get(f'/api/seoul/sewerlevel-rainfall?gubn={gubn}', content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {
                'detail': '서울시 해당지역의 공공데이터를 찾지 못했습니다.'
            }    
        )    