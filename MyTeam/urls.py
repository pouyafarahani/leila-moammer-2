from django.urls import path

from .views import MyTeamView, UserDetailView, OstadDetailView, RezervTeamView, RezervOstadView, send_request_to_rezerv_zarinapl

app_name = 'my_team'

urlpatterns = [
    path('', MyTeamView, name='my_team'),
    path('<int:pk>/', UserDetailView, name='user_detail'),
    path('leilamoammer/<int:pk>/', OstadDetailView, name='ostad_detail'),
    path('leilamoammer/<int:rezerv_id>/', send_request_to_rezerv_zarinapl, name='send_request_to_rezerv_zarinpal'),
    path('rezerv/<int:pk>/', RezervTeamView, name='rezerv_team'),
    path('rezerv/leila/<int:pk>/', RezervOstadView, name='rezerv_ostad'),
]

