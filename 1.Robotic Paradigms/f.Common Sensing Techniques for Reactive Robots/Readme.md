1. Define sensor suite, active/passive sensors, dead reckoning, computer vision.

    **Sensor suite** refers to a set of sensors that are installed on a robot for the purpose of collecting information about the environment. This information is used by the robot to make decisions and perform tasks.

    **Active sensors** are sensors that emit a signal and then analyze the reflection or signal to determine some aspect of the environment. Examples of active sensors include LIDAR and RADAR.

    **Passive sensors**, on the other hand, do not emit a signal but simply detect energy that is naturally present in the environment. Examples of passive sensors include cameras and microphones.

    **Dead reckoning** is a navigation method used by robots in which the robot uses information about its own motion to estimate its position. This method is based on the assumption that the robot's motion is constant and that the robot knows its initial position.

    **Computer vision** refers to the field of computer science that is concerned with giving machines the ability to interpret and understand visual information from the world. This involves using algorithms and machine learning techniques to analyze images and video from cameras to recognize objects, estimate distances, and perform other tasks.

2. Compare and contrast the RGB and HSV color representations specifying the advantages and disadvantages of each type.

RGB (Red Green Blue) is a color representation that uses three channels to represent color values. Each channel represents a component of the color, with 0 being the minimum value and 255 being the maximum value. RGB representation is used in computer graphics, digital imaging, and other digital color applications.

Advantages of RGB:

    - Widely used and supported in various software and hardware systems.
    - Easy to understand and intuitive as it represents colors in terms of their red, green, and blue components.
    - A large color space, making it possible to produce a wide range of colors.

Disadvantages of RGB:

    - Can be sensitive to changes in lighting conditions, making it difficult to achieve consistent color matching across different environments.
    - Not perceptually uniform, meaning that a change in the intensity of one channel may result in a larger color change than a change in the intensity of another channel.

HSV (Hue Saturation Value) is another color representation that uses three channels to represent color values. In this representation, hue is used to represent the color type, saturation is used to represent the intensity of the color, and value is used to represent the brightness of the color.

Advantages of HSV:

    - More perceptually uniform than RGB, making it easier to compare colors in a meaningful way.
    - Provides a better representation of color information in low light conditions.
    - Better suited for color-based processing, such as color segmentation, than RGB.

Disadvantages of HSV:

    - Not as widely supported as RGB, making it more difficult to find compatible software and hardware systems.
    - More complex to understand than RGB as it uses different channels to represent color information.

3. Ultrasonic sensors have many positive and negative attributes. Name and describe three positive and three negative attributes.

Positive attributes:

    - Non-contact measurement: Ultrasonic sensors are capable of measuring the distance to an object without making physical contact. This eliminates the risk of damage to the sensor and the object being measured.

    - Immunity to light conditions: Ultrasonic sensors are not affected by light conditions, which makes them suitable for use in environments with variable lighting conditions.

    - High precision: Ultrasonic sensors are capable of measuring distances with high precision, making them ideal for applications where precise measurements are required.

Negative attributes:

    - Limited range: The range of ultrasonic sensors is limited, typically around 3 to 4 meters, which makes them unsuitable for long-range sensing applications.

    - Reflective surfaces: Ultrasonic sensors can be affected by reflective surfaces, causing false readings or even complete failure in some cases.

    - Environmental limitations: Ultrasonic sensors are susceptible to interference from dust, fog, or other environmental factors, which can reduce the accuracy of their measurements.

4. What is the difference between physical and logical redundancy?

    Physical redundancy refers to the use of multiple physical components to perform the same task in order to increase reliability. For example, a robot may have two motors that control the same wheel, so if one motor fails, the other can take over and keep the robot moving.

    Logical redundancy refers to the use of multiple software components to perform the same task, so if one component fails, another component can take over. For example, a robot may have multiple algorithms that perform the same task, so if one algorithm fails, another algorithm can be used instead.

    The key difference between physical and logical redundancy is that physical redundancy relies on multiple physical components to provide redundancy, while logical redundancy relies on multiple software components to provide redundancy. Physical redundancy is generally considered to be more reliable than logical redundancy, as it is less prone to software errors and is less susceptible to hacking.

5. Describe the three major problems of ultrasonic sensing, and define a hypothetical instance in which a robot would encounter each problem (such as a room with a large amount of glass surfaces).

The three major problems of ultrasonic sensing are:

    1. **Reflection**: Reflection occurs when ultrasonic waves hit a surface and bounce back. This can cause confusion for the sensor, as it may detect multiple reflections instead of the original target. A hypothetical instance in which a robot would encounter this problem would be in a room with large glass surfaces, where the waves could bounce back and forth between the walls and floor.

    2. **Absorption**: Absorption occurs when ultrasonic waves pass through a material and are partially absorbed by the material. This can cause the signal to weaken, making it harder for the sensor to detect objects. A hypothetical instance in which a robot would encounter this problem would be in a room with a lot of furniture made of soft materials, such as foam, which can absorb the ultrasonic waves.

    3. **Noise**: Noise refers to any unwanted signal that can interfere with the ultrasonic signal. This can be caused by a variety of factors, such as electrical interference, environmental noise, and mechanical vibration. A hypothetical instance in which a robot would encounter this problem would be in a busy factory, where machinery and other electrical equipment can generate a lot of electrical noise.

6. Describe with examples the three attributes that should be considered for an entire sensing suite.

The three attributes to be considered for an entire sensing suite are accuracy, reliability, and cost.

**Accuracy**: This refers to the ability of the sensors to measure the environment correctly. For example, if a robot needs to measure the distance between itself and an object, the accuracy of the ultrasonic sensor used for the task should be high.

**Reliability**: The sensors must work correctly and consistently. For example, a robot with a camera as a sensing suite must work under different lighting conditions and produce the same result.

**Cost**: The cost of the sensors is an important factor to consider, as the cost of the sensors may affect the overall cost of the robot. For example, a laser range finder may be more accurate than an ultrasonic sensor, but it may also be more expensive.v

7. Consider a Lego Mindstorms robot. Classify the available sensors for it in terms of modalities.

A Lego Mindstorms robot is equipped with various types of sensors that can be classified into the following modalities:

    Touch Sensors: The Lego Mindstorms robot has touch sensors that can detect when the robot is bumped or pressed. These sensors are used to detect physical contact with objects and are ideal for applications like line following or obstacle avoidance.

    Light Sensors: The Lego Mindstorms robot also has light sensors that can detect the amount of light in the environment. These sensors can be used to detect the presence of light or dark and are ideal for applications like line following or light tracking.

    Ultrasonic Sensors: The Lego Mindstorms robot has ultrasonic sensors that can detect objects using sound waves. These sensors can be used to detect the presence of obstacles and are ideal for applications like obstacle avoidance.

    Infrared Sensors: The Lego Mindstorms robot also has infrared sensors that can detect the presence of other Lego Mindstorms robots. These sensors can be used for communication between robots and are ideal for applications like cooperative robots.

    Overall, the Lego Mindstorms robot is equipped with a range of sensors that can be used for various applications, including line following, obstacle avoidance, light tracking, and communication between robots.

8. Describe the problems of specular reflection, cross talk, and foreshortening with an ultrasonic transducer.

Specular reflection is a problem in ultrasonic sensing where the sound waves are reflected directly off a smooth surface, like glass or metal, and do not scatter. This results in the loss of the returning echoes and leads to inaccurate distance measurements.

Cross talk occurs when the sound waves from one ultrasonic sensor interfere with the sound waves from another ultrasonic sensor. This results in incorrect readings from the sensors and can lead to false detections or the loss of important information.

Foreshortening occurs when the distance measurement between the ultrasonic transducer and the object is not accurate because of the limited beam width of the transducer. This can result in the underestimation of the actual distance between the robot and the object, leading to incorrect readings and dangerous collisions.

9.  List the metrics for rating individual sensors and a sensor suite, and apply these metrics to a particular application.

The metrics for rating individual sensors and a sensor suite include:

    Sensitivity: This refers to the ability of the sensor to detect small changes in the environment. This can be measured by the minimum detectable change in the target object or environmental condition.

    Accuracy: This refers to the ability of the sensor to measure the actual value of the target object or environmental condition. Accuracy can be measured by comparing the readings from the sensor to the actual value.

    Range: This refers to the maximum distance that the sensor can detect an object or environmental condition.

    Resolution: This refers to the smallest increment that can be detected by the sensor.

    Repeatability: This refers to the consistency of the readings from the sensor over time.

    Response time: This refers to the time it takes for the sensor to respond to changes in the environment.

    Cost: This refers to the monetary cost of purchasing and operating the sensor.

Applying these metrics to a particular application:

For example, consider an autonomous robot designed for agriculture. The sensor suite for this robot should be evaluated based on these metrics. The desired accuracy of soil moisture readings is high, so a high sensitivity and accuracy sensor is needed. The range of the sensor should be sufficient to cover the entire field, so a high range sensor is necessary. The resolution of the sensor should be sufficient to detect small changes in soil moisture, so a high resolution sensor is necessary. The repeatability of the readings from the sensor is important for consistent data, so a repeatable sensor is necessary. The response time of the sensor should be quick to respond to changes in soil moisture, so a fast response time sensor is necessary. The cost of the sensor should be reasonable and affordable for the intended use, so a cost-effective sensor is necessary.

10. An alternative to a Denning ring is to mount one or more sonars on a mast and turn the mast. Turning gives the robot a 360 coverage. Which do you think would be better, a fixed ring or a panning mast? Would a panning mast reduce problems of foreshortening, cross-talk, and specular reflection.

11. List and describe advantages and disadvantages of 3 different sensors, including one type of computer vision.

12. Describe all the different characteristics of sensors that must be evaluated when designing a sensor suite. In addition, give priorities for each to determine which you would consider to be the most and least important of these characteristics for a robot that was going to be designed for the 1994 AUVS Unmanned Ground Robotics Competition.

13. Pick a sensor suite that you think would do a good job if you were designing a robot for the 1995 UGV competition described in an earlier chapter. Explain what each sensor would do as well as describe the sensors and sensor suite in terms of the attributes listed in this chapter.

14. You are to design a sensor suite for a new robot for use by fire fighters. The robot is designed to seek out people in a smoke filled building. Keep in mind the following:

- Visibility is often very limited due to smoke.
- Heat can be both an attactive force (e.g. human) or repulsive (e.g. open flame).
- Obstacles may have a wide variety of sound absorbtion (e.g. carpeting or furniture) 

Describe the types of sensors that may be needed and how they will be used. Do not focus on how the robot moves around just on the sensors it will need to use. Extra credit: Comment on using simple voice recognition software and a microphone to seek out human voices (e.g., cries for help).

15. How are the concepts of logical sensors in robotics and polymorphism in objectoriented programming similar?

16. Define image function. What is the image function for
a. the left-right images in a stereo pair?
b. the depth map?

17.  What are two disadvantages of light stripers?

18.  Consider an obstacle avoidance behavior which consists of a perceptual schema that provides a polar plot of range and motor schema which directs the robot to the most open sector. List all the logical sensors covered in this chapter that can be used interchangeably for the perceptual schema. Which of these are logically redundant? Physically redundant?

19. Assume you had a mobile robot about 0.5 meters high and a planar laser range finder. What angle would you mount the laser at if the robot was intended to navigate

a. in a classroom?
b. in a hallway or reception area where the primary obstacle is people?
c. outdoors in unknown terrain?

State any assumptions your design is based on. Is there more information needed; if so, what?
20.  [Programming] Write your own code to give you the threshold of a small interleaved image.

21.  [World Wide Web] Search for Kludge, another robot built by Ian Horswill. Describe Kludge’s homemade whisker system and how well it works.

22. [Programming] Program a mobile robot to find and bump an orange tennis or soccer ball.

23. [Programming] Create a color histogram program. Construct the color histogram, E, for four different brightly colored objects, such as dolls of the South Park or the Simpsons cartoon characters. Present the program with a different image, I, of one of the characters and compute the histogram intersection with each of the four E. Does the highest match correctly identify the character? Why or why not?