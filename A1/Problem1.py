"""
V1.0
"""
from search import Problem, breadth_first_search, depth_first_search, iterative_deepening_search


# ______________________________________________________________________________
# An implementation of the Family raft problem
# Tuple format = [<Node (mom, dad, leftFemaleKid, leftMaleKid,rightFemaleKid, rightMaleKid,police, thief, boatSide)>]
# Possible actions are as follows, move police and either the thief, mom,dad, or one male child or one female child to the other side
# move mom and dad to the other side
# move mom and female child to the other side
# move dad and male child to the other side
class FRP(Problem):
    # state is a tuple(LM,RM,LC,RC,B) with initial value (0,0,2,2,0,0,0,0,0)
    # mom, dad, police and thief value flips between 1(R) and 0(L)
    M = 0;
    D = 1;
    LFK = 2;
    LMK = 3;
    RFK = 4;
    RMK = 5;
    PO = 6;
    TH = 7;
    B = 8  # class "constants"

    def __init__(self, goal):
        self.initial = (0, 0, 2, 2, 0, 0, 0, 0, 0)
        self.goalState = goal

    def actions(self, state):
        # actions are simply the result states possible in this example
        list = []
        if state[FRP.B] == 1:  # boat on the right side
            # 1PO1M - Move cop and mom left
            newState = (state[FRP.M] - 1, state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] - 1, state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1PO1D - move cop and dad left
            newState = (state[FRP.M], state[FRP.D] - 1, state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] - 1, state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

                # 1PO1TH move cop and thief left
            newState = (state[FRP.M], state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] - 1, state[FRP.TH] - 1, state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1PO1FK - move cop and femaleKid left
            newState = (
            state[FRP.M], state[FRP.D], state[FRP.LFK] + 1, state[FRP.LMK], state[FRP.RFK] - 1, state[FRP.RMK],
            state[FRP.PO] - 1, state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

                # 1PO1MK -  move cop and maleKid left
            newState = (
            state[FRP.M], state[FRP.D], state[FRP.LFK], state[FRP.LMK] + 1, state[FRP.RFK], state[FRP.RMK] - 1,
            state[FRP.PO] - 1, state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1PO1MK -  move cop left
            newState = (state[FRP.M], state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] - 1, state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move mom and femaleKid left
            newState = (
            state[FRP.M] - 1, state[FRP.D], state[FRP.LFK] + 1, state[FRP.LMK], state[FRP.RFK] - 1, state[FRP.RMK],
            state[FRP.PO], state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1D -  move mom and dad left
            newState = (
            state[FRP.M] - 1, state[FRP.D] - 1, state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
            state[FRP.PO], state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move mom left
            newState = (state[FRP.M] - 1, state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO], state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move dad and maleKid left
            newState = (
            state[FRP.M], state[FRP.D] - 1, state[FRP.LFK], state[FRP.LMK] + 1, state[FRP.RFK], state[FRP.RMK] - 1,
            state[FRP.PO], state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move dad left
            newState = (state[FRP.M], state[FRP.D] - 1, state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO], state[FRP.TH], state[FRP.B] - 1)
            if self.validate(newState):
                list.append(newState)

        else:  # boat on the left side
            # 1PO1M - Move cop and mom right
            newState = (state[FRP.M] + 1, state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] + 1, state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1PO1D - move cop and dad right
            newState = (state[FRP.M], state[FRP.D] + 1, state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] + 1, state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

                # 1PO1TH move cop and thief right
            newState = (state[FRP.M], state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] + 1, state[FRP.TH] + 1, state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1PO1FK - move cop and femaleKid right
            newState = (
            state[FRP.M], state[FRP.D], state[FRP.LFK] - 1, state[FRP.LMK], state[FRP.RFK] + 1, state[FRP.RMK],
            state[FRP.PO] + 1, state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

                # 1PO1MK -  move cop and maleKid right
            newState = (
            state[FRP.M], state[FRP.D], state[FRP.LFK], state[FRP.LMK] - 1, state[FRP.RFK], state[FRP.RMK] + 1,
            state[FRP.PO] + 1, state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1PO1MK -  move cop right
            newState = (state[FRP.M], state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO] + 1, state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move mom and femaleKid right
            newState = (
            state[FRP.M] + 1, state[FRP.D], state[FRP.LFK] - 1, state[FRP.LMK], state[FRP.RFK] + 1, state[FRP.RMK],
            state[FRP.PO], state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1D -  move mom and dad right
            newState = (
            state[FRP.M] + 1, state[FRP.D] + 1, state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
            state[FRP.PO], state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move mom right
            newState = (state[FRP.M] + 1, state[FRP.D], state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO], state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move dad and maleKid right
            newState = (
            state[FRP.M], state[FRP.D] + 1, state[FRP.LFK], state[FRP.LMK] - 1, state[FRP.RFK], state[FRP.RMK] + 1,
            state[FRP.PO], state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

            # 1M1RFK -  move dad right
            newState = (state[FRP.M], state[FRP.D] + 1, state[FRP.LFK], state[FRP.LMK], state[FRP.RFK], state[FRP.RMK],
                        state[FRP.PO], state[FRP.TH], state[FRP.B] + 1)
            if self.validate(newState):
                list.append(newState)

        return list

    def validate(self, state):
        # verify no number is negative
        if state[FRP.M] < 0 or state[FRP.D] < 0 or state[FRP.LFK] < 0 or state[FRP.LMK] < 0 or state[FRP.RFK] < 0 or \
                state[FRP.RMK] < 0 or state[FRP.PO] < 0 or state[FRP.TH] < 0 or state[FRP.B] < 0:
            return False
        # verify no number is greater than the max
        if state[FRP.M] > 1 or state[FRP.D] > 1 or state[FRP.LFK] > 2 or state[FRP.LMK] > 2 or state[FRP.RFK] > 2 or \
                state[FRP.RMK] > 2 or state[FRP.PO] > 1 or state[FRP.TH] > 1 or state[FRP.B] > 1:
            return False
        # verify if boat is on right, then there must be someone on the right side
        if state[FRP.B] == 1 and (state[FRP.D] + state[FRP.M] + state[FRP.PO]) == 0:
            return False
        # verify if boat is on left, then there must be someone on the left side
        if state[FRP.B] == 0 and (state[FRP.D] + state[FRP.M] + state[FRP.PO]) == 3:
            return False
        # verify mom is not with boy kids on left, unless with dad as well
        if state[FRP.M] == 0 and (state[FRP.LMK] > 0 and state[FRP.D] == 1):
            return False
        # verify mom is not with boy kids on right, unless with dad as well
        if state[FRP.M] == 1 and (state[FRP.RMK] > 0 and state[FRP.D] == 0):
            return False
        # verify dad is not with girl kids on left, unless with mom as well
        if state[FRP.D] == 0 and (state[FRP.LFK] > 0 and state[FRP.M] == 1):
            return False
        # verify dad is not with girl kids on right, unless with mom as well
        if state[FRP.D] == 1 and (state[FRP.RFK] > 0 and state[FRP.M] == 0):
            return False
        # verify thief is not with family on left side, unless with police
        if state[FRP.TH] == 0 and (
                (state[FRP.LFK] > 0 or state[FRP.LMK] > 0 or state[FRP.M] == 0 or state[FRP.D] == 0) and state[
            FRP.PO] == 1):
            return False
        # verify thief is not with family on right side, unless with police
        if state[FRP.TH] == 1 and (
                (state[FRP.RFK] > 0 or state[FRP.RMK] > 0 or state[FRP.M] == 1 or state[FRP.D] == 1) and state[
            FRP.PO] == 0):
            return False
        return True

    def result(self, state, action):
        return action  # since states are so lightweight, the action is itself the new state

    def goal_test(self, state):
        return state == self.goalState


def main():
    # Runs the Family police thief problem, will provide a path to move all family members to the right side without
    # leaving the mom alone with the male children, the dad alone with the female children, and the thief with any of
    # the family members without the police officer
    print('Family Cop Thief Problem: ')
    print(
        ' Tuples are in this format --> [<Node (mom, dad, leftFemaleKid, leftMaleKid,rightFemaleKid, rightMaleKid,police, thief, boatSide)>]')
    goalState = (1, 1, 0, 0, 2, 2, 1, 1, 1)

    problem = FRP(goalState)
    goal = breadth_first_search(problem)
    # print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()


main()
