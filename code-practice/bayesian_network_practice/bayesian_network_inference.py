"""
🔢 Bayesian Network Inference (AIMA)

This Python script demonstrates how to perform probabilistic inference using
Bayesian networks and functions from the AIMA framework (`probability4e` module).

Includes:
- Enumeration-based queries
- Prior and conditional probability calculations
- Variable elimination
"""

#!/usr/bin/env python
# coding: utf-8

from probability4e import *
from utils4e import print_table



T, F = True, False

net = BayesNet([
    ('thunderstorms', '', 0.014),
    ('coldFront', '', 0.006),
    ('tornado', ['thunderstorms', 'coldFront'], {
        (T, T): 0.56, 
        (T, F): 0.32,
        (F, T): 0.04,
        (F, F): 0.001}),
    ('propertyDamage', 'tornado', {T: 0.47, F: 0.005}),
    ('injuries', 'tornado', {T: 0.057, F: 0.009})
])

print('1.1=', enumeration_ask('tornado', {}, net)[True])
print('1.2=', enumeration_ask('propertyDamage', {}, net)[True])
print('1.3=', enumeration_ask('thunderstorms', {'tornado': T}, net)[True])


T, F = True, False

burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', ['Burglary', 'Earthquake'],
     {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
])
print(burglary.variables) # prints out all nodes present in the BayesNet



# With definition of the function given above, X is the variable whose value we are looking for, 
# and e is the evidence we know

# In this problem, we are looking for the probability that John calls (X) given burglary is True (e)
# If you notice below, we add the [True] to the function, this is because enumeration_ask returns a type of dictionary
# whose keys are possible values of the variable X (True, False)

enumeration_ask('JohnCalls', {'Burglary': T}, burglary)[True]
# 0.849017

enumeration_ask('JohnCalls', {}, burglary)[True]
# 0.0521389757

enumeration_ask('Earthquake', {'MaryCalls': T}, burglary)[True]
# 0.03588091528645573




john = enumeration_ask('JohnCalls', {'Burglary': T}, burglary)[True]
mary = enumeration_ask('MaryCalls', {'Burglary': T}, burglary)[True]
john_and_mary = john * mary
print(john_and_mary)

john + mary - john_and_mary
# 0.9484564873653999


heart_disease_network = BayesNet([
    ('SmokingAndAlcohol', '', 0.25),
    ('ModerateExercise', '', 0.5),
    ('HighBP', ['SmokingAndAlcohol', 'ModerateExercise'],{
        (T, T): 0.62, 
        (T, F): 0.74,
        (F, T): 0.31,
        (F, F): 0.51
    }),
    ('Atherosclerosis', '', 0.55),
    ('FamilyHistory', '', 0.15),
    ('HeartDisease', ['Atherosclerosis', 'HighBP', 'FamilyHistory'], {
        (T, T, T): 0.92,
        (T, T, F): 0.91,
        (T, F, T): 0.79,
        (T, F, F): 0.77,
        (F, T, T): 0.74,
        (F, T, F): 0.69,
        (F, F, T): 0.38,
        (F, F, F): 0.22
    }),
    ('AnginaPectoris', 'HeartDisease', {
        T: 0.85,
        F: 0.42
    }),
    ('RapidHeartbeats', 'HeartDisease', {
        T: 0.99,
        F: 0.3
    })
])

enumeration_ask('HeartDisease', {}, heart_disease_network)[True]

enumeration_ask('AnginaPectoris', {'SmokingAndAlcohol': T, 'ModerateExercise': F, 'FamilyHistory': T}, heart_disease_network)[True]

enumeration_ask('Atherosclerosis', {'AnginaPectoris': T, 'RapidHeartbeats': T, 'FamilyHistory': T}, heart_disease_network)[True]

print('Without any change in lifestyle:', enumeration_ask('HeartDisease', {'SmokingAndAlcohol': T, 'ModerateExercise': F, 'FamilyHistory': T}, heart_disease_network)[True])

print('Start exercise:', enumeration_ask('HeartDisease', {'SmokingAndAlcohol': T, 'ModerateExercise': T, 'FamilyHistory': T}, heart_disease_network)[True])
print('Stop smoking:', enumeration_ask('HeartDisease', {'SmokingAndAlcohol': F, 'ModerateExercise': F, 'FamilyHistory': T}, heart_disease_network)[True])
print('Stop smoking and start excercise:', enumeration_ask('HeartDisease', {'SmokingAndAlcohol': F, 'ModerateExercise': T, 'FamilyHistory': T}, heart_disease_network)[True])

# The difference in the original probability vs. specific lifestyle choices (in order, as displayed above)
print((0.7782899999999999 - 0.75027)  / 0.7782899999999999 * 100)
print((0.7782899999999999 - 0.724585) / 0.7782899999999999 * 100)
print((0.7782899999999999 - 0.677885) / 0.7782899999999999 * 100)