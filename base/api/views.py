from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Entry
from .serializers import EntrySerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/entries',
        'GET /api/entry/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getEntries(request):
    entries = Entry.objects.all()
    serializer = EntrySerializer(entries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEntry(request, pk):
    entry = Entry.objects.get(id=pk)
    serializer = EntrySerializer(entry, many=False)
    return Response(serializer.data)
