from rest_auth.views import LoginView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomRegisterSerializer, User
from accounts.models import CustomUser
from accounts import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db.models import Q


@permission_classes([])
class CustomLoginView(LoginView):
    def post(self,request):
        if "email" not in request.data or "password" not in request.data:
            return Response({
                "message" : "Email and Password are Required"
            },status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']

        try:
            CustomUser.objects.get(email=email)
            user = authenticate(email=email, password=password)
            if user is not None:
                token = Token.objects.get_or_create(user=user)
                print(token)
                return Response({
                    "token" : token[0].key,
                    "id":user.id,
                    "first_name" : user.first_name,
                    "last_name" : user.last_name,
                    "email" : user.email,
                    "phone_number" : user.phone_number
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message" : "Email or Password is incorrect"
                }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({
                "message" : "Account Does Not Exist"
            }, status=status.HTTP_404_NOT_FOUND)



@permission_classes([])
class CustomRegisterView(APIView):
    def post(self,request):
        # serializer_class = CustomRegisterSerializer
        if "email" not in request.data or "password" not in request.data or "first_name" not in request.data or "last_name" not in request.data or "phone_number" not in request.data:
            return Response("All Fields Are Required",status=status.HTTP_400_BAD_REQUEST)
        email = request.data["email"]
        password = request.data["password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        phone_number = request.data["phone_number"]
        ref_code = ""
        if len(password)<5:
            return Response({
                "message":"Password Should not be less than 5"
            },status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(email=email)
            return Response("User Already exists with Email",status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            return Response("User Already exists with Phone Number",status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        
        if "ref_code" in request.data:
            ref_code = request.data["ref_code"]
            try:
                obj = models.ReferalCode.objects.get(referal_code=ref_code)
            except:
                return Response({
                    "message" : "Referal Code Doesnot Exists"
                },status=status.HTTP_400_BAD_REQUEST)
        
        serializer_class = CustomRegisterSerializer(data=request.data)
        print(serializer_class.is_valid())
        user = CustomUser.objects.create(
            email = email,
            first_name = first_name,
            last_name=last_name,
            phone_number=phone_number,
            ref_code=ref_code
            )
        user.set_password(password)
        user.save()

        return Response({
            "message" : "User Successfully Created"
        },status=status.HTTP_201_CREATED)

        



