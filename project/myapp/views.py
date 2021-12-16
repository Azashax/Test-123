from rest_framework.generics import *
from .serializers import *
from .models import *


class UserCategoryListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))