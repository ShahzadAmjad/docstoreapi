from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from . import serializers
from . models import documents
# from . models import folders
# from . models import topics
from . serializers import documentSerializers

class documentList(APIView):
    def get(self,request, *args, **kwargs):
        fol_name=self.request.query_params["fol_name"]
        top_name=self.request.query_params["top_name"]
        print("Folder name: "+fol_name);
        print("Topic Name"+top_name);
        documentById= documents.objects.get(fol_name=fol_name , top_name=top_name)
        #employees1=folders.objects.values('fol_id').filter(fol_name='feedback')
        employees1 = documents.objects.all()
        serializer=documentSerializers(documentById)
        return Response(serializer.data)

    #queryset = documents.objects.all();
    #serializer_class=documentSerializers()

class documentCreate(generics.CreateAPIView):
    queryset = documents.objects.all();
    serializer_class=documentSerializers()


class documentDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = documents.objects.all()
    serializer_class = documentSerializers


class documentUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = documents.objects.all()
    serializer_class = documentSerializers


class documentDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = documents.objects.all()
    serializer_class = documentSerializers
 #   def get(self,request):
        #employees1=employee.objects.all()
        #serializer=employeesSerializers(employees1, many=True)
        #return Response(serializer.data)

  #  def post(self):
        #pass

