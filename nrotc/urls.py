from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='nrotc-home'),
    path('download/', views.download_docx, name='download'),
    path('contact/', views.contact_view, name='contact'),
    path('conv-order/', views.conv_order_view, name='conv-order'),
    path('prb-report/', views.prb_report_view, name='prb-report'),
    path('pns-rec/', views.pns_rec_view, name='pns-rec'),
    path('co-sum-letter/', views.co_sum_letter_view, name='co-sum-letter'),
    path('student-prb-waiver/', views.student_prb_waiver_view, name='student-prb-waiver'),
    path('pns-prb-waiver/', views.pns_prb_waiver_view, name='pns-prb-waiver'),
    path('prb-date-change/', views.prb_date_change_view, name='prb-date-change'),
]