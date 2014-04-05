from django.contrib import admin
from debates.models import Topic,Location,Date,Affirmative_form,Negative_form,SubmittedAffirmativeScore,SubmittedNegativeScore,School,GoogleUser,Student,Team,Debate,Period


admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(SubmittedAffirmativeScore)
admin.site.register(SubmittedNegativeScore)
admin.site.register(School)
admin.site.register(GoogleUser)
admin.site.register(Student)
admin.site.register(Team)
admin.site.register(Debate)
admin.site.register(Period)





try:
	from admin_import.options import add_import
except ImportError:
	pass
else:
		add_import(InviteeAdmin)