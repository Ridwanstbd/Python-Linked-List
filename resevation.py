class ReservationNode:
    def __init__(self, reservation_id, guest_name, check_in_date):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.next = None

class ReservationLinkedList:
    def __init__(self):
        self.head = None

    def push(self, reservation_id, guest_name, check_in_date):
        new_node = ReservationNode(reservation_id, guest_name, check_in_date)

        new_node.next = self.head
        self.head = new_node

    def display(self):
        current_node = self.head

        while current_node:
            print(f'ID: {current_node.reservation_id}, Guest: {current_node.guest_name} , Check-in: {current_node.check_in_date}')
            current_node = current_node.next
    
    def delete(self,key):
        current_node = self.head
        prev_node = None

        if current_node is not None and current_node.reservation_id == key:
            self.head = current_node.next
            current_node = None
            return 

        while current_node is not None and current_node.reservation_id != key:
            prev_node = current_node
            current_node = current_node.next 

        if current_node is None:
            print(f"Node dengan data '{key}' tidak ditemukan.")
            return

        prev_node.next = current_node.next
        current_node = None    

sll = ReservationLinkedList()
sll.push(301, "Widhiya", "2024-10-20")
sll.push(302, "Aprilia", "2024-10-21")
sll.push(303, "Yunita", "2024-04-26")
sll.push(304, "Putri", "2024-04-22")

print("Data Reservasi:")
sll.display()
        
print("Menghapus Data: 302")
sll.delete(302)

print("Hasil data Setelah Hapus:")
sll.display()