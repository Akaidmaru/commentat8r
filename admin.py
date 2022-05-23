from django.contrib import admin

class Commentat8rAdminSite(admin.AdminSite):
	title_header = 'c8admin'
	site_header = 'c8admin'
	index_title = 'c8admin'
	logout_template = 'commentat8r/logged_out.html'
