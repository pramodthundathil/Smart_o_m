from django.urls import path
from.import views

urlpatterns = [
    path('approvals',views.approvals,name='approvals'),

    path('leave_approve',views.leave_approve,name='leave_approve'),
    path('leave_aprv',views.leave_aprv,name='leave_aprv'),
    path('leave_status',views.leave_status,name='leave_status')

    
]
