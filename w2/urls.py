from django.urls import path

from . import views

urlpatterns = [
    path('', views.signin, name="登入畫面"),
    path('signin', views.signin, name="登入畫面"),
    path('首頁', views.首頁, name="首頁"),
    path('遊戲選擇畫面', views.遊戲選擇畫面, name="遊戲選擇畫面"),
    path('簽到', views.簽到, name="簽到"),
    path('商店', views.商店, name="商店"),
    path('衣櫥', views.衣櫥, name="衣櫥"),
    path('紀錄', views.紀錄, name="紀錄"),
    path('紀錄上肢', views.紀錄上肢, name="紀錄上肢"),
    path('紀錄下肢', views.紀錄下肢, name="紀錄下肢"),
    path('紀錄四肢', views.紀錄四肢, name="紀錄四肢"),
    path('紀錄手部', views.紀錄手部, name="紀錄手部"),
    path('上肢遊戲畫面-解說', views.上肢遊戲畫面解說, name="上肢遊戲畫面-解說"),
    path('下肢遊戲畫面-解說', views.下肢遊戲畫面解說, name="下肢遊戲畫面-解說"),
    path('四肢遊戲畫面-解說1', views.四肢遊戲畫面解說1, name="四肢遊戲畫面-解說1"),
    path('四肢遊戲畫面-解說2', views.四肢遊戲畫面解說2, name="四肢遊戲畫面-解說2"),
    path('手部遊戲畫面-解說', views.手部遊戲畫面解說, name="手部遊戲畫面-解說"),
    path('遊戲畫面倒數-上肢', views.遊戲畫面倒數上肢, name="遊戲畫面倒數-上肢"),
    path('遊戲畫面倒數-下肢', views.遊戲畫面倒數下肢, name="遊戲畫面倒數-下肢"),
    path('遊戲畫面倒數-四肢', views.遊戲畫面倒數四肢, name="遊戲畫面倒數-四肢"),
    path('遊戲畫面倒數-手部', views.遊戲畫面倒數手部, name="遊戲畫面倒數-手部"),
    path('遊戲畫面-上肢/', views.遊戲畫面上肢, name="遊戲畫面-上肢"),
    path('遊戲畫面-下肢/', views.遊戲畫面下肢, name="遊戲畫面-下肢"),
    path('遊戲畫面-四肢/', views.遊戲畫面四肢, name="遊戲畫面-四肢"),
    path('遊戲畫面-手部/', views.遊戲畫面手部, name="遊戲畫面-手部"),
    path('signup', views.signup, name="signup"),
    path('home', views.首頁, name="首頁"),
    path('遊戲難度選擇-上肢', views.遊戲難度選擇上肢, name="遊戲難度選擇-上肢"),
    path('遊戲難度選擇-下肢', views.遊戲難度選擇下肢, name="遊戲難度選擇-下肢"),
    path('遊戲難度選擇-四肢', views.遊戲難度選擇四肢, name="遊戲難度選擇-四肢"),
    path('遊戲難度選擇-手部', views.遊戲難度選擇手部, name="遊戲難度選擇-手部"),
    
]
