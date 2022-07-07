from rest_framework import serializers


class RainfallDataSerializer(serializers.Serializer):
    raingauge_name = serializers.CharField(max_length=50)
    sum_rain_fall  = serializers.FloatField()
    

class SeoulOpenDataSerializer(serializers.Serializer):
    gu_name         = serializers.CharField(max_length=20)
    avg_water_level = serializers.FloatField()
    raingauge_info  = RainfallDataSerializer(many=True)