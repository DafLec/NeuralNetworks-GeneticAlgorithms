# Genetic Algorithms

Los **algoritmos genéticos** están basados en el proceso de **selección natural**, que de acuerdo a Darwin es el que dirige la evolución biológica.  
Un algoritmo genético continuamente modifica una población de individuos, haciendo cada generación “mejor” que la anterior. Los pasos que se siguen para este proceso suelen ser:  
1. Inicialización  
2. Asignación de potencial   
3. Selección  
4. Reproducción  
5. Mutación  
La inicialización consiste en **establecer una población** donde cada individuo tenga al menos un gen.  
La asignación de potencial es **calcular, con base en un ideal, el potencial** que tiene cada individuo (¿qué tanto se parece al gen ideal?).  
El proceso de selección se puede hacer de dos formas: **al azar o con base en los mejores potenciales**. Este consiste en elegir a 2 padres que crearán a un nuevo individuo.  
La reproducción consiste en **mezclar los genes de los dos padres** para formar a un nuevo individuo para la siguiente generación.
Finalmente, la mutación es **cambiar, aleatoriamente, una parte del gen** del nuevo individuo.  
Estos algoritmos se pueden utilizar para **resolver problemas de optimización**, incluidos los problemas en los que la función objetivo es discontinua, no diferenciable, estocástica o altamente no lineal, problemas que normalmente no son fáciles de resolver con la optimización estándar.  
___
# Neural Networks

Las **redes neuronales** nos ayudan a resolver diversos problemas. Sin embargo, tienen un límite: **los hiperparámetros**. Los hiperparámetros son variablees que determinan la estructura de una red y las variables que determinan cómo debe ser entrenada. Las redes neuronales ntradicinales no pueden hacer el cálculo de los hiperparámetros, pero se pueden **utilizar los algoritmos genéticos para conocer los hiperparámetros para una red neuronal**  
Para esto es necesario:  
1. Crear una población con diversas redes neuronales  
2. Assignarles hiperparámetros de manera aleatoria  
3. Entrenar las redes una a una  
4. Calcular el costo de entrenamiento  
5. Calcular el potencial de cada red neuronal basado en el costo.  
6. Encontrar el potencial máximo en la población.  
7. ...Continuar con el algoritmo genético  

## Referencias
* https://www.mathworks.com/help/gads/what-is-the-genetic-algorithm.html  
* https://www.youtube.com/watch?v=rGWBo0JGf50  
* https://towardsdatascience.com/gas-and-nns-6a41f1e8146d  
* https://static1.squarespace.com/static/58e2a71bf7e0ab3ba886cea3/t/5909113c1b631b40f8137956/1493766462349/1989+neural+networks.pdf  
* https://blog.coast.ai/lets-evolve-a-neural-network-with-a-genetic-algorithm-code-included-8809bece164  
* https://towardsdatascience.com/what-are-hyperparameters-and-how-to-tune-the-hyperparameters-in-a-deep-neural-network-d0604917584a  

