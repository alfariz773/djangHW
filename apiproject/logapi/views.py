# from rest_framework import status
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from django.contrib.auth.forms import UserCreationForm

# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def signup(request):
#     form = UserCreationForm(data=request.data)
#     if form.is_valid():
#         user = form.save()
#         return Response("account created successfully", status=status.HTTP_201_CREATED)
#     return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},status=HTTP_200_OK)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def signup(request):
    name = request.data.get('name')
    password = request.data.get('password')

    if not name or not password:
        return Response({'error': 'Name and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=name).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=name, password=password)
    Token.objects.create(user=user)
    return Response({'message': 'Account created successfully!'}, status=status.HTTP_201_CREATED)


 
@api_view(['POST'])
def login(request):
    name = request.data.get('name')
    password = request.data.get('password')

    user = authenticate(username=name, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'name': user.username,
        'token': token.key
    }, status=status.HTTP_200_OK)
