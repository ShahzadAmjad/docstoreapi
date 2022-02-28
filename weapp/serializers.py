from rest_framework import serializers
from . models import documents
# from . models import folders
# from . models import topics



class documentSerializers(serializers.ModelSerializer):

    class Meta:
        model=documents
        #fields=['doc_name']
        fields='__all__'