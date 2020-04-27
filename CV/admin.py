from django.contrib import admin

# Register your models here.
from CV.models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('name', 'profession', 'obtained_ranks',
                    'max_ranks', 'user_id', 'email', 'phone', 'date_created')
    list_filter = ('name', 'profession', 'obtained_ranks',
                   'max_ranks', 'user_id', 'email', 'phone')
    list_per_page = 50
    date_hierarchy = ('date_created')

    # def get_ordering(self, request):
    #     if request.user.is_super():
    #         return ('-date_created')
    #     else:
    #         return None

    class Meta:
        fields = '__all__'


admin.site.register(Profile, ProfileAdmin)
