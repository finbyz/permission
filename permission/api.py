from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist()
def docperm():
	doc = frappe.new_doc("DocPerm")
	doc.read = 1
	doc.write = 1
	doc.create = 1
	doc.delete = 1
	doc.idx = 2
	doc.parent = "Custom DocPerm" #"Role"
	doc.role = "Local Admin"
	doc.parentfield = 'permissions'
	doc.parenttype = "DocType"
	
	doc1 = frappe.new_doc("DocPerm")
	doc1.read = 1
	doc1.write = 1
	doc1.create = 1
	doc1.delete = 1
	doc1.idx = 2
	doc1.parent = "Role"
	doc1.role = "Local Admin"
	doc1.parentfield = 'permissions'
	doc1.parenttype = "DocType"
	
	doc.db_insert()
	doc1.db_insert()
