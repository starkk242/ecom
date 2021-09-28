from django.contrib.auth import get_user_model
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from accounts import models

try:
    from allauth.utils import email_address_exists
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

User = get_user_model()


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email","phone_number","ref_code")


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={"input_type": "password"})


class CustomRegisterSerializer(serializers.Serializer):
    """
    Modified RegisterSerializer class from rest_auth
    """

    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(write_only=True, style={"input_type": "password"})
    phone_number = serializers.CharField()
    ref_code = serializers.CharField(required=False)


    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address."
            )
        return email

    def validate_password(self, password):
        if len(password) < 5:
            raise serializers.ValidationError(
                "Password Should be Minimum 5 characters long"
            )
        return password

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password": self.validated_data.get("password", ""),
            "email": self.validated_data.get("email", ""),
            "phone_number" : self.validated_data.get("phone_number",""),
            "ref_code": self.validated_data.get("ref_code",""),
        }
    
    def validate_ref_code(self,ref_code):
        try:
            obj = models.ReferalCode.objects.get(referal_code=ref_code)
            return ref_code
        except:
            raise serializers.ValidationError("Referal Code Does not Exist")

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user
