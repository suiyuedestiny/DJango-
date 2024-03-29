from django.shortcuts import render, redirect
from app0326 import models
from django import forms
# Create your views here.


def depart_add(request):

    if request.method == 'GET':
        return render(request, 'depart_add.html')

    depar_name = request.POST.get('departname')

    models.Department.objects.create(title=depar_name)

    return redirect('/depart/list/')


def depart_del(request):

    depart_id = request.GET.get('id')
    models.Department.objects.filter(id=depart_id).delete()

    return redirect('/depart/list/')


def depart_list(request):

    depart_object = models.Department.objects.all()

    return render(request, 'depart_list.html', {'depart_obj': depart_object})


def depart_edit(request, nid):

    if request.method == "GET":
        # depart_id = request.GET.get('id')
        depart_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html',  {'depart_obj': depart_object})


    depart_name = request.POST.get('departname')

    # depart_id = request.GET.get('id')
    models.Department.objects.filter(id=nid).update(title=depart_name)
    return redirect('/depart/list/')



def user_list(request):

    user_object = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'user_obj': user_object})

##############################################################################

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username', 'password', 'age', 'account', 'creat_time', 'depart', 'gener']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'account': forms.TextInput(attrs={'class': 'form-control'}),
            'creat_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'depart': forms.Select(attrs={'class': 'form-control'}),
            'gener': forms.Select(attrs={'class': 'form-control'}),

        }
def user_add(request):

    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})


    form = UserModelForm(data=request.POST)

    # 如果检验成功
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list')
    else:
        print(form.errors)
        return render(request, 'user_add.html', {'form': form})



def user_edit(request, nid):

    if request.method == 'GET':
        user_title = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=user_title)
        return render(request, 'user_edit.html', {'form': form})

    user_id = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=user_id)
    if form.is_valid():
        #增加一些不需要用户输入的值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list')

    return render(request, 'user_edit.html', {'form': form})



def user_del(request, nid):

        models.UserInfo.objects.filter(id=nid).delete()

        return redirect('/user/list/')


################################################ 靓号管理

def prettyNum_list(request):

    PrettyNum_obj = models.PrettyNum.objects.all()

    return render(request, 'prettyNum_list.html', {'PrettyNum': PrettyNum_obj})

class PrettyModelForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNum
        # fields = ['mobile', 'price', 'level', 'status']
        fields = '__all__'
        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    # def __int__(self, *args, **kwargs):
    #     super().__int__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {'class': 'form-control'}

def prettyNum_add(request):

    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'prettyNum_add.html', {'form': form})

    form = PrettyModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettyNum/list/')


    return  render(request, 'prettyNum_add.html', {'form': form})












