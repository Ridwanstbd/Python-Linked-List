class ReservationNode:
    def __init__(self, reservation_id, guest_name, check_in_date):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.left = None
        self.right = None

class ReservationTree:
    def __init__(self):
        self.root = None

    def insert(self, reservation_id, guest_name, check_in_date):
        if self.root is None:
            self.root = ReservationNode(reservation_id, guest_name, check_in_date)
        else:
            self._insert_recursive(self.root, reservation_id, guest_name, check_in_date)

    def _insert_recursive(self, current_node, reservation_id, guest_name, check_in_date):
        if reservation_id < current_node.reservation_id:
            if current_node.left is None:
                current_node.left = ReservationNode(reservation_id, guest_name, check_in_date)
            else:
                self._insert_recursive(current_node.left, reservation_id, guest_name, check_in_date)
        elif reservation_id > current_node.reservation_id:
            if current_node.right is None:
                current_node.right = ReservationNode(reservation_id, guest_name, check_in_date)
            else:
                self._insert_recursive(current_node.right, reservation_id, guest_name, check_in_date)

    def search(self, reservation_id):
        return self._search_recursive(self.root, reservation_id)
        
    def _search_recursive(self, current_node, reservation_id):
        if current_node is None:
            return None
        if current_node.reservation_id == reservation_id:
            return current_node
        elif reservation_id < current_node.reservation_id:
            return self._search_recursive(current_node.left, reservation_id)
        else:
            return self._search_recursive(current_node.right, reservation_id)
            
    def delete(self, reservation_id):
        self.root = self._delete_recursive(self.root, reservation_id)

    def _delete_recursive(self, node, reservation_id):
        if node is None:
            return node
        if reservation_id < node.reservation_id:
            node.left = self._delete_recursive(node.left, reservation_id)
        elif reservation_id > node.reservation_id:
            node.right = self._delete_recursive(node.right, reservation_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.reservation_id, node.guest_name, node.check_in_date = temp.reservation_id, temp.guest_name, temp.check_in_date
            node.right = self._delete_recursive(node.right, temp.reservation_id)
        return node
        
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        
    def update(self, reservation_id, new_guest_name, new_check_in_date):
        node = self.search(reservation_id)
        if node:
            node.guest_name = new_guest_name
            node.check_in_date = new_check_in_date
            return True
        return False
        
    def display(self, node, level=0):
        if node is not None:
            self.display(node.right, level + 1)
            print("  " * level + f"ID: {node.reservation_id}, Guest: {node.guest_name}, Check-in: {node.check_in_date}")
            self.display(node.left, level + 1)

if __name__ == "__main__":
    rt = ReservationTree()
    rt.insert(301, "Widhiya", "2024-10-20")
    rt.insert(302, "Aprilia", "2024-10-21")
    rt.insert(303, "Yunita", "2024-04-26")
    rt.insert(304, "Putri", "2024-04-22")

    print("Data Reservasi:")
    rt.display(rt.root)

    print("\nMenghapus reservasi dengan ID 302")
    rt.delete(302)
    rt.display(rt.root)

    print("\nMemperbarui reservasi dengan ID 303 menjadi 'Widhiya' dengan tanggal check-in '2024-10-21'")
    rt.update(303, "Widhiya", "2024-10-21")

    result = rt.search(301)
    if result:
        print(f"\nReservasi ditemukan: ID {result.reservation_id}, Guest: {result.guest_name}, Check-in: {result.check_in_date}")
    else:
        print("Reservasi tidak ditemukan.")
