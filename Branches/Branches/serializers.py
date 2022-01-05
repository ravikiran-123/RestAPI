from rest_framework.serializers import ModelSerializer

from sbi.models import Banking

class BankSerializer(ModelSerializer):
    class Meta:
        model=Banking
        fields='__all__'