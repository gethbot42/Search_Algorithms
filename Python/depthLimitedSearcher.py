from display import Displayable, visualize
from searchProblem import Path

class DepthLimitedSearcher(Displayable):
    """depth limited searcher
    """
    def __init__(self, depth_limit, problem):
        """creates a searcher from a problem
        """
        self.problem = problem
        self.initialize_frontier()
        self.num_expanded = 0
        self.add_to_frontier(Path(problem.start_node()))
        self.depth_limit = depth_limit
        self.hit_depth_bound = False
        super().__init__()

    def initialize_frontier(self):
        self.frontier = []
        
    def empty_frontier(self):
        return self.frontier == []
        
    def add_to_frontier(self,path):
        self.frontier.append(path)
        
    @visualize
    def search(self):
        """returns (next) path from the problem's start node
        to a goal node. 
        Returns None if no path exists.
        """
        while not self.empty_frontier():
            path = self.frontier.pop()
            self.display(2, "Expanding:",path,"(cost:",path.cost,")")
            self.num_expanded += 1
            if self.problem.is_goal(path.end()):    # solution found
                self.display(1, self.num_expanded, "paths have been expanded and",
                            len(self.frontier), "paths remain in the frontier")
                self.solution = path   # store the solution found
                return path                
            else:
                neighs = self.problem.neighbors(path.end())
                if (len(list(path.nodes())) - 1) >= self.depth_limit: #we have hit the depth_limit
                  if len(neighs) != 0: #no neighbors with this path
                    hit_depth_bound = True
                  #self.display(1, "No solutions at depth", 
                    #self.depth_limit)
                else:
                  self.display(3,"Neighbors are", neighs)
                  for arc in reversed(neighs):
                      self.add_to_frontier(Path(path,arc))
                  self.display(3,"Frontier:",self.frontier)
        self.display(1,"No (more) solutions. Total of",
                     self.num_expanded,"paths expanded.")
                     
                     
