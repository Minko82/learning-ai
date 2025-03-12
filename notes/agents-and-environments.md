# 📜 Intelligent Agents & Environments

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

## 5️⃣ Rationality & Performance Measures
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

📌 **Properties of Environments:**

### **Observability**
| Property | Meaning |
|------------|------------------------------------------------|
| **Fully Observable** | Agent has complete knowledge of the world |
| **Partially Observable** | Agent only has limited information |
| **Unobservable** | Agent has no direct perception of the environment |

<br>

### **Determinism vs. Stochasticity**
| Property | Meaning | Example |
|------------|------------------------------------------------|-----------------------------|
| **Deterministic** | Next state is fully determined by actions | Calculator |
| **Stochastic** | Actions have uncertainty | Weather forecast |

<br>

### **Discrete vs. Continuous**
| Property | Meaning |
|------------|------------------------------------------------|
| **Discrete** | The agent has finitely many distinct actions |
| **Continuous** | The agent has infinitely many possible actions |

<br>

### **Benign vs. Adversarial**
| Property | Meaning |
|------------|------------------------------------------------|
| **Benign** | There is no opposing agent working against the system |
| **Adversarial** | The environment includes agents with conflicting objectives |

<br>

### **Single Agent vs. Multi-Agent**
| Property | Meaning |
|------------|------------------------------------------------|
| **Single Agent** | Only one agent is operating in the environment |
| **Multi-Agent** | Multiple agents interact, possibly cooperatively or competitively |

<br>

### **Episodic vs. Sequential**
| Property | Meaning | Example |
|------------|------------------------------------------------|-----------------------------|
| **Episodic** | Decisions don’t affect future percepts | Image classification |
| **Sequential** | Past decisions impact the future | Chess, driving |

<br>

### **Static vs. Dynamic**
| Property | Meaning | Example |
|------------|------------------------------------------------|-----------------------------|
| **Static** | The environment doesn’t change while deciding | Sudoku |
| **Dynamic** | The world keeps changing | Self-driving cars |
