TICKET_PRICES = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}

def get_ticket_price(destination_city):
    """Returns ticket price for a given city."""
    print(f"Fetching ticket price for {destination_city}")
    return TICKET_PRICES.get(destination_city.lower(), "Unknown")