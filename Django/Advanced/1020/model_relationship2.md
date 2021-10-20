[TOC]



# Model Relationship II 

## 1. Intro : 병원 진료 기록 시스템

### 1. 1 병원 진료 기록 시스템을 통한 M: N 관계 학습

- 환자와 의사가 사용하는 병원 진료 기록 시스템 구축
- 모델링은 현실 세계를 최대한 유사하게 반영하기 위한 것



### 1. 2  1:N의 한계

- 1: N 모델 관계 설정

  한 명의 의사가 여러 환자 진료 가능

  ```python
  from django.db import models
  
  # Create your models here.
  class Doctor(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  
  class Patient(models.Model):
      name = models.TextField()
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  

- 마이그레이션 후 shell_plus 실행

  ```shell
  In [1]: doctor1 = Doctor.objects.create(name='justin')
  
  In [2]: doctor2 = Doctor.objects.create(name='eric')
  
  In [3]: patient1 = Patient.objects.create(name='tony', doctor=doctor1)
  
  In [4]: patient2 = Patient.objects.create(name='harry', doctor=doctor2)
  ```

  

- 1번 환자가 1번 의사 진료 마치고 2번 의사에게 방문하려면 새로운 예약 생성해야함

- 기존 예약 유지한 채로 새로운 예약 생성해아함

- 새로 생성한 3번 환자는 1번 환자와 다름!! id값 3

- 한 번에 두 의사에게 진료받고자 한다면...?

- 하나의 외래 키에 2개의 의사 데이터를 넣을 수 없음

- 새로운 예약 생성하는 것이 불가능

- 여러 의사에게 진료받은 기록을 환자 한 명에 저장할 수 없음

  

### 1.3 중개 모델

- 중개 모델 작성ㅊㅇ
