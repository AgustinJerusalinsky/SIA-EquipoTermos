from output import Output
from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs
from state import State
from hanoiTowers import HanoiTowers
from helpers.configHelper import ConfigHelper
from helpers.searchHelper import SearchHelper
import time

def main():
    print("proyectazo de SIA")

    ##Create the helpers
    configHelper = ConfigHelper()
    searchHelper = SearchHelper()

    ##First,check if parameters are ok
    if(configHelper.validateConfigurationProperties()):
        ##Get the heuristic function used
        heuristicFunction = searchHelper.getHeuristicFunction(configHelper.heuristicFunction,configHelper.diskCount,configHelper.destinationTower)
        ##Start the Hanoi with the specified disk count and the heuristic function
        hanoiTowers = HanoiTowers(configHelper.diskCount,configHelper.destinationTower,heuristicFunction)
        ##Get the search method used
        searchMethod = searchHelper.getSearchMethod(configHelper.searchMethod,configHelper.initialState,hanoiTowers)
        initialTime=time.perf_counter()
        ##Start the game
        solution = searchMethod.start()
        finishTime=time.perf_counter()
        if(solution is not None):
            
            output=Output(configHelper.searchMethod,finishTime-initialTime,solution)
            print(output)
        else:
            print('No solution was found :(')

#Variable que existe 
## python3 app.py => settea el name a main ( para ejectuarlo )
## Si quiero un archivo que es una clase y lo intenta de usar main lo patea
if __name__ == "__main__":
    main()