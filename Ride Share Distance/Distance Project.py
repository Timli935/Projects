#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Euclidean_distance(p, q): #computes the Euclidean/linear distance
    return((((p[0]-q[0])**2)+((p[1]-q[1])**2))**(1/2))


# In[3]:


def lyft_distance(p, q): #computes the lyft distance, assuming streets are perpendicular
    return(abs((p[0]-q[0]))+(abs(p[1]-q[1])))


# In[4]:


def trip_cost(p,q): #cost of the trip, assuming $0.4 per mile
    distance = lyft_distance(p,q)
    cost = distance*0.4
    cost="{:.2f}".format(cost) #modify the cost format
    print("The cost of the trip will be $" + cost)


# In[5]:


def compute_distance(p,q, path_type = None): #compute distance depends on input
    if path_type is None:
        return(Euclidean_distance(p, q))  
    else:
        return(lyft_distance(p,q))


# In[13]:


from matplotlib import pyplot as plt #plots the assumed starting, stops, and end points of the trip

start = (-2,3)
stops = [(-1,-2),(3,3),(2,-1)]
end=(4,0)

x_stops=[p[0] for p in stops]
y_stops=[p[1] for p in stops]
start_point = [start[0],start[1]]
stop_point = [end[0],end[1]]

plt.scatter(x_stops,y_stops)
plt.scatter(start_point[0],start_point[1],color="red")
plt.scatter(stop_point[0],stop_point[1],color="gold")


# In[14]:


print(compute_distance((4,5),(-2,-6)))
print(compute_distance((4,5),(-2,-6),path_type="lyft"))


# In[15]:


from itertools import permutations #generate permulations for trip points
perms =permutations(range(3))
perms=list(perms)
perms


# In[16]:


def best_route(start, stops, end): #calculates the best routes
    min_dis = None
    best_perm = None
    for perm in perms:
        d = 0
        points = [start] + [stops[i] for i in perm] + [end]
        for i in range(len(points)-1): #replace the minimum route if there is a shorter one
            d += compute_distance(points[i], points[i+1], path_type="lyft")
        if min_dis is None or d < min_dis:
            min_dis = d
            best_perm = perm
    return (min_dis, best_perm)


# In[17]:


best_distance, best_perm= best_route(start,stops,end)
best_distance, best_perm


# In[18]:


plt.scatter(x_stops,y_stops)
plt.scatter(start_point[0],start_point[1],color="red")
plt.scatter(stop_point[0],stop_point[1],color="gold")

def plot_line(p,q): #plots the minimum routes
    plt.plot([p[0],q[0]],[p[1],q[1]],color="black")
    
plot_line(start,stops[best_perm[0]])
plot_line(stops[best_perm[0]],stops[best_perm[1]])
plot_line(stops[best_perm[1]],stops[best_perm[2]])
plot_line(stops[best_perm[2]],end)


# In[ ]:




