from django.core.mail import send_mail


def contact(request):
    name=request.POST.get('name', '')
    phone=request.POST.get('phone', '')
    email=request.POST.get('email', '')
    text=request.POST.get('text', '')
    data={"name":name,"phone":phone,'email':email,'text':text}
    send_mail('Анкета девочки',str("Имя девочки: "+data['name']+"\n"+"Номер телефона: "+data["phone"]+"\n"+"Email: "+data['email']+'\n'+"Сообщение: "+data['text']+'\n'+"Это письмо сформировано автоматически. Пожалуйста, не отвечайте на него."), 'llipyc999@gmail.com',['charmstudioomsk@mail.ru'], fail_silently=False)
    