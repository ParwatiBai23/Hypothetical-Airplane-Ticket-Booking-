# Copyright (c) 2024, Parwati Bai and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        # Set the status to "Completed" when the document is submitted
        self.status = "Completed"
        self.save()

