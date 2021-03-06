# -*- coding: utf-8 -*-
"""Mine_Field.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m9MAdC8AM49EvQYvPENTWhSAva_7RrIq
"""

pip install python-sat



from pysat.solvers import Glucose3
from Agent.py import*

#[Left, right, Up, Down] where 65 is a dummy node ( always false )
neighbour={1: [65,2, 5,65], 2: [1, 3, 6,65], 3: [2, 4, 7,65],4: [3,65, 8,65],5: [65,1, 6, 9], 6: [5, 7, 2, 10],
 7: [6, 8, 3, 11], 8: [4, 7, 12,65], 9: [65,5, 10, 13], 10: [9, 11, 6, 14], 11: [10, 12, 7, 15],
 12: [8, 11, 16, 65], 13: [65,9, 65,14], 14: [13, 15,65, 10], 15: [14, 16,65, 11], 16: [15,65,65, 12]}

g = Glucose3()

def percept0(l,r,u,d,p0):
  clauses = []
  g.add_clause([-1*d,-1*p0 ])
  clauses.append([-1*d,-1*p0 ])
  g.add_clause([1*d, 1*l, 1*p0, 1*r, 1*u])
  clauses.append([1*d, 1*l, 1*p0, 1*r, 1*u])
  g.add_clause([-1*l, -1*p0] )
  clauses.append([-1*l, -1*p0] )
  g.add_clause([-1*r, -1*p0] )
  clauses.append([-1*r, -1*p0] )
  g.add_clause([-1*u, -1*p0] )
  clauses.append([-1*u, -1*p0] )
  return clauses


def percept1(l,r,u,d,p1):
  clauses = []
  g.add_clause([-1*d,-1*p1,-1*r])
  clauses.append([-1*d,-1*p1,-1*r])
  g.add_clause([-1*l,-1*d,-1*p1])
  clauses.append([-1*l,-1*d,-1*p1])
  g.add_clause([l,-1*d, p1, r, u])
  clauses.append([l,-1*d, p1, r, u])
  g.add_clause([-1*d,-1*p1,-1*u])
  clauses.append([-1*d,-1*p1,-1*u])
  g.add_clause([d,-1*l,p1, r, u])
  clauses.append([d,-1*l,p1, r, u])
  g.add_clause([d,l,-1*p1, r, u])
  clauses.append([d,l,-1*p1, r, u])
  g.add_clause([d,l,p1, -1*r, u])
  clauses.append([d,l,p1, -1*r, u])
  g.add_clause([d,l,p1, r, -1*u])
  clauses.append([d,l,p1, r, -1*u])
  g.add_clause([-1*l,-1*p1,-1*r])
  clauses.append([-1*l,-1*p1,-1*r])
  g.add_clause([-1*l,-1*p1,-1*u])
  clauses.append([-1*l,-1*p1,-1*u])
  g.add_clause([-1*u,-1*p1,-1*r])
  clauses.append([-1*u,-1*p1,-1*r])
  return clauses

def percept2(l,r,u,d,p2):
  clauses= []
  g.add_clause([-1*d, -1*l, p2])
  clauses.append([-1*d, -1*l, p2])
  g.add_clause([-1*d, -1*r, p2])
  clauses.append([-1*d, -1*r, p2])
  g.add_clause([-1*d, -1*u, p2])
  clauses.append([-1*d, -1*u, p2])
  g.add_clause([d, l, -1*p2, r])
  clauses.append([d, l, -1*p2, r])
  g.add_clause([d, l, -1*p2, u])
  clauses.append([d, l, -1*p2, u])
  g.add_clause([d, -1*p2, r, u ])
  clauses.append([d, -1*p2, r, u ])
  g.add_clause([-1*l, p2, -1*r ])
  clauses.append([-1*l, p2, -1*r ])
  g.add_clause([-1*l, p2, -1*u])
  clauses.append([-1*l, p2, -1*u])
  g.add_clause([l, -1*p2, r, u ])
  clauses.append([l, -1*p2, r, u ])
  g.add_clause([p2, -1*r, -1*u])
  clauses.append([p2, -1*r, -1*u])
  return clauses

def Explore_rooms(ag, visited, goalLoc, dfsVisited,path): #dfs to new safe room
    curr_pos=ag.FindCurrentLocation()
    curLoc= 4*(curr_pos[1]-1)+curr_pos[0] #convert to location index
    if(curLoc==goalLoc or curLoc == 16 ):
        return True
    dfsVisited[curLoc]=True
        
    if curr_pos[1]+1 <= 4:
      if (visited[curLoc+4]==True ):
        if dfsVisited[curLoc+4]==False:
          ag.TakeAction('Up')
          cell = ag.FindCurrentLocation()
          path.append(cell)          
          if Explore_rooms(ag, visited, goalLoc, dfsVisited,path):
              return True
          path.remove(cell)
          ag.TakeAction('Down')
          

    if curr_pos[0]+1 <= 4:
      if (visited[curLoc+1]==True  ):
        if dfsVisited[curLoc+1]==False:
          ag.TakeAction('Right')
          cell = ag.FindCurrentLocation()
          path.append(cell)          
          if Explore_rooms(ag, visited, goalLoc, dfsVisited,path):
              return True
          path.remove(cell)
          ag.TakeAction('Left')
          

    if curr_pos[1]-1 >= 1:
      if (visited[curLoc-4]==True ):
        if dfsVisited[curLoc-4]==False:
          ag.TakeAction('Down')
          cell = ag.FindCurrentLocation()
          path.append(cell)          
          if Explore_rooms(ag, visited, goalLoc, dfsVisited,path):
              return True
          path.remove(cell)
          ag.TakeAction('Up')
          

    if curr_pos[0]-1 >= 1:
      if (visited[curLoc-1]==True ):
        if dfsVisited[curLoc-1]==False:
          ag.TakeAction('Left')
          cell = ag.FindCurrentLocation()
          path.append(cell)          
          if Explore_rooms(ag, visited, goalLoc, dfsVisited,path):
              return True
          path.remove(cell)
          ag.TakeAction('Right')
          

    

    

    return False

def ExitWumpusWorld(ag, clauses ):
  clauses.append([-65]) # 65 represents dummy node which never has mine.
  clauses.append([-16]) # 16 represents the final state which can never have a mine.
  clauses.append([-1]) # start can never have a mine.
  path = [] # will store the path
  visited = [False for i in range(17)] #Rooms Visited till now 
  visited[1] = True
  while(ag.FindCurrentLocation()!=[4, 4]):
   
    percept= ag.PerceiveCurrentLocation()
    curr_pos = ag.FindCurrentLocation()
    curLocIndex= 4*(curr_pos[1]-1)+ curr_pos[0]
    visited[curLocIndex]=True
    
    if percept=='=0': 
      g.add_clause( [16+ curLocIndex] ) # 16-32 represents percept 0
      clauses.append([16+ curLocIndex])
      g.add_clause([ -1* (32+curLocIndex) ])
      clauses.append([ -1* (32+curLocIndex) ])
      g.add_clause([ -1* (48+curLocIndex) ])
      clauses.append([ -1* (48+curLocIndex) ])
    elif percept == '=1':
      g.add_clause( [32+ curLocIndex] )  # 32-48 represents percept 1
      clauses.append([32+ curLocIndex])
      g.add_clause([ -1* (48+curLocIndex) ])
      clauses.append([ -1* (48+curLocIndex) ])
      g.add_clause([ -1* (16+curLocIndex) ])
      clauses.append([ -1* (16+curLocIndex) ])
    else:
      g.add_clause( [48+ curLocIndex] ) # 48-64 represents percept 2
      clauses.append([48+ curLocIndex])
      g.add_clause([ -1* (16+curLocIndex) ])
      clauses.append([ -1* (16+curLocIndex) ])
      g.add_clause([ -1* (32+curLocIndex) ])
      clauses.append([ -1* (32+curLocIndex) ])

            
    for newLoc in [16,15,12,14,11,8,13,10,7,4,9,6,3,5,2,1]:
        if visited[newLoc]==False:
          tempclauses= clauses 
          tempclauses.append([newLoc])
          g1 = Glucose3()
          g1.append_formula(tempclauses)
          tempclauses.remove([newLoc])
          if g1.solve() == False:
              #Room is safe
              clauses.append([-1*newLoc])
              dfsVisited = [False for i in range(17)] 
              visited[newLoc] = True
              roomReachable=Explore_rooms(ag, visited, newLoc, dfsVisited,path) #dfs to new safe Room
              if roomReachable:
                  break
  return path



def initialise_knowledge():
# 1-16 is mine locations ( T/F )
# 17-32 is percept 0 ( T/F )
# 33-48 is percept 1 ( T/F )
# 49-64 is percept 2 ( T/F )
  mega_clause = []
  for i in range (1,17):
    mega_clause.extend(percept0(neighbour[i][0],neighbour[i][1], neighbour[i][2], neighbour[i][3], i+16 ))
    mega_clause.extend(percept1(neighbour[i][0],neighbour[i][1], neighbour[i][2], neighbour[i][3], i+32 ))
    mega_clause.extend(percept2(neighbour[i][0],neighbour[i][1], neighbour[i][2], neighbour[i][3], i+48 ))
  return mega_clause



def main():
    cl = initialise_knowledge()
    ag = Agent()
    print('Start Location: {0}'.format(ag.FindCurrentLocation()))
    path = ExitWumpusWorld(ag, cl)   

    print('{0} reached. Exiting the Wumpus World.'.format(ag.FindCurrentLocation()))

main()

