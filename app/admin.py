from django.contrib import admin

# Register your models here.
from app.models import Korisnik, Objava, Komentar, Blokiran


class KorisnikAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Korisnik, KorisnikAdmin)


class ObjavaAdmin(admin.ModelAdmin):
    search_fields = ("naslov", "sodrzina")
    list_display = ("naslov", "user")
    list_filter = ("datum_kreiranje",)

    def has_change_permission(self, request, obj=None):
        if obj and (obj.user.user == request.user or request.user.is_superuser):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (obj.user.user == request.user or request.user.is_superuser):
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = Korisnik.objects.get(user=request.user)
        blocked = Blokiran.objects.filter(blokiran=user).values_list('blokiral', flat=True)
        qs = qs.exclude(user__in=blocked)
        return qs


admin.site.register(Objava, ObjavaAdmin)


class KomentarAdmin(admin.ModelAdmin):
    list_display = ("sodrzina", "datum")

    def has_delete_permission(self, request, obj=None):
        if obj and (obj.user.user == request.user or obj.objava.user.user == request.user or request.user.is_superuser):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and (obj.user.user == request.user or obj.objava.user.user == request.user or request.user.is_superuser):
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = Korisnik.objects.get(user=request.user)
        blocked = Blokiran.objects.filter(blokiran=user).values_list('blokiral', flat=True)
        qs = qs.exclude(user__in=blocked)
        return qs


admin.site.register(Komentar, KomentarAdmin)

admin.site.register(Blokiran)

