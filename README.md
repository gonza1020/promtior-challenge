
# Promtior challenge

Chatbot implementando arquitectura RAG que permite responder preguntas acerca de Promtior.

El chatbot consta de 2 partes , el frrntend desarrollado con Next.js y el backend desarrollado en Python. Ambas partes de la aplicacion fueron desplegadas en Azure utilizando el servicio Azure Container Instances (ACI).



## Introduccion
El objetivo de este challenge es desarrollar un chatbot utilizando la arquitectura RAG y la libreria langchain para poder responder a las siguientes preguntas. 

- What services does Promtior offers?
- When was the company founded?


## Diagrama

![Diagrama](/doc/diagram.jpg)


## Desafios

Realizar este challenge fue una experiencia desafiante y nueva para mi ya que es una tecnologia nueva y me tuve que informar profundamente acerca de todos los componentes involucrados en la solucion. 
Langchain provee una documentacion solida lo cual me permitio poder finalizar este desafio sin mayores problemas. Ademas de eso, tambien investigue en otras fuentes para poder aclarar algunos conceptos.

## Problemas encontrados
1. Comunicacion entre contenedores en Azure.
- Se soluciono habilitando ip's publicas para cada contenedor.






## 🔗 Link

http://promtior-challenge.g7h0hmaygedzh0f8.eastus.azurecontainer.io:3000/


