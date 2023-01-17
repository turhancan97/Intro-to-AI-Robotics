1. What is the difference between a primitive and an abstract behavior?
   *  **Primitive behavior** is composed of only one perceptual schema and one motor schema; there is no need to have any coordinated control program. Primitive behaviors can be thought of being monolithic, where they do only one (“mono”) thing. Because they are usually a simple mapping from stimulus to response, they are often programmed as a single method, not composed from multiple methods or objects. The concept of Perceptual and Motor Schema is there, but hidden for the sake of implementation. Behaviors which are assembled from other behaviors or have multiple perceptual schema and motor schema will be referred to as abstract behaviors, because they are farther removed from the sensors and actuators than a primitive behavior. The use of the term **abstract behavior** should not be confused with an abstract class in OOP.
   *  Primitive behaviors and abstract behaviors are two different types of behaviors that can be used in robotic systems.
   *  Primitive behaviors are basic, low-level behaviors that are directly controlled by sensor inputs and have a well-defined set of actions. They are typically simple, atomic actions that the robot can perform, such as avoiding obstacles, following a line, or approaching a goal. Primitive behaviors are used to handle specific, well-defined tasks and are easy to implement, test and debug.
   *  Abstract behaviors, on the other hand, are higher-level behaviors that are built on top of primitive behaviors. They are more complex, involving multiple primitive behaviors and decision-making processes. Abstract behaviors can perform more complex tasks such as navigating through a maze, or interacting with humans. They are more difficult to implement, test and debug, but can handle more complex and dynamic environments.
   *  In summary, the main difference between primitive and abstract behaviors is that primitive behaviors are simple, low-level behaviors that are directly controlled by sensor inputs and have a well-defined set of actions, while abstract behaviors are higher-level behaviors that are built on top of primitive behaviors and can perform more complex tasks.

2. Define:
    a. behavior table
    b. causal chain
    c. coordinated control programy
3. Can the perceptual schema and the motor schema for a behavior execute asynchronously, that is, have different update rates?
4. Fig. 5.2 shows two methods of implementing a potential fields-based follow-corridor behavior. A third way is to have two instances of a move-away-from-wall (perpendicular) behavior with a move-parallel-to-wall behavior. What are the advantages and disadvantages of such an implementation?
5. List and describe the steps in designing a reactive system
6. Consider the Pick Up the Trash example in Sec. 5.5.2. The example assumed the arena was empty except for walls, cans, and trash cans. What would happen if there were chairs and tables present? Could the gripper accidently scoop a chair or table leg? How would the system react? What changes, if any, would need to be made to the behavior table and FSA?
7. Solve the 1994 International Association for Unmanned Systems Unmanned Ground Vehicle problem using STRIPS (Ch. 2). Be sure to include a world model and a difference table.y
8. Solve the 1994 AAAI Pick Up the Trash problem using STRIPS (Ch. 2). Be sure to include a world model and a difference table.
9.  How is defining a robot’s behaviors linked to the robot’s ecological niche?y
10. What is special about a primitive behavior in terms of perceptual and motor schema?y
11. Construct a Behavioral Table of the behaviors needed for a robot to move from room to room.
12. What are the two main deficits encountered when designing and implementing reactive robotic systems?
13. Make up a task for a robot to complete. Describe what each of the 7 steps of the design methodology would require you to do to complete the task.
14. Describe the two methods for assembling primitive behaviors into abstract behaviors: finite state automata and scripts.
15. Assume that the CSM robot had been wider and needed to use an avoid-obstacle behavior. Make a Behavior Table to include this new behavior.y
16. Assuming the state of the robot in question 1, describe how the coordinated control program should handle concurrent behaviors.
17. Recall how some mammals freeze when they see motion (an affordance for a predator) in an attempt to become invisible, and persist in this behavior until the predator
is very close, then flee. Define this behavior using Behavior Tables.
1.  Suppose the competition course described in Section 5.4 has been modified so that a hay bale can be placed directly on the white line. The robot must move around the bale and rejoin the line on the other side. Create a behavior table that not only follows
the line but correctly responds to the bale so that it can continue following the line.
1.  [World Wide Web] Search the web for the International Association for Unmanned Systems competition home page and briefly describe three unmanned vehicle projects linked to the IAUS site.
2.  [World Wide Web] Identify at least 5 robot competitions, and for each describe the basic task. Can the task be accomplished with a reactive robot? Why or why not?
3.  [Programming] Using Rug Warrior kits, Lego Mindstorms kits, or similar robotics tools, implement your own schools version of an IAUS Unmanned Ground Robotics Competition. Your class should decide on the course, the course objectives, rules, and prizes (if any). Groups should not begin construction of their robot without first describing the
steps involved in designing a reactive behavioral system for the task at hand.y
1.  [Programming] Write a script in pseudo-code for following a hallway. Consider that the robot may start in a hallway intersection facing away from the hallway it is supposed to take. Also the robot might start in the middle of a hall facing a wall, rather than having forward point to the long axis of the hall.
2.  [Programming] The Pick Up the Trash competitions were a bit different than actually presented in this book. For example, the robots were actually permitted to cache up to three cans before going to the trash can, and the robots could go after white Styrofoam cups as trash. How would you integrate this into:
    a. the FSA and
    b. the script described in the book?
3.  [Programming] Could the exception handling sub-scripts for picking up trash be implemented with the exception handling functionality provided by Ada or C++?
4.  [Advanced Reading] Read Rodney Brooks’ one paragraph introduction to Chapter 1 in Cambrian Intelligence 28 on the lack of mathematics in behavioral robotics. Now consider the behavior of the CSM robot around white shoes and dandelions. Certainly it would be useful to have theories which can prove when a behavioral system will fail. Is it possible?
