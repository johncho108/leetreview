from rest_framework.serializers import ModelSerializer
from base.models import Entry

class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
