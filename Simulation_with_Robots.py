import numpy as np


class Bumblebee1:
    def __init__(self):
        # path = ["up", "down", "straight"]
        self.row = 3
        self.path = [-1, 1, 0]
        self.path_probs = [0.1, 0.1, 0.8]

    def row1(self):
        chosen_path = np.random.choice(self.path, p=self.path_probs)
        self.row += chosen_path

    def row2(self):
        chosen_path = np.random.choice(self.path, p=self.path_probs)
        self.row += chosen_path

    def row3(self):
        chosen_path = np.random.choice(self.path, p=self.path_probs)
        self.row += chosen_path

    def row4(self):
        chosen_path = np.random.choice(self.path, p=self.path_probs)
        self.row += chosen_path

    def row5(self):
        chosen_path = np.random.choice(self.path, p=self.path_probs)
        self.row += chosen_path

    def bumblebee1(self):
        tile_counter = 0
        while (tile_counter <= 200):
            # print(self.row)
            tile_counter += 1
            if (self.row == 1):
                self.row1()
            elif (self.row == 2):
                self.row2()
            elif (self.row == 3):
                self.row3()
            elif (self.row == 4):
                self.row4()
            elif (self.row == 5):
                self.row5()
            else:
                break
        return tile_counter


class Bumblebee2:
    def __init__(self):
        # path = ["up", "down", "straight"]
        self.row = 3

        self.row3_path = [-1, 1, 0]
        self.row3_path_probs = [0.25, 0.25, 0.5]

        self.row1_2_path = [-1, 1, 0]
        self.row1_2_path_probs = [0.1, 0.5, 0.4]

        self.row4_5_path = [-1, 1, 0]
        self.row4_5_path_probs = [0.5, 0.1, 0.4]

    def row1(self):
        chosen_path = np.random.choice(self.row1_2_path, p=self.row1_2_path_probs)
        self.row += chosen_path

    def row2(self):
        chosen_path = np.random.choice(self.row1_2_path, p=self.row1_2_path_probs)
        self.row += chosen_path

    def row3(self):
        chosen_path = np.random.choice(self.row3_path, p=self.row3_path_probs)
        self.row += chosen_path

    def row4(self):
        chosen_path = np.random.choice(self.row4_5_path, p=self.row4_5_path_probs)
        self.row += chosen_path

    def row5(self):
        chosen_path = np.random.choice(self.row4_5_path, p=self.row4_5_path_probs)
        self.row += chosen_path

    def bumblebee2(self):
        tile_counter = 0
        while (tile_counter < 200):
            # print(self.row)
            tile_counter += 1
            if (self.row == 1):
                self.row1()
            elif (self.row == 2):
                self.row2()
            elif (self.row == 3):
                self.row3()
            elif (self.row == 4):
                self.row4()
            elif (self.row == 5):
                self.row5()
            else:
                break
        return tile_counter


class Bumblebee3:
    def __init__(self):
        # path = ["up", "down", "straight"]
        self.row = 3

        self.row3_path = [-1, 1, 0]
        self.row3_path_probs = [0.4, 0.4, 0.2]

        self.row2_4_path = [-1, 1, 0]
        self.row2_4_path_probs = [float(1 / 3), float(1 / 3), float(1 / 3)]

        self.row1_path = [-1, 1, 0]
        self.row1_path_probs = [0.1, 0.6, 0.3]

        self.row5_path = [-1, 1, 0]
        self.row5_path_probs = [0.6, 0.1, 0.3]

    def row1(self):
        chosen_path = np.random.choice(self.row1_path, p=self.row1_path_probs)
        self.row += chosen_path

    def row2(self):
        chosen_path = np.random.choice(self.row2_4_path, p=self.row2_4_path_probs)
        self.row += chosen_path

    def row3(self):
        chosen_path = np.random.choice(self.row3_path, p=self.row3_path_probs)
        self.row += chosen_path

    def row4(self):
        chosen_path = np.random.choice(self.row2_4_path, p=self.row2_4_path_probs)
        self.row += chosen_path

    def row5(self):
        chosen_path = np.random.choice(self.row5_path, p=self.row5_path_probs)
        self.row += chosen_path

    def bumblebee3(self):
        tile_counter = 0
        while (tile_counter < 200):
            # print(self.row)
            tile_counter += 1
            if (self.row == 1):
                self.row1()
            elif (self.row == 2):
                self.row2()
            elif (self.row == 3):
                self.row3()
            elif (self.row == 4):
                self.row4()
            elif (self.row == 5):
                self.row5()
            else:
                break
        return tile_counter


def main():
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(0, 1000000, 1):
        bumblebee1_ = Bumblebee1()
        total1 += bumblebee1_.bumblebee1()

        bumblebee2_ = Bumblebee2()
        total2 += bumblebee2_.bumblebee2()

        bumblebee3_ = Bumblebee3()
        total3 += bumblebee3_.bumblebee3()

    avg1 = total1 / 1000000
    avg2 = total2 / 1000000
    avg3 = total3 / 1000000

    pairs = [(avg1, "Bumblebee1"), (avg2, "Bumblebee2"), (avg3, "Bumblebee3")]
    print(avg1, avg2, avg3)
    print(pairs)
    print("With average {} tiles in one round trip, after 1 million of round trips, robot {} would have the least malfunctions.".format(max(pairs)[0], max(pairs)[1]))


if __name__ == "__main__":
    main()