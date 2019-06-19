from rest_framework import status
from rest_framework.response import Response

from . import models as m
from . import serializers as s
from ..core.views import ApproveViewSet, TMSViewSet


class DepartmentViewSet(TMSViewSet):

    queryset = m.Department.objects.all()
    serializer_class = s.DepartmentSerializer
    short_serializer_class = s.ShortDepartmentSerializer


class PositionViewSet(TMSViewSet):

    queryset = m.Position.objects.all()
    serializer_class = s.PositionSerializer
    short_serializer_class = s.ShortPositionSerializer


class RoleManagementViewSet(TMSViewSet):

    queryset = m.RoleManagement.objects.all()
    serializer_class = s.RoleManagementSerializer
    data_view_serializer_class = s.RoleManagementDataViewSerializer


class RestRequestViewSet(ApproveViewSet):

    queryset = m.RestRequest.objects.all()
    serializer_class = s.RestRequestSerializer
    data_view_serializer_class = s.RestRequestDataViewSerializer


class StaffProfileViewSet(TMSViewSet):

    queryset = m.StaffProfile.objects.all()
    serializer_class = s.StaffProfileSerializer
    short_serializer_class = s.ShortStaffProfileSerializer
    data_view_serializer_class = s.StaffProfileDataViewSerializer

    def create(self, request):
        context = {
            'user': request.data.pop('user'),
            'driver_license': request.data.pop('driver_license')
        }

        serializer = self.serializer_class(
            data=request.data, context=context
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, pk=None):
        serializer_instance = self.get_object()
        context = {
            'user': request.data.pop('user'),
            'driver_license': request.data.pop('driver_license')
        }

        serializer = self.serializer_class(
            serializer_instance,
            data=request.data,
            context=context,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class CustomerProfileViewSet(TMSViewSet):

    queryset = m.CustomerProfile.objects.all()
    serializer_class = s.CustomerProfileSerializer
    short_serializer_class = s.ShortCustomerProfileSerializer
    data_view_serializer_class = s.CustomerProfileDataViewSerializer

    def create(self, request):
        context = {
            'user': request.data.pop('user'),
            'products': request.data.pop('products')
        }

        serializer = self.serializer_class(
            data=request.data, context=context
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, pk=None):
        serializer_instance = self.get_object()
        context = {
            'user': request.data.pop('user'),
            'products': request.data.pop('products')
        }

        serializer = self.serializer_class(
            serializer_instance,
            data=request.data,
            context=context,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )