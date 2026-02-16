import frappe
from frappe.utils import now


@frappe.whitelist()
def upsert(**data):

    if not data.get("title") or not data.get("organization"):
        frappe.throw("Title and Organization are required")

    existing = existing = frappe.db.exists("Scraping Site", {"source_url": data.get("source_url")})


    if existing:
        doc = frappe.get_doc("Scraping Site", existing)
    else:
        doc = frappe.new_doc("Scraping Site")

    doc.update({
        "title": data.get("title"),
        "organization": data.get("organization"),
        "funding_amount": data.get("funding_amount"),
        "thematic_area": data.get("thematic_area"),
        "description": data.get("description"),
        "source_url": data.get("source_url"),
        "country": data.get("country"),
        "deadline": data.get("deadline"),
        "last_crawled_on": now(),
    })


    doc.save(ignore_permissions=True)

    return {"status": "success"}
