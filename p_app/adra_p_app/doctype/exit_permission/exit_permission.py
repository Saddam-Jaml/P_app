# Copyright (c) 2024, saddam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# /home/js/frappe-bench/apps/p_app/p_app/adra_p_app/doctype/exit_permission/exit_permission.py

class ExitPermission(Document):
    
    


    def before_save(self):
        # Ensure proper validation or numbering (optional)
        self.name = f"EP-{self.from_location}-{self.to_location}-{frappe.utils.nowdate()}"
                      if not self.item_tab:
                                     frappe.msgprint("No items found in the child table!")
                    else:
                        for item in self.item_tab:
                              frappe.msgprint(f"Item: {item.item_name}, Serial: {item.serial_number}")

    def on_submit(self):
        # On submission, if items need to be returned, add to Return Tracker
        if self.needs_return:
            create_return_entry(self)

def create_return_entry(exit_permission):
    # Create a Return Tracker entry
    return_entry = frappe.get_doc({
        "doctype": "Return Tracker",
        "exit_permission": exit_permission.name,
        "from_location": exit_permission.from_location,
        "to_location": exit_permission.to_location,
        "requester": exit_permission.requester,
        "Items": [
            {
                "item_name": item.item_name,
                "serial_number": item.serial_number,
                "qty": item.qty,
                "project": item.project
            } for item in exit_permission.Items
        ]
    })
    return_entry.insert()
    frappe.db.commit()

