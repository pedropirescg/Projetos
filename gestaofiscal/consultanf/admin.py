from django.contrib import admin
from consultanf.models import NotaFiscal, ItemNF, Produto, Empresa

#admin.site.register(NotaFiscal)
@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('numero', 'empresa', 'serie')
#admin.site.register(ItemNF)
@admin.register(ItemNF)
class ItemNFAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Produto)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Empresa)
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass