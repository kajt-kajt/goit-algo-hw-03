import sys

###################################################################################
#  Let's describe Towers of Hanoi environment that enforces the rules of the game #

class HanoiTowerDisk:
    """
    Represents a single Hanoi Tower disk
    """
    def __init__(self, size: int):
        self.size = size
        self.has_below = None

    def __str__(self):
        return str(self.size)


class HanoiTowerRod:
    """
    Represents a single Hanoi Tower Rod
    """
    def __init__(self):
        self.disk_on_top = None

    def __str__(self):
        curr_disk = self.disk_on_top
        result = []
        while curr_disk:
            result.append(str(curr_disk))
            curr_disk = curr_disk.has_below
        return "|" + "--".join(result[::-1])

    def push(self, disk: HanoiTowerDisk):
        """
        Adds disk on top of everything
        """
        # if rod is empty, any disk can be added
        if self.disk_on_top is None:
            self.disk_on_top = disk
        else:
            if self.disk_on_top.size < disk.size:
                raise ValueError("ERROR: Cannot add bigger disk on top of smaller one.")
            disk.has_below = self.disk_on_top
            self.disk_on_top = disk

    def pop(self) -> HanoiTowerDisk:
        """
        Removes disk from top
        """
        if self.disk_on_top is None:
            raise ValueError("ERROR: Trying to get disk from empty rod.")
        result = self.disk_on_top
        self.disk_on_top = self.disk_on_top.has_below
        result.has_below = None
        return result


class HanoiTowersSystem:
    """
    Class represents Hanoi Towers environment and enforces restrictions.
    """
    def __init__(self, disks_quantity: int):
        self.__action_counter = 0
        # modeling rods
        self.rods = {}
        self.rods["A"] = HanoiTowerRod()
        self.rods["B"] = HanoiTowerRod()
        self.rods["C"] = HanoiTowerRod()
        # putting disks on rod A
        for i in range(disks_quantity,0,-1):
            self.rods["A"].push(HanoiTowerDisk(i))

    def __str__(self):
        return "\n".join([f"{label}: {rod}" for label, rod in self.rods.items() ])
    
    def move_single_disk(self, src_rod: str, dst_rod: str, size: int):
        """
        Method models moving of single disk between rods taking into account all task restrictions.
        Outputs a log of an action and state of system after it.
        In case of rule violation raises ValueError.
        """
        # in case rod names are wrong, raising an error is fine
        disk = self.rods[src_rod].pop()
        if disk.size != size:
            raise ValueError(f"No disk {size} found on top of rod {src_rod}")
        self.rods[dst_rod].push(disk)
        self.__action_counter += 1
        print(f" [{self.__action_counter}] Move disk {size} from rod {src_rod} to rod {dst_rod}:")
        print(self)
        print()


#######################################################
###### Resursive algorithm to solve the problem #######

def move_disks(system: HanoiTowersSystem,
               disks: list[int],
               from_rod: str,
               to_rod: str):
    """
    Actual recursive algorithm to solve problem
    """
    if len(disks) == 1:
        # recursion base case
        system.move_single_disk(from_rod,to_rod,disks[0])
        return
    # let's split disks list
    buffer_rod = {"A", "B", "C"}.difference({from_rod,to_rod}).pop()
    move_disks(system, disks[1:], from_rod, buffer_rod)
    system.move_single_disk(from_rod,to_rod,disks[0])
    move_disks(system, disks[1:], buffer_rod, to_rod)


def main():
    """
    Entry point
    """
    # Let's get n as command line argument or ask user directly.
    n = None
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            if n < 1:
                n = None
        except ValueError:
            pass
    while n is None:
        try:
            n = int(input("Enter n: "))
            if n < 1:
                n = None
        except ValueError:
            pass

    hanoi_towers = HanoiTowersSystem(n)
    print(hanoi_towers)
    print()
    move_disks(hanoi_towers, list(range(n,0,-1)), "A", "C")


if __name__ == "__main__":
    main()
