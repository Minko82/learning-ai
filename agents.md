# 📜 Chapter 1: Intelligent Agents & Environments

## 1️⃣ What is an **Agent**?
**Agent** → Any entity that **perceives its environment** and **acts upon it** to achieve a goal.

💡 **Formula:**  

$$
\text{Agent} = \text{Percepts} + \text{Actions}
$$

<br>

---

## 2️⃣ Percepts & Percept Sequence
- **Percept** → The input data that an agent receives from its environment.  
- **Percept Sequence** → The **history** of all percepts the agent has received.  

📌 **Example:**  
- A self-driving car perceives **lane markings, traffic lights, and nearby vehicles.**  
- A chatbot perceives **text input from users.**  

<br>

---

## 3️⃣ What is an Agent Function?
**Agent function** → a mapping from **percept sequences** to **actions**:

$$
 f: P^* \rightarrow A
$$

Where:
- **\( P^* \)** = All possible percept sequences
- **\( A \)** = Set of all possible actions

📌 **Example:**  
- A self-driving car **(Agent)** receives a **traffic light is red (Percept)** → The function decides to **brake (Action).**


<br>

---

## 4️⃣ What is an Agent Program?
**Agent program** → the actual **implementation** of the agent function in **code**.

📌 **Example:** A thermostat can be implemented as:

```python
# Simple reflex agent for a thermostat
def thermostat(percept):
    if percept == "Too Hot":
        return "Turn AC On"
    elif percept == "Too Cold":
        return "Turn Heater On"
    else:
        return "Do Nothing"
```

<br>

---

## 7️⃣ Rationality & Performance Measures
- **Rationality** → Choosing the action that **maximizes expected success**  
- **Performance Measure** → Defines **what is "good" behavior**

**⚠️ Can't call an agent rational if there's no performance measure ⚠️**

<br>

📌 **Example:**  
- For a chess bot, winning is good, losing is bad.  
- For a search engine, **relevant results** improve performance.

<br>

**Rationality is based on PEAS:**

$$
\text{Agent} = \text{Performance} + \text{Environment} + \text{Actuator} + \text{Sensors} 
$$

📌 **Example:**  

| Agent Type | Performance Measure | Environment | Actuators | Sensors |
|------------|----------------------|-------------|-----------|---------|
| **Taxi Driver** | Safe, fast, legal, comfortable trip, maximize profit | Roads, traffic, pedestrians, customers | Steering, accelerator, brake, signal, horn, display | Cameras, sonar, speedometer, GPS, odometer, accelerometer, engine sensors, keyboard |



<br>

---

## 6️⃣ Task Environments
**Task environment** → the "problems" that rational agents are the "solution"

**Environment** → **everything an agent interacts with**.

<br>

**Properties of Environments:**



<br>

---

## 🌟 Summary
✔ **Agents perceive and act on environments.**  
✔ **Environments can be:**  
  - static/dynamic
  - observable/partially observable
  - deterministic/stochastic
  - discrete/continious
  - benign/adversarial
  - single agent/multi-agentepisodic/sequential
    
✔ **A rational agent selects actions that maximize performance based on percepts.**  

---

