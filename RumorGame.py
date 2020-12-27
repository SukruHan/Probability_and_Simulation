import numpy as np 
import random
import string

def question_A_B_C(px = 0.15):
    N = 20 # number of people in group
    #px = 0.15 # probability of rumor transmitted
    t = 200 # number of times to run the system
    NoP = 2 # number of people selected each time
    people_names = list(string.ascii_lowercase)
    time_counter_list = []
    prob_question_b_counter = 0
    prob_question_c_counter = 0
    for i in range(1, t):
        k = 1 # number of people knows the rumor
        people = {}
        random_person_knows_rumor = random.randrange(20)
        for j in range(N):
            if j == random_person_knows_rumor:
                people[people_names[j]] = 1
            else:
                people[people_names[j]] = 0
        assert len(people) == N
        break_condition = True
        time_counter = 1
        while(break_condition):
            if(k==20):
                break_condition = False
            else:
                random_selected_people = list(random.sample(list(people), NoP))
                if((time_counter==100) and (k>=15)):
                    prob_question_b_counter += 1
                if((time_counter==10) and (k<=2)):
                    prob_question_c_counter += 1
                if((people[random_selected_people[0]] == 0) and (people[random_selected_people[1]] == 1)):
                    rand_prob = random.random()
                    if(rand_prob <= px):
                        people[random_selected_people[0]] = 1
                        k += 1
                    else:
                        pass
                elif((people[random_selected_people[0]] == 1) and (people[random_selected_people[1]] == 0)):
                    rand_prob = random.random()
                    if(rand_prob <= px):
                        people[random_selected_people[1]] = 1
                        k += 1
                    else:
                        pass
                else:
                    pass
                time_counter += 1
        time_counter_list.append(time_counter)
    print("### QUESTION A ###")
    print("\nAverage time that it takes for everyone to hear the humor: ", np.mean(time_counter_list), "\n")
    print("### QUESTION B ###")
    print("\nProbability that at least 15 people know the humor at time t=100: ", prob_question_b_counter/t, "\n")
    print("### QUESTION C ###")
    print("\nProbability that at most 2 people know the humor at time t=10: ", prob_question_c_counter/t, "\n")

def question_D(px = 0.20):
    print("\n##################")
    print("### QUESTION D ###")
    print("\nWhen transmission probability increases to 0.20, results are as follow;\n")
    question_A_B_C(px)
    print("Results intuitively expected. Because average time that it takes for everyone to hear the humor is less. Probability that at least 15 people know the humor at time t=100 has increased because transmission probability is increased. Interesting part is 'c'.  Probability that at most 2 people know the humor at time t=10 decreases since the constraint is 'at most 2 people' is binding. More than 2 people know the humuor at time t=10. Therfore probability has decreased.")
    print("##################\n")

def question_E(px = 0.99):
    print("\n##################")
    print("### QUESTION E ###")
    print("\nWhen transmission probability increases to 0.99, results are as follow;\n")
    question_A_B_C(px)
    print("Results intuitively expected. Because average time that it takes for everyone to hear the humor is less. Probability that at least 15 people know the humor at time t=100 has increased because transmission probability is increased. Interesting part is 'c'.  Probability that at most 2 people know the humor at time t=10 decreases since the constraint is 'at most 2 people' is binding. More than 2 people know the humuor at time t=10. Therfore probability has decreased.")
    print("##################\n")

if __name__ == "__main__":
    question_A_B_C()
    question_D()
    question_E()