"""
V1.0
"""
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

#______________________________________________________________________________
#An implementation of the Water jug problem
# Tuple format = [<Node (7-liter, 4-liter, 3-liter)>]
#Possible actions are as follows:
# Pour the contents of the 7 liter jug into the 4 or 3 liter jug
# Pour the contents of the 4 liter jug into the 7 or 3 liter jug
# Pour the contents of the 3 liter jug into the 7 or 4 liter jug
class WJP(Problem):
    #state is a tuple(SL,FL,TL) with initial value (7,0,0)
    SL=0; FL=1; TL=2 #class "constants"
    
    def __init__(self, goal):
        self.initial = (7,0,0)
        self.goalState = goal
    
    def actions(self, state):
        #actions are simply the result states possible in this example
        list=[]
        #7L4L pour the contents of the seven liter jug into the four liter jug
        amountToPour = min(state[WJP.SL], 4 - state[WJP.FL]);
        newState = (state[WJP.SL] - amountToPour,state[WJP.FL] + amountToPour ,state[WJP.TL])
        if self.validate(newState):
            list.append(newState)
                
        #7L3L - pour the contents of the seven liter jug into the three liter jug
        amountToPour = min(state[WJP.SL], 3 - state[WJP.TL]);
        newState = (state[WJP.SL]- amountToPour,state[WJP.FL],state[WJP.TL]+amountToPour)
        if self.validate(newState):
            list.append(newState)   
                
        #4L3L - pour the contents of the four liter jug into the three liter jug
        amountToPour = min(state[WJP.FL], 3 - state[WJP.TL]);
        newState = (state[WJP.SL],state[WJP.FL]- amountToPour,state[WJP.TL]+ amountToPour)
        if self.validate(newState):
            list.append(newState)

        #4L7L - pour the contents of the four liter jug into the seven liter jug
        amountToPour = min(state[WJP.FL], 7 - state[WJP.SL]);
        newState = (state[WJP.SL]+ amountToPour,state[WJP.FL]- amountToPour,state[WJP.TL])
        if self.validate(newState):
            list.append(newState)
                
        #3L4L - pour the contents of the three liter jug into the four liter jug
        amountToPour = min(state[WJP.TL], 4 - state[WJP.FL]);
        newState = (state[WJP.SL],state[WJP.FL] + amountToPour,state[WJP.TL] - amountToPour)
        if self.validate(newState):
            list.append(newState)     
                
        #3L7L - pour the contents of the three liter jug into the seven liter jug
        amountToPour = min(state[WJP.TL], 7 - state[WJP.SL]);
        newState = (state[WJP.SL] + amountToPour,state[WJP.FL],state[WJP.TL] - amountToPour)
        if self.validate(newState):
            list.append(newState)   
                
                
        return list

    def validate(self, state):
        #verify no number is negative
        if state[WJP.SL] < 0 or state[WJP.FL] < 0 or state[WJP.TL] < 0:
            return False
        #verify no number is greater than the max
        if state[WJP.SL] > 7 or state[WJP.FL] > 4 or state[WJP.TL] > 3:
            return False
        return True  
        
    def result(self, state, action):
        return action #since states are so lightweight, the action is itself the new state

    def goal_test(self, state):
        return state == self.goalState


def main():
    #Runs the Water Jug problem, will provide a solution to fill the three jugs
    # to a 2,2,3 configuration without overfilling a jug and only by pouring
    # until the pouring jug is empty or the recieving jug is full
    print('Water Jug Problem: ')
    print(' Tuples are in this format --> [<Node (Seven-liter, Four-liter,  Three-liter)>]')
    goalState = (2,2,3)

    problem = WJP(goalState)
    goal = breadth_first_search(problem)
    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    #print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()

main()