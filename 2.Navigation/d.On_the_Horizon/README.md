# Exercises - Chapter 12

## On the Horizon

---

1. Define polymorphism. List the challenges for sensing and intelligent control for a polymorphic platform.

Polymorphism refers to the ability of an object or platform to change its form, structure, or shape in order to adapt to different environments and tasks. In robotics, polymorphism refers to the concept of shape-shifting robots, where a single platform can change its physical form and shape in response to different scenarios, environments, or tasks. This allows the robot to become better suited to a particular situation and improve its overall efficiency and effectiveness. The challenges for sensing and intelligent control in polymorphic robots include the ability to accurately sense changes in the environment, the ability to control and coordinate multiple actuators and parts during shape-shifting, and the ability to make decisions about when and how to change the form of the robot.

The detailed challenges for sensing and intelligent control for a polymorphic platform are as follows:

    Complexity: A polymorphic platform can be complex to design, as it requires multiple methods or functions that can operate on a variety of inputs. This complexity can increase the risk of errors and decrease efficiency.

    Integration: It can be difficult to integrate multiple systems and sensors into a single platform.

    Robustness: The different forms of a polymorphic platform may have different strengths and weaknesses, making it difficult to design a system that is robust in all conditions.

    Interoperability: It can be challenging to ensure that different parts of a polymorphic platform can communicate with each other effectively.

    Dynamic adaptation: The ability to dynamically adapt to different environments and conditions is crucial for the success of a polymorphic platform. This requires sophisticated sensors and control systems that can respond quickly to changes in the environment.

2. Consider designing a robot platform for urban search and rescue. What are the advantages and disadvantages of polymorphism? What are the advantages and disadvantages of a humanoid platform? 

Polymorphism in urban search and rescue (USAR) robots can provide the advantage of versatility, adaptability, and the ability to access tight or narrow spaces. A polymorphic platform can transform into different shapes and forms to perform specific tasks, such as crawling, rolling, or flying. It can also fit into tight spaces, reach high places, and traverse rough terrain.

However, polymorphism also brings some disadvantages. It can be challenging to design and control a shape-shifting robot that is stable, safe, and reliable. Polymorphic robots often require more complex control systems and may not be as strong or durable as a non-shape-shifting robot. They also may not have the same dexterity or precision as a specialized robot for a specific task.

On the other hand, humanoid robots have the advantage of a more natural and intuitive interface, as well as the ability to perform tasks that require human-like dexterity and manipulation. They also have the advantage of being able to perform a wider range of tasks than a non-humanoid robot.

However, humanoid robots also have some disadvantages in the context of USAR. They may be less stable and have a higher risk of falling or getting stuck in tight spaces. They may also be slower or less effective than specialized robots for specific tasks. They may also require more complex control systems and be more expensive to develop and maintain than non-humanoid robots.

In conclusion, both polymorphic and humanoid robots have their advantages and disadvantages in the context of USAR. The choice between the two will depend on the specific requirements and constraints of the mission, such as task requirements, safety concerns, and cost constraints.

3. Define adjustable autonomy. What teleoperation scheme does it most closely resemble? Is there a real difference between it and teleoperation?

Adjustable autonomy refers to a system where the level of control given to the robot can be adjusted on the fly, allowing for a range of possibilities from full human control to full autonomous control. The level of control can be adjusted based on the current task, environment, or other factors.

Adjustable autonomy most closely resembles teleoperation, where the human operator has direct control over the robot's movements. However, there is a difference between the two in that with adjustable autonomy, the level of control can be dynamically adjusted, whereas in teleoperation, the level of control is typically fixed.

4. Propose a robot or robot society for the humanitarian applications below. Specify the Paradigm and architecture you would use. Justify your answer. a. Demining. b. Urban search and rescue.

For a. Demining:

Paradigm: Autonomous or Semi-autonomous
Architecture: Mobile robot with obstacle avoidance and metal detection sensors

Justification: Demining requires a robot that can navigate through potentially dangerous terrain and accurately detect the presence of landmines. The use of autonomous or semi-autonomous systems allows the robot to operate independently and reduces the risk to human operators. A mobile robot with obstacle avoidance sensors ensures that the robot can navigate through challenging terrain and avoid obstacles that may pose a threat. Additionally, metal detection sensors are crucial for detecting the presence of landmines.

For b. Urban search and rescue:

Paradigm: Teleoperation or Hybrid (Teleoperation with some autonomous features)
Architecture: Legged robot or tracked robot with high mobility and a range of sensors

Justification: Urban search and rescue often requires robots to navigate through complex and challenging environments. A legged robot or tracked robot with high mobility is well-suited for this task, as it can traverse obstacles and maneuver through tight spaces. Teleoperation or a hybrid of teleoperation and autonomous features allows for human operators to control the robot and make decisions, while also allowing the robot to perform certain tasks autonomously. A range of sensors, such as cameras, microphones, and thermography sensors, can be used to gather information about the environment and help locate victims.

5. [Advanced Reading] Look up and define neural networks. How are they being used for robotics? What makes them different from other approaches? Who are the researchers using neural networks?

Neural networks are a type of machine learning algorithm modeled after the structure and function of the human brain. They consist of layers of interconnected nodes, or artificial neurons, that use a set of weighted connections to process and transmit information. Neural networks can be trained to recognize patterns and make predictions based on input data, making them well-suited for a wide range of applications, including robotics.

In robotics, neural networks are used for tasks such as perception, control, and decision-making. For example, they can be used to process sensory data from cameras or other sensors to detect and identify objects or to perform object recognition and tracking. Neural networks can also be used to control the motion of robots or to generate motion patterns for different tasks.

What makes neural networks different from other approaches is their ability to learn from experience and improve over time. Unlike traditional rule-based systems, neural networks can adapt to changing environments and find solutions to complex problems without being explicitly programmed to do so. Researchers using neural networks include computer scientists, engineers, and roboticists. Some of the leading institutions and researchers in this field include MIT, Carnegie Mellon University, and Google Brain.

6. [Advanced Reading] Look up and define genetic algorithms. How are they being used for robotics? What makes them different from other approaches? Who are the researchers using genetic algorithms?

Genetic algorithms are a type of optimization algorithm inspired by Charles Darwin's theory of evolution. They work by randomly generating a population of candidate solutions and then iteratively selecting the best solutions for reproduction and mutation. The result is a gradual evolution of better solutions over multiple generations.

In robotics, genetic algorithms are used for a variety of purposes, including parameter tuning, motion planning, and control. They are particularly useful in situations where the optimization problem is complex and difficult to solve using traditional methods. For example, they have been used to optimize the parameters of a neural network controller for a robot arm, or to find the optimal path for a robot to follow in an unknown environment.

What makes genetic algorithms different from other approaches is that they do not require a detailed understanding of the underlying optimization problem. Instead, they work by generating and testing a large number of candidate solutions until a good one is found. This makes them well-suited for solving problems with many unknowns or where the relationship between inputs and outputs is not well understood.

Some of the researchers using genetic algorithms in robotics include Marco Dorigo, Riccardo Poli, and David E. Goldberg.

7. [World Wide Web] Do a web search and report on the types of robot pets currently available or proposed. What is the motivation for each pet? What are the difficult issues being addressed?

Robot pets are an emerging trend in the field of robotics, and they are becoming increasingly popular as people look for new ways to interact with technology. There are several different types of robot pets currently available or proposed, each with its own unique features and capabilities.

One type of robot pet is the entertainment robot. These robots are designed primarily for entertainment purposes, and they are often used as interactive toys. Examples of entertainment robot pets include the Zoomer Dino, which can be trained to perform tricks, and the FurReal Friends, which are lifelike robots that are designed to be played with and cared for like real pets.

Another type of robot pet is the therapeutic robot. These robots are designed to provide comfort and support to people who are dealing with physical or emotional challenges, such as dementia patients, children with autism, or people with anxiety or depression. Examples of therapeutic robot pets include Paro, a robotic seal that has been shown to reduce stress and anxiety in dementia patients, and the Nao robot, which has been used to help children with autism improve their social and communication skills.

There are also robot pets that are designed for education and research purposes. These robots are often used to teach children about science, technology, engineering, and mathematics (STEM) subjects, and they are also used in research projects to explore new technologies and methods. Examples of educational robot pets include the LEGO Mindstorms robots, which can be programmed to perform a variety of tasks, and the NAO robots, which have been used in research projects to study human-robot interaction.

The motivation behind each type of robot pet is different, but they all share the goal of improving human-robot interaction and exploring new and innovative ways to interact with technology. The difficult issues being addressed include the development of realistic, lifelike robots that can provide meaningful and engaging experiences for users, and the development of algorithms and technologies that can help robots understand and respond to human emotions and behaviors.

8. [World Wide Web] Search the web for more information about the Honda humanoid robot, Cog, and Robonaut. Compare and contrast the motivation and objectives of each.

Honda humanoid robot is a robot developed by Honda Motors to help in various tasks such as assisting people with physical disabilities, helping in hazardous situations, and providing companionship. The main objective of this robot is to provide mobility and dexterity to people with physical disabilities, and to help in various tasks that are hazardous or difficult for human beings.

Cog is a humanoid robot developed by MIT's AI Lab and Harvard's Wyss Institute for Biologically Inspired Engineering. The main objective of Cog is to study human cognitive and motor skills and to understand how robots can be designed to perform tasks in a similar manner to humans. Cog is designed to mimic human movements and behaviors, and its main motivation is to understand how humans interact with their environment and other objects.

Robonaut is a humanoid robot developed by NASA and General Motors. The main motivation for Robonaut is to help astronauts perform tasks in space, especially in hazardous environments where human intervention is not possible. Robonaut is designed to be highly dexterous and has a flexible arm that can be used for various tasks. The main objective of Robonaut is to perform various tasks in space, including maintenance and repair work, that would otherwise be impossible for human astronauts to perform.

In conclusion, Honda humanoid robot is motivated by providing mobility and dexterity to people with physical disabilities, and to help in various tasks that are hazardous or difficult for human beings. Cog is motivated by understanding human cognitive and motor skills and how robots can be designed to perform tasks in a similar manner to humans. Robonaut is motivated by performing various tasks in space, especially in hazardous environments where human intervention is not possible. Each of these robots has its own unique objectives and motivations, and they are all making important contributions to the field of robotics.