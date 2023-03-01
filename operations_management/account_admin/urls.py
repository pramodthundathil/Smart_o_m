from django.urls import path
from.import views

urlpatterns = [
    path('accountadmin',views.accountadmin,name='accountadmin'),
    path('conveyance',views.conveyance,name= 'conveyance'),
    path("addcoveyance",views.addcoveyance,name="addcoveyance"),
    path("ConveyanceApprove",views.ConveyanceApprove,name="ConveyanceApprove"),
    path("conveyancechange/<int:pk>",views.conveyancechange,name="conveyancechange"),
    path("WorkReports",views.WorkReports,name="WorkReports"),
    path("AddWork",views.AddWork,name="AddWork"),
    path("AllWorks",views.AllWorks,name="AllWorks"),
    path("DeleteWork/<int:pk>",views.DeleteWork,name="DeleteWork"),
    path("TakeWork/<int:pk>",views.TakeWork,name="TakeWork"),
    
]
