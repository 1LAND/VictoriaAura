from django.http.response import HttpResponseRedirect

from django.http.request import HttpRequest

import requests

from rest_framework.response import Response
from rest_framework.decorators import action,api_view
from rest_framework.viewsets import ModelViewSet


from .serializers import NewsSerializers,ImgSerializer,GameDisciplineSerializer,UserMinInfoSerializer,UserMaxInfoSerializer,TeamSerializer
from .models import News,ImgFiles,GameDiscipline,User,Team
from rest_framework.permissions import IsAdminUser

from config import CONFIG_DONATION_ALERT as CDA

DEFAULT_URL = "https://www.donationalerts.com/oauth/"
DEFAULT_API_LINK = "https://www.donationalerts.com/api/v1/"


def get_access_token(code):
    return requests.post(
        f"https://www.donationalerts.com/oauth/token",
        data={
            "grant_type":"authorization_code",
            "client_id":CDA['client_id'],
            "client_secret":CDA['client_secret'],
            "redirect_uri":CDA['redirect_uri'],
            "code":code
        },
        proxies={"http": "Http Proxy"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
        ).json()['access_token']


@api_view(['GET'])
def donation_alerts_login(request):
    if request.method == 'GET':
        return HttpResponseRedirect(redirect_to=f"{DEFAULT_URL}authorize?client_id={CDA['client_id']}&redirect_uri={CDA['redirect_uri']}&response_type=code&"\
        "scope=oauth-user-show%20oauth-donation-subscribe%20oauth-donation-index%20oauth-custom_alert-store%20oauth-goal-subscribe%20oauth-poll-subscribe")

@api_view(['GET'])
def donation_alerts(request):
    code = request.GET.get("code")
    access_token = get_access_token(code)
    objs = requests.get(f"{DEFAULT_API_LINK}alerts/donations?page=1",proxies={"http": "Http Proxy"}, headers={"Authorization": f"Bearer {access_token}"}).json()
    return Response([{"group":i['username'],"users":i['message'],"amount":i['amount'],"currency": i["currency"]} for i in objs['data']])



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