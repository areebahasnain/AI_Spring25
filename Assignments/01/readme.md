# Question 1


# Question 2
### 1. Playing a decent game of table tennis (ping-pong)
Feasibility: Feasible.

Explanation: AI-powered robots have demonstrated the ability to play table tennis at a high level. These systems use advanced computer vision, real-time motion planning, and reinforcement learning to track the ball, predict trajectories, and execute precise paddle movements. While they may not yet match the adaptability and finesse of top human players, they can play a decent game.

### 2. Playing a decent game of bridge at a competitive level
Feasibility: Feasible.

Explanation: AI systems like Suphx have achieved superhuman performance in bridge, particularly in online platforms. These systems use advanced algorithms to analyze probabilities, strategies, and bidding patterns. However, replicating human-like intuition and partnership dynamics in face-to-face games remains a challenge.

### 3. Writing an intentionally funny story
Feasibility: Partially feasible.

Explanation: AI models like GPT-4 can generate humorous text, including jokes and funny snippets. However, crafting a consistently funny story requires deep understanding of context, timing, and cultural nuances, which AI still struggles with. While AI can produce humor, it often lacks the creativity and subtlety of human-generated humor.

### 4. Giving competent legal advice in a specialized area of law
Feasibility: Partially feasible.

Explanation: AI systems can assist lawyers by analyzing legal documents, identifying precedents, and providing recommendations. However, offering fully competent legal advice requires nuanced understanding of context, ethics, and client-specific factors, which AI cannot yet fully replicate. Legal liability and regulatory concerns also limit the use of AI for direct legal advice.

### 5. Discover and prove a new mathematical theorem
Feasibility: Partially feasible.

Explanation: AI systems like DeepMind’s AlphaTensor and Lean have demonstrated the ability to discover new algorithms and assist in proving theorems. However, discovering and proving entirely new, complex theorems independently remains challenging. AI excels in exploring large search spaces and suggesting potential avenues for proof, but human intuition and creativity are still critical.

### 6. Perform a surgical operation
Feasibility: Partially feasible.

Explanation: Robotic systems like the da Vinci Surgical System can perform surgeries with high precision under human supervision. However, fully autonomous surgical operations are not yet feasible due to the need for real-time decision-making, adaptability to unexpected complications, and ethical concerns. AI can assist in planning and guiding surgeries, but human oversight is still required.

### 7. Unload any dishwasher in any home
Feasibility: Not feasible.

Explanation: Unloading a dishwasher requires advanced robotics, including dexterity, object recognition, and adaptability to different kitchen layouts and dishware arrangements. While robotic arms have made progress in controlled environments, handling the variability and fragility of real-world dishware in diverse home settings remains a significant challenge.

### 8. Construct a building
Feasibility: Partially feasible.

Explanation: AI and robotics can assist in specific aspects of construction, such as design (via generative AI), site surveying (via drones), and bricklaying (via robots like SAM by Construction Robotics). However, constructing an entire building autonomously is infeasible due to the complexity of coordinating tasks, handling unexpected issues, and ensuring safety and compliance with regulations.


# Question 3
## AI Healthcare Diagnosis System
### *Agent Description:*
The agent is an AI-driven healthcare system designed to assist doctors by analyzing medical images, patient records, and lab reports to diagnose diseases.
It uses machine learning models (e.g., deep learning, decision trees) trained on large medical datasets to provide diagnostic recommendations with confidence scores.
The agent can also incorporate rule-based reasoning for handling well-defined medical protocols and guidelines.

Example actions: Detect abnormalities in medical images (e.g., tumors in X-rays), suggest potential diagnoses based on symptoms and lab results, and recommend treatment options.

### *Environment Characteristics:*
**Accessible:** Partially accessible. The agent has access to patient records, medical images, and lab results, but it may not have complete information about all symptoms, patient history, or external factors (e.g., lifestyle, environmental influences).

**Deterministic:** Mostly non-deterministic. The same symptoms or test results can indicate multiple diseases, and the agent must handle uncertainty and variability in medical data.

**Episodic:** Sequential. Patient history and prior diagnoses significantly influence future recommendations, making the environment sequential rather than purely episodic.

**Static:** Dynamic. New patient data, lab results, and updates in medical research constantly change the environment, requiring the agent to adapt over time.

**Continuous:** Continuous. Real-time patient monitoring (e.g., vital signs) and ongoing lab tests provide a continuous stream of data that the agent must process.

### *Best Agent Architecture:*
**Hybrid AI System:**

Combines rule-based reasoning for handling well-defined medical protocols (e.g., "if symptom X and lab result Y, consider diagnosis Z") with deep learning models for pattern recognition and complex decision-making.

Uses convolutional neural networks (CNNs) for analyzing medical images and recurrent neural networks (RNNs) or transformers for processing sequential patient data.

Incorporates uncertainty modeling (e.g., Bayesian networks) to handle the non-deterministic nature of medical diagnoses.

**Model-Based Reflex Agent:**

Uses a learned model of the environment (e.g., relationships between symptoms, lab results, and diseases) to make informed decisions.

Continuously updates its model based on new patient data and medical research.

### *Examples:*
IBM Watson Health: Uses a hybrid approach combining rule-based reasoning and machine learning to assist in cancer diagnosis and treatment recommendations.

Google’s DeepMind: Employs deep learning models for medical imaging analysis, such as detecting eye diseases from retinal scans.

PathAI: Leverages AI to improve pathology diagnostics by analyzing tissue samples and providing diagnostic insights.

# Question 4



