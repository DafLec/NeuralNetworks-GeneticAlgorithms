
# coding: utf-8

# In[1]:


'''A continuacion podemos encontrar un ejemplo de la implementacion de un algoritmo genetico
    Al final de las iteraciones el ptencial es de 0 como se esperaba
'''
import random

class Individuo():
    def __init__(self):
        self.gen = ""
        self.goal = "geneticforthewin"
        self.r = random.randint(97, 122)
        self.fitness = 0
        for n in range(len(self.goal)):
            self.gen += chr(random.randint(97, 122))
    
    def compareGoal(self,position, c):
        return (int(ord(self.goal[position])-ord(c)))**2
    
    def countFitness(self):
        self.fitness= 0
        for i in range(len(self.goal)):
            self.fitness -= self.compareGoal(i, self.gen[i])
            
    def compareTo(individuo):
        if(self.fitness > individuo.fitness):
            return 1
        else:
            if (self.fitness == individuo.fitness):
                return 0
            else:
                return -1


# In[2]:


popSize = 100;
iterations = 100;
population = []

def selection():
    i1 = population[random.randint(0, popSize-1)]
    i2 = population[random.randint(0, popSize-1)]
    if(i1.fitness > i2.fitness):
        return i1
    else:
        return i2

def makeOffspring(children, p1, p2):
    i1 = Individuo()
    i2 = Individuo()
    
    i1.gen = p1.gen[0:int(len(p1.gen)/2)]+p2.gen[int(len(p2.gen)/2):len(p2.gen)]
    i2.gen = p2.gen[0:int(len(p2.gen)/2)]+p1.gen[int(len(p1.gen)/2):len(p1.gen)]

    children.append(i1)
    children.append(i2)
    
def mutate (i):
    ran = random.randint(0, len(i.goal))
    i.gen = i.gen[0:ran]+chr(random.randint(97, 122))+i.gen[ran+1:(len(i.gen))]
    
for i in range(popSize): #Inicializaacion (poblacion)
    ind = Individuo()
    ind.countFitness(); #Asignación de potencial
    population.append(ind)

for i in range(iterations):#se itera
    offspring= []
    for j in range(int(popSize/2)): #Selección
        p1 = selection()
        p2 = selection()
        makeOffspring(offspring, p1, p2) #Reproduccion
    for j in range(popSize):
        mutate(offspring[j]) #Mutación
        offspring[j].countFitness() #asignación de potencial en la siguiente generación
    
    population.extend(offspring)
    population.sort(key=lambda x: x.fitness, reverse=True)
    
    print(population[0].gen+" "+str(population[0].fitness))

