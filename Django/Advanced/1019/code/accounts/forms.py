from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model   


class CustomUserCreationForm(UserCreationForm):
    # 기존의 장고가 유저 생성하는 것을 고쳐서 쓸 것임

    class Meta(UserCreationForm.Meta):  # UserCreationForm 클래스 안의 Meta클래스 상속
        model = get_user_model()  # 새로 정의함 : overriding, 어떻게 일어나느냐? 
                                  # 현재 meta 클래스에서 찾는 거고
        # get_user_model() : 현재 활성화된 user모델을 찾아오는 것
        fields = UserCreationForm.Meta.fields                  

        # 나머지는 상속받은(부모)의 UserCreationForm.Meta