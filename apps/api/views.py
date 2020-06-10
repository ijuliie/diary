from .models import Entry
from .serializers import EntrySerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny

class EntryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print("i am calling the get query set")
        queryset = Entry.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = EntrySerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied("You must have an account to make an entry")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        entry = Entry.objects.get(pk=self.kwargs['pk'])
        if not request.user == entry.owner:
            raise PermissionDenied("You don't have permission to edit this entry")
        return super().update(request, *args, **kwargs)

    def destory(self, request, *args, **kwargs):
        entry = Entry.objects.get(pk=kwargs['pk'])
        if not request.user == entry.owner:
            raise PermissionDenied('You do not have permission to remove this entry')
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateEntry(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Entry.objects.filter(is_public=True)
    serializer_class = EntrySerializer
            
    def perform_create(self, serializer):
        serializer.save()


class EntryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Entry.objects.all()
        return queryset

    serializer_class = EntrySerializer

class EntryPublicView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        queryset = Entry.objects.order_by('-created_at').filter(is_public=True)
        return queryset

    serializer_class = EntrySerializer