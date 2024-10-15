// Copyright (c) 2024, Nipun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Case", {
	refresh(frm) {
        frm.add_custom_button(__('Convert to Lawyer Notice'), function() {
            frappe.call({
                method: "claimspro.claimspro.doctype.case.case.convert_case_to_lawyer_notice",
                args: {
                    case_name: frm.doc.name
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint(__('Lawyer Notice Created: ' + response.message));
                    }
                }
            });
        });

        frm.add_custom_button(__('Create Arbitration Reference Letter'), function() {
            frappe.call({
                method: "claimspro.claimspro.doctype.case.case.create_arbitration_reference",
                args: {
                    case_name: frm.doc.name
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint(__('Arbitration Reference Letter Created: ' + response.message));
                    }
                }
            });
        });

	},
});
