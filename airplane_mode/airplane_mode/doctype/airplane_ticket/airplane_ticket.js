// Copyright (c) 2024, Parwati Bai and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    flight_price: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    add_ons_add: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    add_ons_remove: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    calculate_total_amount: function(frm) {
        let flight_price = frm.doc.flight_price || 0;
        let total_addons_amount = 0;

        frm.doc.add_ons.forEach(add_on => {
            total_addons_amount += add_on.amount || 0;
        });

        // Set the total amount
        frm.set_value('total_amount', flight_price + total_addons_amount);
    }
});
