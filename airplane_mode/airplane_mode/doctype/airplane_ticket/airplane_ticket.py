# Copyright (c) 2024, Parwati Bai and contributors
# For license information, please see license.txt
import random
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

    def validate(self):
        self.calculate_total_amount()
        
        self.ensure_unique_add_ons()
        

        self.check_airplane_capacity()

    def before_submit(self):
        if not self.ticket_status:
            frappe.throw("Please set the status of the ticket before submission.")
        if self.ticket_status != "Boarded":
            frappe.throw("Only tickets with status 'Boarded' can be submitted.")

    def before_insert(self):
        self.assign_random_seat()

    def calculate_total_amount(self):
        """Calculate total amount based on flight price and add-ons."""
        self.total_amount = (self.flight_price or 0) + sum(addon.amount or 0 for addon in self.add_ons)

    def ensure_unique_add_ons(self):
        """Ensure that each add-on type is unique."""
        add_on_types = [addon.add_on_type for addon in self.add_ons if addon.add_on_type]
        if len(add_on_types) != len(set(add_on_types)):
            frappe.throw("Each add-on type must be unique.")
    
    def check_airplane_capacity(self):
        """Check if the number of tickets exceeds the airplane's capacity."""
        if not self.airplane:
            frappe.throw("Airplane is not specified for this ticket.")

        airplane = frappe.get_doc('Airplane', self.airplane)
        airplane_capacity = airplane.capacity

        current_tickets = frappe.db.count('Airplane Ticket', {
            'flight': self.flight,
            'ticket_status': 'Booked'
        })

        if current_tickets >= airplane_capacity:
            frappe.throw(f"The airplane for this flight has a capacity of {airplane_capacity} seats, and all seats are already booked.")

    def assign_random_seat(self):
        """Assign a random seat to the ticket before insert."""
        random_number = random.randint(1, 99)
        random_letter = random.choice('ABCDE')
        self.seat = f"{random_number}{random_letter}"

