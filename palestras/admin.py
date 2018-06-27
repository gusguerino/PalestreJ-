from django.contrib import admin
from django.urls import reverse
from .models import Palestra, Pergunta
from django.utils.safestring import mark_safe


@admin.register(Pergunta)
class PalestraAdmin(admin.ModelAdmin):
    list_display = (
        'pergunta', 'palestra', 'autor', 'aceita'
    )

    search_fields = [
        'pergunta', 'autor'
    ]

    def aceita(self, obj):
        return obj.foi_aceita()
    aceita.boolean = True


class PerguntasInline(admin.TabularInline):
    model = Pergunta


@admin.register(Palestra)
class PalestraAdmin(admin.ModelAdmin):
    inlines = [
        PerguntasInline
    ]
    list_display = (
        'titulo', 'palestrante', 'perguntas', 'perguntas_aceitas', 'visualizar_perguntas'
    )
    search_fields = [
        'titulo', 'palestrante'
    ]

    def visualizar_perguntas(self, obj):
        redirect_url = reverse('admin:palestrante_pergunta_changelist')
        extra = "?palestra__id__exact=%d" % (obj.id)
        return mark_safe("<a href='{}'>Questões</a>".format(redirect_url + extra))

    def perguntas(self, obj):
        print(obj.quantidade_perguntas())
        return obj.quantidade_perguntas()

    def perguntas_aceitas(self, obj):
        return obj.quantidade_perguntas_aceitas()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)
