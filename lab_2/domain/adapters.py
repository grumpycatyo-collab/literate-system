class ExternalOrderSystem:
    def create_external_order(self, items, customer_id):
        return {
            "order_items": items,
            "customer": customer_id,
            "status": "pending"
        }

class OrderAdapter:
    def __init__(self, external_system: ExternalOrderSystem):
        self.external_system = external_system

    def convert_to_internal_order(self, external_order):
        return {
            "items": external_order["order_items"],
            "customer_id": external_order["customer"],
            "status": "active"
        }