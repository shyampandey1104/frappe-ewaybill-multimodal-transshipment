# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "ewaybill_transshipment"
app_title = "Frappe Ewaybill Multimodal Transshipment"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Ewaybill Multimodal Transshipment - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/ewaybill_transshipment/css/ewaybill_transshipment.bundle.css"
app_include_js = "/assets/ewaybill_transshipment/js/ewaybill_transshipment.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Ewaybill Multimodal Transshipment Entry": {
        "validate": "ewaybill_transshipment.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "ewaybill_transshipment.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "ewaybill_transshipment.tasks.hourly_sync"
    ],
    "daily": [
        "ewaybill_transshipment.tasks.daily_reconciliation"
    ],
    "weekly": [
        "ewaybill_transshipment.tasks.weekly_digest"
    ]
}
