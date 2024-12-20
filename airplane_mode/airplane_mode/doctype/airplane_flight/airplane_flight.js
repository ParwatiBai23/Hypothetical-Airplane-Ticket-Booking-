// Copyright (c) 2024, Parwati Bai and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Flight", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Flight', {
    refresh: function(frm) {
        calculate_total_crew_members(frm);
    },
    crew_members_add: function(frm) {
        calculate_total_crew_members(frm);
    },
    crew_members_remove: function(frm) {
        calculate_total_crew_members(frm);
    }
});

function calculate_total_crew_members(frm) {
    let total_crew_members = frm.doc.crew_members ? frm.doc.crew_members.length : 0;

    frm.set_value('total_crew_members', total_crew_members);

    // frm.dashboard.set_headline(`Total Crew Members: ${total_crew_members}`);
}
