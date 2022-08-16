import json
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.serializers import CategorySerializer, AdsSerializer, AdsCreateSerializer, AdsUpdateSerializer, \
    AdsDeleteSerializer, AdsUploadeImageSerializer, SelectionSerializer, SelectionDetailSerializer, \
    SelectionCreateSerializer, SelectionUpdateSerializer, SelectionDeleteSerializer
from rest_framework.viewsets import ModelViewSet
from ads.permissions import AdsEditPermission, SelectionEditPermission
from ads.models import Ads, Categorie, Selection
from django.conf import settings


class CategoryViewSet(ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer
    permission_classes = [IsAuthenticated, AdsEditPermission]


class AdsDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsDeleteSerializer
    permission_classes = [IsAuthenticated, AdsEditPermission]


class AdsUploadImageView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUploadeImageSerializer
    permission_classes = [IsAuthenticated, AdsEditPermission]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get("image", None)
        self.object.save()
        return self.update(request, *args, **kwargs)


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDeleteSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]
