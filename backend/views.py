from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


from .serializers import NewsSerializers,ImgSerializer,GameDisciplineSerializer,UserMinInfoSerializer,UserMaxInfoSerializer,TeamSerializer
from .models import News,ImgFiles,GameDiscipline,User,Team
from rest_framework.permissions import IsAdminUser


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserMinInfoSerializer

    @action(methods=['get'],detail=True,permission_classes=[IsAdminUser])
    def all(self,request,pk=None):
        data = User.objects.filter(pk=pk)
        serializer = UserMaxInfoSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data[0]) 

class NewsViewSet(ModelViewSet):
    queryset = News.objects.only('id','short_text','slug','img').select_related('img').order_by('-date','-time').all()
    serializer_class = NewsSerializers

class GameDisciplineViewSet(ModelViewSet):
    queryset = GameDiscipline.objects.all()
    serializer_class = GameDisciplineSerializer

class ImgViewSet(ModelViewSet):
    queryset = ImgFiles.objects.only('file','name')
    serializer_class = ImgSerializer
    @action(methods=['get'],detail=False)
    def MN(self,request):
        data = self.get_queryset().filter(type_img='MN')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    @action(methods=['get'],detail=False)
    def TO(self,request):
        data = self.get_queryset().filter(type_img='TO')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    @action(methods=['get'],detail=False)
    def NW(self,request):
        data = self.get_queryset().filter(type_img='NW')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    @action(methods=['get'],detail=False)
    def US(self,request):
        data = self.get_queryset().filter(type_img='US')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)    
    @action(methods=['get'],detail=False)
    def TM(self,request):
        data = self.get_queryset().filter(type_img='TM')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    @action(methods=['get'],detail=False)
    def CO(self,request):
        data = self.get_queryset().filter(type_img='CO')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    @action(methods=['get'],detail=False)
    def GD(self,request):
        data = self.get_queryset().filter(type_img='GD')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)