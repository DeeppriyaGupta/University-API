from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import UniversityViewSet, ProgramViewSet, StudentViewSet

router=routers.DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'students', StudentViewSet)

urlpatterns=[
    path('', include(router.urls))
    # path('universities/<int:pk>/', UniversityViewSet.as_view(), name='universityviewset')
]

#localhost:8000/api/university/{universityId}/programs/{programId}/student