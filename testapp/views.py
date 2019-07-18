from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.template import RequestContext
from django.template import loader


# Create your views here.
class test1_View(generic.TemplateView):
    # template_nameは利用するテンプレート名
    template_name = 'testapp/test1.html'

    def post(self, request, *args, **kwargs):

        request.session['buttonname'] = request.POST
        Ttext = {'texttest': 'aa'}

        if 'button_1' in request.POST:
            # redirectで画面遷移
            # return redirect('/test2/')
            return redirect('testapp:test2')
        elif 'button_2' in request.POST:
            # HttpResponseRedirectで画面遷移
            # return HttpResponseRedirect('/test2/')
            return HttpResponseRedirect(reverse('testapp:test2'))
            # ↓↓redirectとは違い、逆引きするためにはreverseを使用しなければならない。
            # return HttpResponseRedirect('testapp:test2')
        elif 'button_3' in request.POST:
            return render(request,'testapp/test2.html',Ttext)
        elif 'button_4' in request.POST:
            return render_to_response('testapp/test2.html',Ttext)
        elif 'button_5' in request.POST:
            temp = loader.get_template('testapp/test2.html')
            return HttpResponse (temp.render(Ttext,request))
        #else:
        return redirect("testapp:test1")

    def get(self, request, *args, **kwargs):

        Ttext = {'texttest': 'aa'}

        if 'Gbutton_1' in request.GET:
            #return render(request,'testapp/test2.html',{'texttest':'aa'})
            return render(request,'testapp/test2.html',Ttext)

        return render(request,'testapp/test1.html')
        #return render(request,'')
        #return generic.TemplateView.get(self, request, *args, **kwargs)

test1_view = test1_View.as_view()

class test2_View(generic.TemplateView):
    # template_nameは利用するテンプレート名
    template_name = 'testapp/test2.html'

    def post(self, request, *args, **kwargs):
        if 'buttonname' in self.request.session:
            buttonname = self.request.session['buttonname']
            print('セッション残ってる' + str(buttonname))
        else:
            print('セッション残ってない。。')
        return HttpResponseRedirect(reverse('testapp:test1'))

    def get(self, request, *args, **kwargs):
        Ttext = {'texttest': 'aa'}

        if 'Pbutton_01' in request.GET:
            #return render(request,'testapp/test2.html',{'texttest':'aa'})
            return render(request,'testapp/test2.html',Ttext)

        return render(request,'testapp/test2.html',Ttext)
        #return generic.TemplateView.get(self, request, *args, **kwargs)
