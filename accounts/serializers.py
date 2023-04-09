import re
from rest_framework.exceptions import ValidationError
from .models import User
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    """
        회원가입 Serializer
    """
    check_password = serializers.CharField(style={'input_type': 'password'}, write_only=True
                                           , required=True)

    class Meta:
        model = User
        fields = ('nickname', 'password', 'check_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'check_password': {'write_only': True},
        }

    """
        유효성 검사
    """

    def validate_nickname(self, value):
        """
            닉네임 정규화 확인
        """
        if re.search(r'^[a-zA-Z0-9]{4,12}$', value) or re.search(r'^[a-zA-Z]{4,12}$', value):
            return value
        raise ValidationError('닉네임은 4글자 이상 12글자 이하이며 영어 또는 영어+숫자만 사용가능합니다.')

    def validate_password(self, value):
        """
            비밀번호 정규화 확인
        """
        if not re.search(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,15}$', value):
            raise ValidationError('비밀번호는 8글자 이상, 15글자 이하이며 특수문자, 숫자를 포함해야 합니다.')
        return value

    def validate(self, attrs):
        """
            비밀번호, 비밀번호 체크 가 같은값인지 확인
        """
        password = attrs.get('password')
        check_password = attrs.get('check_password')
        if password != check_password:
            raise ValidationError('입력된 두 비밀번호가 다릅니다.')
        return attrs

    def create(self, validated_data):
        validated_data.pop('check_password')
        user = User.objects.create_user(**validated_data)
        return user