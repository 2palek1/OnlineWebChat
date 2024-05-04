from django.urls import path
from .views import deleteMember, lobby, room, getToken, createMember, getMember


urlpatterns = [
    path('', lobby),
    path('room/', room),
    path('get_token/', getToken),
    path('create_member/',createMember),
    path('get_member/', getMember),
    path('delete_member/', deleteMember),
]