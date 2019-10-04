# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "permission"
app_title = "Permission"
app_publisher = "Finbyz Tech Pvt Ltd"
app_description = "custom app for override the default permission"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@finbyz.com"
app_license = "GPL 3.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/permission/css/permission.css"
# app_include_js = "/assets/permission/js/permission.js"

# include js, css files in header of web template
# web_include_css = "/assets/permission/css/permission.css"
# web_include_js = "/assets/permission/js/permission.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "permission.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "permission.install.before_install"
# after_install = "permission.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "permission.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"permission.tasks.all"
# 	],
# 	"daily": [
# 		"permission.tasks.daily"
# 	],
# 	"hourly": [
# 		"permission.tasks.hourly"
# 	],
# 	"weekly": [
# 		"permission.tasks.weekly"
# 	]
# 	"monthly": [
# 		"permission.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "permission.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "permission.event.get_events"
# }
override_whitelisted_methods = {
	"frappe.core.page.permission_manager.permission_manager.get_roles_and_doctypes": "permission.api.get_roles_and_doctypes",
	"frappe.core.page.permission_manager.permission_manager.get_permissions": "permission.api.get_permissions",
	"frappe.core.page.permission_manager.permission_manager.add": "permission.api.add",
	"frappe.core.page.permission_manager.permission_manager.update": "permission.api.update",
	"frappe.core.page.permission_manager.permission_manager.remove": "permission.api.remove",
	"frappe.core.page.permission_manager.permission_manager.reset": "permission.api.reset",
	"frappe.core.page.permission_manager.permission_manager.get_users_with_role": "permission.api.get_users_with_role",
	"frappe.core.page.permission_manager.permission_manager.get_standard_permissions": "permission.api.get_standard_permissions",
	# "erpnext.manufacturing.doctype.work_order.work_order.make_stock_entry": "snehraj.api.make_stock_entry",
}
app_include_css = [
	"/assets/permission/css/permission.min.css"
]