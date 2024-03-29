# Solution of Introduction to AI Robotics by Robin R. Murphy Book

## Table of Contents

* [Robotic Paradigms](/1.Robotic_Paradigms/)
  * [From Teleoperation To Autonomy](/1.Robotic_Paradigms/a.From_Teleoperation_To_Autonomy/README.MD)
  * [The Hierarchical Paradigm](/1.Robotic_Paradigms/b.The_Hierarchical_Paradigm/README.MD)
  * [Biological Foundations of the Reactive Paradigm](/1.Robotic_Paradigms/c.Biological_Foundations_of_the_Reactive_Paradigm/README.md)
  * [The Reactive Paradigm](/1.Robotic_Paradigms/d.The_Reactive_Paradigm/README.md)
  * [Designing a Reactive Implementation](/1.Robotic_Paradigms/e.Designing_a_Reactive_Implementation/README.md)
  * [Common Sensing Techniques for Reactive Robots](/1.Robotic_Paradigms/f.Common_Sensing_Techniques_for_Reactive_Robots/Readme.md)
  * [The Hybrid Deliberative/Reactive Paradigm](/1.Robotic_Paradigms/g.The_Hybrid_Deliberative-Reactive_Paradigm/README.md)
  * [Multi-agents](/1.Robotic_Paradigms/h.Multi-agents/README.md)
* [Navigation](/2.Navigation/)
    * [Topological Path Planning](/2.Navigation/a.Topological_Path_Planning/README.md)
    * [Metric Path Planning](/2.Navigation/b.Metric_Path_Planning/README.md)
    * [Localization and Map Making](/2.Navigation/c.Localization_and_Map_Making/README.md)
    * [On the Horizon](/2.Navigation/d.On_the_Horizon/README.md)

## Some Questions and Answers

* Multi-agent foraging. Start with only a phototropic and avoid-robot behavior, where a robot is an obstacle that isn’t a light. The program will start with an empty world consisting of a light (you may need to make a "bigger light" by placing lights next to each other). Between 2 and 5 phototropic robots will be placed at different random starting locations in the world. Each will wander through the world, avoiding obstacles, until it comes to a light. Then it will move directly to the light (attractive field). If more than one robot is attracted to the same light, they should center themselves evenly around the light. 

<p align="center">
    <img src="docs/image/ligh_move.gif" alt="drawing" width="500"/></p>

* Cooperating to bring the food home. Add the push-to-home behavior where the robot wants to be on a straight line behind the light to home.

<p align="center">
    <img src="docs/image/home_move.gif" alt="drawing" width="500"/></p>

* Dijkstra Algorithm
<p align="center">
    <img src="docs/image/Dijks.png" alt="drawing" width="500"/></p>

* A* Algorithm

<p align="center">
    <img src="docs/image/astar.png" alt="drawing" width="500"/></p>