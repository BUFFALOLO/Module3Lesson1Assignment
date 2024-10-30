"""
1. Real-World Python Dictionary Applications
Objective: The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods.

Task 1: Restaurant Menu Update: You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

Problem Statement: Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
- Add a new category called "Beverages" with at least two items.

- Update the price of "Steak" to 17.99.

- Remove "Bruschetta" from "Starters". 
"""

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
print(restaurant_menu)

restaurant_menu["Beverages"]= {"Soda": 1.99, "Craft Beer": 7.59}
print(restaurant_menu)

restaurant_menu["Main Course"]["Steak"]= 17.99
print(restaurant_menu)

del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

"""
2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker: Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
    Open a new service ticket.
    Update the status of an existing ticket.
    Display all tickets or filter by status.
    Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
"""
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue, status="open"):
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": status}
        print(f"{ticket_id} opened for {customer}. | Issue: {issue} | Status: {status} ")

def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

def display_tickets():
    for ticket_id, details in service_tickets.items():
        customer = details["Customer"]
        issue = details["Issue"]
        status = details["Status"]
        print(f"{ticket_id} | Name: {customer}, Issue: {issue}, Status: {status}")  # Corrected print statement

open_ticket("Ticket003", "Lauren", "Forgot username")

display_tickets()

update_ticket_status("Ticket001", "closed")

display_tickets()

open_ticket("Ticket004", "Matt", "Forgot password")

display_tickets()


