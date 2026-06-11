"""
utils/display.py
Pretty-print helpers using the 'rich' library.
Renders guests, rooms, and reservations as formatted tables.
"""

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def print_success(message: str) -> None:
    """Print a success message in green."""
    console.print(f"[bold green]✔ {message}[/bold green]")


def print_error(message: str) -> None:
    """Print an error message in red."""
    console.print(f"[bold red]✘ {message}[/bold red]")


def print_info(message: str) -> None:
    """Print an informational message in cyan."""
    console.print(f"[cyan]{message}[/cyan]")


def display_guests(guests: list) -> None:
    """Render a rich table of all registered guests."""
    if not guests:
        print_info("No guests registered yet.")
        return
    table = Table(title="Registered Guests", box=box.ROUNDED)
    table.add_column("ID", style="dim", width=4)
    table.add_column("Name", style="bold")
    table.add_column("Email")
    table.add_column("Phone")
    for guest in guests:
        table.add_row(
            str(guest.guest_id),
            guest.name,
            guest.email,
            guest.phone or "-",
        )
    console.print(table)


def display_rooms(rooms: list) -> None:
    """Render a rich table of all rooms."""
    if not rooms:
        print_info("No rooms added yet.")
        return
    table = Table(title="Hotel Rooms", box=box.ROUNDED)
    table.add_column("Room No.", style="dim", width=6)
    table.add_column("Type", style="bold")
    table.add_column("Price/Night", justify="right")
    table.add_column("Status")
    for room in rooms:
        status_color = "green" if room.available else "red"
        status_label = "Available" if room.available else "Occupied"
        table.add_row(
            str(room.number),
            room.room_type.capitalize(),
            f"KES {room.price_per_night:,.0f}",
            f"[{status_color}]{status_label}[/{status_color}]",
        )
    console.print(table)


def display_reservations(reservations: list) -> None:
    """Render a rich table of all reservations."""
    if not reservations:
        print_info("No reservations found.")
        return
    table = Table(title="Reservations", box=box.ROUNDED)
    table.add_column("ID", style="dim", width=4)
    table.add_column("Guest", style="bold")
    table.add_column("Room", justify="center")
    table.add_column("Check-In")
    table.add_column("Check-Out")
    table.add_column("Nights", justify="right")
    table.add_column("Total Cost", justify="right")
    table.add_column("Status")
    status_colors = {
        "confirmed": "green",
        "cancelled": "red",
        "checked-out": "yellow",
    }
    for res in reservations:
        color = status_colors.get(res.status, "white")
        table.add_row(
            str(res.reservation_id),
            res.guest.name,
            str(res.room.number),
            res.check_in,
            res.check_out,
            str(res.nights()),
            f"KES {res.total_cost():,.0f}",
            f"[{color}]{res.status}[/{color}]",
        )
    console.print(table)


def display_overdue(reservations: list) -> None:
    """Render a rich table of overdue reservations."""
    from datetime import date, datetime
    overdue = [r for r in reservations if r.is_overdue()]
    if not overdue:
        print_info("No overdue reservations.")
        return
    table = Table(title="⚠ Overdue Checkouts", box=box.ROUNDED)
    table.add_column("ID", style="dim", width=4)
    table.add_column("Guest", style="bold")
    table.add_column("Room", justify="center")
    table.add_column("Due Date")
    table.add_column("Days Overdue", justify="right")
    for res in overdue:
        checkout = datetime.strptime(res.check_out, "%Y-%m-%d").date()
        days_late = (date.today() - checkout).days
        table.add_row(
            str(res.reservation_id),
            res.guest.name,
            str(res.room.number),
            res.check_out,
            f"[bold red]{days_late} days[/bold red]",
        )
    console.print(table)