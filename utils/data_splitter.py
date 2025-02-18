from models.organization import Organization
from models.lead import Lead

def split_data_for_entities(main_data):
    """Distributes input data to Organization and Lead based on their fields."""

    # Get allowed fields for each model dynamically
    org_fields = {field.name for field in Organization.__dataclass_fields__.values()}
    lead_fields = {field.name for field in Lead.__dataclass_fields__.values()}

    # Filter relevant fields for each model
    organization_data = {k: v for k, v in main_data.items() if k in org_fields}
    lead_data = {k: v for k, v in main_data.items() if k in lead_fields}

    return organization_data, lead_data
