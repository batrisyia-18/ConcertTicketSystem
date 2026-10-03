import streamlit as st

from ticket_module import (
    calculate_ticket_price,
    check_ticket_availability,
    ConcertTicket,
    VIPTicket
)


# Page Configuration
st.set_page_config(
    page_title="Concert Planning & Ticket System",
    page_icon="🎵"
)

st.title("🎵 Concert Planning & Ticket System")
st.write("Plan your concert visit and book your ticket easily.")


# ==========================================
# 1. CUSTOMER INFORMATION
# ==========================================

st.header("1. Customer Information")

customer_name = st.text_input(
    "Customer Name:"
)


# ==========================================
# 2. CONCERT SELECTION
# ==========================================

st.header("2. Concert Selection")

concert_name = st.selectbox(
    "Select Concert:",
    [
        "Midnight Music Festival",
        "Summer Beats Concert",
        "Harmony Live"
    ]
)


# ==========================================
# 3. TICKET SELECTION
# ==========================================

st.header("3. Ticket Selection")

ticket_type = st.radio(
    "Select Ticket Type:",
    ["Standard", "VIP"]
)

quantity_input = st.text_input(
    "Number of Tickets:",
    placeholder="Example: 2"
)


# ==========================================
# 4. CONCERT INFORMATION
# ==========================================

st.header("4. Concert Information")

if concert_name == "Midnight Music Festival":
    standard_price = 80
    vip_price = 150
    available_tickets = 50

elif concert_name == "Summer Beats Concert":
    standard_price = 100
    vip_price = 180
    available_tickets = 40

else:
    standard_price = 70
    vip_price = 130
    available_tickets = 30


st.info(
    f"Standard Ticket: RM{standard_price} | "
    f"VIP Ticket: RM{vip_price} | "
    f"Available Tickets: {available_tickets}"
)


# ==========================================
# 5. TICKET BOOKING
# ==========================================

st.header("5. Ticket Booking")

if st.button("🎫 Book Ticket"):

    try:

        # Check empty customer name
        if customer_name.strip() == "":
            st.error("Customer name cannot be empty.")

        # Check empty ticket quantity
        elif quantity_input.strip() == "":
            st.error("Ticket quantity cannot be empty.")

        else:

            # Convert quantity into integer
            quantity = int(quantity_input)

            # Check invalid quantity
            if quantity <= 0:
                st.error(
                    "Ticket quantity must be more than 0."
                )

            elif quantity > 10:
                st.error(
                    "Maximum 10 tickets are allowed per booking."
                )

            else:

                # Check ticket availability
                is_available, message = check_ticket_availability(
                    available_tickets,
                    quantity
                )

                if not is_available:
                    st.error(message)

                else:

                    # ==========================
                    # STANDARD TICKET
                    # ==========================

                    if ticket_type == "Standard":

                        total_price = calculate_ticket_price(
                            standard_price,
                            quantity
                        )

                        # Create object
                        ticket = ConcertTicket(
                            customer_name,
                            concert_name,
                            ticket_type,
                            quantity,
                            standard_price
                        )

                        st.success(
                            "Ticket booked successfully!"
                        )

                        st.subheader("🎫 Booking Summary")

                        st.write(
                            f"Customer Name: "
                            f"{ticket.customer_name}"
                        )

                        st.write(
                            f"Concert: "
                            f"{ticket.concert_name}"
                        )

                        st.write(
                            f"Ticket Type: "
                            f"{ticket.ticket_type}"
                        )

                        st.write(
                            f"Quantity: "
                            f"{ticket.quantity}"
                        )

                        st.write(
                            f"Price per Ticket: "
                            f"RM{ticket.price:.2f}"
                        )

                        st.write(
                            f"Total Price: "
                            f"RM{total_price:.2f}"
                        )


                    # ==========================
                    # VIP TICKET
                    # ==========================

                    else:

                        vip_fee = 20

                        # Create VIP object
                        ticket = VIPTicket(
                            customer_name,
                            concert_name,
                            ticket_type,
                            quantity,
                            vip_price,
                            vip_fee
                        )

                        # Use overridden method
                        total_price = ticket.calculate_total()

                        st.success(
                            "VIP ticket booked successfully!"
                        )

                        st.subheader("🎫 Booking Summary")

                        st.write(
                            f"Customer Name: "
                            f"{ticket.customer_name}"
                        )

                        st.write(
                            f"Concert: "
                            f"{ticket.concert_name}"
                        )

                        st.write(
                            f"Ticket Type: "
                            f"{ticket.ticket_type}"
                        )

                        st.write(
                            f"Quantity: "
                            f"{ticket.quantity}"
                        )

                        st.write(
                            f"VIP Ticket Price: "
                            f"RM{ticket.price:.2f}"
                        )

                        st.write(
                            f"VIP Fee: "
                            f"RM{ticket.vip_fee:.2f} per ticket"
                        )

                        st.write(
                            f"Total Price: "
                            f"RM{total_price:.2f}"
                        )

                        st.info(
                            ticket.get_vip_benefit()
                        )


    # Error when user enters letters
    except ValueError:
        st.error(
            "Invalid ticket quantity. "
            "Please enter numbers only."
        )

    # Unexpected error
    except Exception as e:
        st.error(
            f"An unexpected error occurred: {e}"
        )