from django.urls import path


from .views import HomePageView, linkedinView, gitHubView, credlyView, twitterView, facebookView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('linkedin', linkedinView, name='linked-in'),
    path('github', gitHubView, name='github'),
    path('credly', credlyView, name='credly'),
    path('twitter', twitterView, name='twitter'),
    path('facebook', facebookView, name='facebook'),
]