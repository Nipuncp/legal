# Copyright (c) 2024, Nipun and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


import frappe

class Case(Document):
    pass

@frappe.whitelist()
def convert_case_to_lawyer_notice(case_name):
    # Get the Case document
    case_doc = frappe.get_doc("Case", case_name)

    # Create a new Lawyer Notice document and copy fields
    lawyer_notice = frappe.new_doc("Lawyer Notice")
    
    # Copy relevant fields from Case to Lawyer Notice
    fieldnames = [field.fieldname for field in case_doc.meta.fields if field.fieldtype != "Table"]
    for field in fieldnames:
        lawyer_notice.set(field, case_doc.get(field))
    
    # Handle copying the child table "loan_member"
    if case_doc.get("loan_member"):
        lawyer_notice.loan_member = []
        for member in case_doc.loan_member:
            member_row = lawyer_notice.append("loan_member", member.as_dict())
            frappe.logger().debug(f"Appended member row: {member_row}")

    # Debugging: Log the Lawyer Notice document before saving
    frappe.logger().debug(f"Lawyer Notice Document: {lawyer_notice.as_dict()}")

    # Save the Lawyer Notice document
    lawyer_notice.insert()
    frappe.db.commit()

    # Debugging: Log the saved Lawyer Notice name
    frappe.logger().debug(f"Lawyer Notice created with name: {lawyer_notice.name}")

    return lawyer_notice.name

@frappe.whitelist()
def create_arbitration_reference(case_name):
    # Get the Case document
    case_doc = frappe.get_doc("Case", case_name)

    # Create a new Arbitration Reference Letter document
    arbitration_letter = frappe.new_doc("Arbitration Reference Letter or Demand Notice")
    
    # Copy fields from Case to Arbitration Reference Letter
    fieldnames = [field.fieldname for field in case_doc.meta.fields if field.fieldtype != "Table"]
    for field in fieldnames:
        arbitration_letter.set(field, case_doc.get(field))

    # Handle copying child table if necessary
    if case_doc.get("loan_member"):
        arbitration_letter.loan_member = []
        for member in case_doc.loan_member:
            member_row = arbitration_letter.append("loan_member", member.as_dict())

    # Save the new Arbitration Reference Letter
    arbitration_letter.insert()
    frappe.db.commit()

    return arbitration_letter.name