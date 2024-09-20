# Copyright (c) 2024, Parwati Bai and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VoterList(Document):
	def validate(self):
		if self.age < 18 :
		    frappe.throw("person is eligible for vote")

