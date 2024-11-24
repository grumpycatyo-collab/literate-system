class ManufacturingSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ManufacturingSystem, cls).__new__(cls)
            cls._instance.active_orders = []
            cls._instance.completed_orders = []
        return cls._instance

    def add_order(self, order):
        self.active_orders.append(order)

    def remove_order(self, order):
        if order in self.active_orders:
            self.active_orders.remove(order)
        elif order in self.completed_orders:
            self.completed_orders.remove(order)

    def complete_order(self, order):
        if order in self.active_orders:
            self.active_orders.remove(order)
            self.completed_orders.append(order)

    def get_active_orders(self):
        return self.active_orders

    def get_completed_orders(self):
        return self.completed_orders
