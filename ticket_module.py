# Function 1: Calculate total ticket price
def calculate_ticket_price(price, quantity):
    total_price = price * quantity
    return total_price

# Function 2: Check ticket availability
def check_ticket_availability(available_tickets, quantity):
    if quantity <= available_tickets:
        return True, "Ticket is available."
    else:
        return False, "Not enough tickets available."

# Parent Class
class ConcertTicket:

    def __init__(self, customer_name, concert_name, ticket_type, quantity, price):
        self.customer_name = customer_name
        self.concert_name = concert_name
        self.ticket_type = ticket_type
        self.quantity = quantity
        self.price = price

    # Method 1: Calculate total price
    def calculate_total(self):
        return self.price * self.quantity

    # Method 2: Generate ticket summary
    def generate_summary(self):
        return (
            f"Customer Name: {self.customer_name}\n"
            f"Concert: {self.concert_name}\n"
            f"Ticket Type: {self.ticket_type}\n"
            f"Quantity: {self.quantity}\n"
            f"Total Price: RM{self.calculate_total():.2f}"
        )
    
# Subclass
class VIPTicket(ConcertTicket):

    def __init__(self, customer_name, concert_name, ticket_type,
                 quantity, price, vip_fee):

        # Inherit attributes from parent class
        super().__init__(
            customer_name,
            concert_name,
            ticket_type,
            quantity,
            price
        )

        # New attribute for VIP ticket
        self.vip_fee = vip_fee

    # Override parent method
    def calculate_total(self):
        normal_total = super().calculate_total()
        vip_total = normal_total + (self.vip_fee * self.quantity)
        return vip_total

    # New method for VIP benefit
    def get_vip_benefit(self):
        return "VIP Benefit: Priority entry and exclusive merchandise."