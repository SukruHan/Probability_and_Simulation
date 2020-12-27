import numpy as np


class Prisoner:
    def __init__(self):
        self.days = 0
        self.door_probs = [0.1, 0.2, 0.3, 0.1, 0.3]

    def door1(self):
        self.days += 3
        # print("in door 1, days:", self.days)
        return "Cell"

    def door2(self):
        self.days += 1
        # print("in door 2, days:", self.days)
        return "Cell"

    def door3(self):
        # print("in door 3, days:", self.days)
        return "Freedom"

    def door4(self):
        self.days += 2
        # print("in door 4, days:", self.days)
        return "Freedom"

    def door5(self):
        self.days += 3
        # print("in door 5, days:", self.days)
        return self.door2()

    def algorithm(self):
        self.doors = ["door1", "door2", "door3", "door4", "door5"]
        doors = self.doors
        break_condition = True
        general_situtaion = "Cell"
        while (break_condition):
            if (general_situtaion == "Cell"):
                chosen_door = np.random.choice(doors, p=self.door_probs)
                if (chosen_door == "door1"):
                    general_situtaion = self.door1()
                elif (chosen_door == "door2"):
                    general_situtaion = self.door2()
                elif (chosen_door == "door3"):
                    general_situtaion = self.door3()
                elif (chosen_door == "door4"):
                    general_situtaion = self.door4()
                elif (chosen_door == "door5"):
                    self.door5()
            elif (general_situtaion == "Freedom"):
                break_condition = False
                return self.days
            else:
                print("Something is wrong.")


def main():
    N = [20, 50, 100, 500, 1000]  # Number of times to compute
    averages = []
    variances = []
    for n in N:
        all_days = []
        for i in range(n):
            prisoner = Prisoner()
            days = prisoner.algorithm()
            all_days.append(days)
        averages.append(np.mean(all_days))
        variances.append(np.var(all_days))
    for ((avg, var), times) in zip(zip(averages, variances), N):
        print("For {} times: Average is {} and Variance is {}".format(times, avg, var))


if __name__ == "__main__":
    main()