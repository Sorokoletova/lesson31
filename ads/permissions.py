from rest_framework.permissions import BasePermission
from ads.models import User, Selection
class AdsEditPermission(BasePermission):
    message = "Редактировать могут только админ или модератор"

    def has_permission(self, request, view):
        if request.user.role in [User.MODERATOR, User.ADMIN]:
            return True
        try:
            ads = Ads.objects.get(pk=view.kwargs['pk'])
        except Ads.DoesNotExist:
            raise 404

        if ads.autor_id == request.user.id:
            return True
        return False

class SelectionEditPermission(BasePermission):
    message = "Редактировать могут только админ или модератор"

    def has_permission(self, request, view):

        try:
            selection = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            raise 404

        if selection.owner_id == request.user.id:
            return True
        return False