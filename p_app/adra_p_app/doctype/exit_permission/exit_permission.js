// Copyright (c) 2024, saddam and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Exit Permission", {
// 	refresh(frm) {

// 	},
// });

// /home/js/frappe-bench/apps/p_app/p_app/adra_p_app/public/js/exit_permission.js
frappe.ui.form.on('Exit Permission', {
    refresh(frm) {
        if (frm.doc.needs_return) {
            frm.add_custom_button(__('Create Return Entry'), function() {
                frappe.call({
                    method: "p_app.adra_p_app.doctype.exit_permission.exit_permission.create_return_entry",
                    args: {
                        exit_permission: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint(__('Return Tracker entry created.'));
                        }
                    }
                });
            });
        }
    }
});

