# Copyright (c) 2024, Parwati Bai and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class AirplaneTicketAddonType(Document):
# 	pass

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        # Calculate Total Amount
        self.calculate_total_amount()
        # Ensure unique add-ons
        self.remove_duplicate_add_ons()

    def calculate_total_amount(self):
        # Start with the flight price
        total = self.flight_price or 0
        
        # Add the sum of all add-on amounts
        if self.add_ons:
            total += sum([addon.amount for addon in self.add_ons])
        
        # Set the total amount
        self.total_amount = total

    def remove_duplicate_add_ons(self):
        # Using a set to track unique add-ons
        unique_items = set()
        to_remove = []
        
        # Iterate over add-ons to find duplicates
        for addon in self.add_ons:
            if addon.item in unique_items:
                # Mark duplicate for removal
                to_remove.append(addon)
            else:
                unique_items.add(addon.item)
        
        # Remove duplicates
        for addon in to_remove:
            self.remove(addon)

