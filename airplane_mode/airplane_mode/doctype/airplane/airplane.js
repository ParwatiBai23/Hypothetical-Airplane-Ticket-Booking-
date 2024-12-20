// Copyright (c) 2024, Parwati Bai and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airplane', {
    refresh: function(frm) {
        if (!frappe.user.has_role('Airport Authority Personnel')) {
            frm.set_df_property('initial_audit_completed', 'hidden', true);
            frm.set_df_property('initial_audit_completed', 'read_only', true);
        } else {
            frm.set_df_property('initial_audit_completed', 'hidden', false);
            frm.set_df_property('initial_audit_completed', 'read_only', false);
        }
    }
});
