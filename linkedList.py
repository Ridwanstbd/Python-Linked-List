class ReservationNode:
    def __init__(self, reservation_id, guest_name, check_in_date):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.next = None

class ReservationLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, reservation_id, guest_name, check_in_date):
        new_node = ReservationNode(reservation_id, guest_name, check_in_date)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, reservation_id):
        current = self.head
        while current is not None:
            if current.reservation_id == reservation_id:
                return current
            current = current.next
        return None

    def delete(self, reservation_id):
        current = self.head
        prev = None
        while current is not None:
            if current.reservation_id == reservation_id:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def update(self, reservation_id, new_guest_name, new_check_in_date):
        node = self.search(reservation_id)
        if node:
            node.guest_name = new_guest_name
            node.check_in_date = new_check_in_date
            return True
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(f"ID: {current.reservation_id}, Guest: {current.guest_name}, Check-in: {current.check_in_date}")
            current = current.next

if __name__ == "__main__":
    reservations = ReservationLinkedList()
    reservations.insert(301, "Widhiya", "2024-10-20")
    reservations.insert(302, "Aprilia", "2024-10-21")
    reservations.insert(303, "Yunita", "2024-04-26")
    reservations.insert(304, "Putri", "2024-04-22")

    print("Data Reservasi:")
    reservations.display()

    print("\nMenghapus reservasi dengan ID 302")
    reservations.delete(302)
    reservations.display()

    print("\nMemperbarui reservasi dengan ID 303 menjadi 'Widhiya' dengan tanggal check-in '2024-10-21'")
    reservations.update(303, "Widhiya", "2024-10-21")
    reservations.display()

    result = reservations.search(301)
    if result:
        print(f"\nReservasi ditemukan: ID {result.reservation_id}, Guest: {result.guest_name}, Check-in: {result.check_in_date}")
    else:
        print("Reservasi tidak ditemukan.")
