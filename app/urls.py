from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app.views import (
    TeamList,
    TournamentDetail,
    TournamentList,
    TournamentParticipantDetail,
    UserList,
)

schema_view = get_schema_view(
    info=openapi.Info(title="Tournament Table API", default_version="1.0.0"),
    public=True,
)

urlpatterns = [
    path("api/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
]

urlpatterns += [
    # Пользователи
    path("api/users", UserList.as_view(), name="users"),
    # Команды
    path("api/teams", TeamList.as_view(), name="teams"),
    # Турниры
    path("api/tournaments", TournamentList.as_view(), name="tournaments"),
    path("api/tournaments/<id>", TournamentDetail.as_view(), name="tournament"),
    path(
        "api/tournaments/<id>/participants/<team_id>",
        TournamentParticipantDetail.as_view(),
        name="tournament_participant",
    ),
]
