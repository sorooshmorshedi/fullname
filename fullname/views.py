from rest_framework.views import APIView
from fullname.models import User
from fullname.serializer import UserSerializer, UserEditSerializer
from rest_framework import status
from rest_framework.response import Response


class UserApiView(APIView):
    def get(self, request):
        query = User.objects.all()
        serializer = UserSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEdit(APIView):
    def put(self, request, pk):
        query = User.objects.filter(pk=pk).first()
        serializer = UserEditSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.filter(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = UserSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
