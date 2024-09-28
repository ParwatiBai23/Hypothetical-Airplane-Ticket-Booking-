# Copyright (c) 2024, Parwati Bai and contributors
# For license information, please see license.txt
import random
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    
    def validate(self):
        self.total_amount = (self.flight_price or 0) + sum(addon.amount or 0 for addon in self.add_ons)
        
        add_on_items = [addon.item for addon in self.add_ons]  
        if len(add_on_items) != len(set(add_on_items)):
            frappe.throw("Each add-on type must be unique.")
    
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Ticket can only be submitted if status is 'Boarded'.")
    
    def before_insert(self):
        random_number = random.randint(1, 99)
        random_letter = random.choice('ABCDE')
        self.seat = f"{random_number}{random_letter}"
