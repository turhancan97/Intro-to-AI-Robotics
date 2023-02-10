# Exercises - Chapter 6

## Common Sensing Techniques for Reactive Robots

---

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

It depends on the specific application and requirements of the robot.

A fixed ring of sonars provides a continuous and stable measurement of the environment, allowing the robot to perceive its surroundings even when it is moving. This is useful for navigation and mapping tasks.

A panning mast, on the other hand, provides the ability to rotate the sonars and scan the environment, providing a wider range of coverage. This is useful in situations where the robot needs to survey a large area and gather more detailed information about its surroundings.

In terms of reducing problems of foreshortening, cross-talk, and specular reflection, a panning mast may help to mitigate these problems by providing a more controlled and isolated measurement of the environment. However, the mast must be carefully designed and the scanning must be done at a slow and controlled rate to minimize the potential for these problems.

Ultimately, the best solution will depend on the specific requirements and constraints of the application.

11. List and describe advantages and disadvantages of 3 different sensors, including one type of computer vision.

**Infrared Sensors:**
    Advantages:
        Low cost
        Simple and easy to use
        Can be used in environments where light is not present
    Disadvantages:
        Can be affected by dust, rain or other environmental conditions
        Limited range
        Poor accuracy in identifying objects

**LIDAR Sensors:**
    Advantages:
        High accuracy
        Can detect objects from a distance
        Can map the environment in real time

    Disadvantages:
        Expensive
        Large size
        Can be affected by the environment (e.g. fog or rain)

**Computer Vision (RGB Cameras):**
    Advantages:
        High accuracy in identifying objects and shapes
        Can recognize colors and patterns
        Can be used for navigation
  
    Disadvantages:
        Can be affected by lighting conditions
        Computationally expensive
        Can be vulnerable to glare or reflection from shiny surfaces.

12. Describe all the different characteristics of sensors that must be evaluated when designing a sensor suite. In addition, give priorities for each to determine which you would consider to be the most and least important of these characteristics for a robot that was going to be designed for the 1994 AUVS Unmanned Ground Robotics Competition.

When designing a sensor suite for a robot, there are several characteristics that must be evaluated to ensure the most effective and efficient performance. The most important characteristics include:

    Range: The maximum distance at which the sensor can detect an object or environment feature.

    Accuracy: The degree of precision with which the sensor can measure the distance, position, or orientation of an object or environment feature.

    Resolution: The smallest change in distance, position, or orientation that can be detected by the sensor.

    Sensitivity: The ability of the sensor to detect small changes in distance, position, or orientation.

    Latency: The time delay between the sensor receiving a signal and producing an output.

    Field of View: The area of the environment that can be detected by the sensor at a given time.

    Cost: The monetary cost of the sensor and its components.

For the 1994 AUVS Unmanned Ground Robotics Competition, range and accuracy would likely be considered the most important characteristics for a sensor suite. This is because the robot would need to accurately detect the white line on the ground, as well as any obstacles, in order to complete the competition tasks. Resolution and sensitivity would also be important in order to accurately detect small changes in the environment. Latency would not be as critical for this competition, but it should still be considered to ensure a timely response from the robot. Field of view and cost would also need to be taken into account, as the robot would need a wide field of view to navigate the competition course, but also a cost-effective solution to ensure the feasibility of the project.

13. Pick a sensor suite that you think would do a good job if you were designing a robot for the 1995 UGV competition described in an earlier chapter. Explain what each sensor would do as well as describe the sensors and sensor suite in terms of the attributes listed in this chapter.

In designing a robot for the 1995 UGV competition, a sensor suite that would be suitable for the task is a combination of various sensors such as:

    Lidar sensor - This sensor would be used for mapping the environment and for detecting obstacles. The Lidar sensor emits laser beams and measures the time it takes for the beams to bounce back to determine the distance between the robot and objects in its environment.

    Ultrasonic sensors - Ultrasonic sensors would be used for detecting obstacles and for determining the distance between the robot and objects in its environment. These sensors emit high frequency sound waves and measure the time it takes for the waves to bounce back to determine the distance between the robot and objects in its environment.

    Camera sensor - This sensor would be used for computer vision and for identifying objects. The camera sensor would capture images of the environment and the robot would use computer vision algorithms to analyze these images and identify objects in its environment.

The sensor suite would be evaluated based on the following attributes:

    Accuracy - This attribute refers to the ability of the sensors to accurately measure the distance between the robot and objects in its environment.

    Range - This attribute refers to the maximum distance that the sensors can detect objects.

    Sensitivity - This attribute refers to the ability of the sensors to detect objects accurately at different distances.

    Reliability - This attribute refers to the ability of the sensors to provide consistent and accurate measurements over time.

    Cost - This attribute refers to the cost of purchasing and maintaining the sensors.

In terms of priorities, accuracy would be considered the most important attribute for a robot designed for the 1995 UGV competition, followed by range, sensitivity, reliability, and cost.

14. You are to design a sensor suite for a new robot for use by fire fighters. The robot is designed to seek out people in a smoke filled building. Keep in mind the following:

- Visibility is often very limited due to smoke.
- Heat can be both an attactive force (e.g. human) or repulsive (e.g. open flame).
- Obstacles may have a wide variety of sound absorbtion (e.g. carpeting or furniture) 

Describe the types of sensors that may be needed and how they will be used. Do not focus on how the robot moves around just on the sensors it will need to use. Extra credit: Comment on using simple voice recognition software and a microphone to seek out human voices (e.g., cries for help).

    To design a sensor suite for a fire fighting robot, the following sensors would be necessary:

    Infrared sensors: These sensors can detect heat sources, which would be useful in finding people in a smoke filled building. The sensors can also detect open flames and high temperature objects, which would help the robot to avoid dangerous situations.

    LIDAR (Light Detection and Ranging): LIDAR sensors can help the robot navigate in low visibility conditions, such as in smoke filled buildings. The sensors emit laser beams and use the reflection to create a 3D map of the environment. This information can be used to help the robot avoid obstacles and find the way to its target.

    Ultrasonic sensors: Ultrasonic sensors can detect the distance to objects and help the robot to navigate around obstacles. They are useful in finding people in a smoke filled building as they can detect the presence of objects, even if they are not visible.

    Microphone: A microphone can be used in conjunction with voice recognition software to detect human voices. This can help the robot to locate people who are calling for help. However, this method is not reliable as it is dependent on the clarity of the voice and the level of ambient noise.

    Overall, the combination of these sensors can provide the robot with the information it needs to navigate in a smoke filled building, locate people, and avoid dangerous situations. The sensors need to be designed and placed in a way that maximizes their effectiveness and provides the robot with a comprehensive understanding of its environment.

15. How are the concepts of logical sensors in robotics and polymorphism in object oriented programming similar?

Both logical sensors in robotics and polymorphism in object oriented programming refer to the ability to handle multiple different types of inputs in a flexible and adaptable manner. Logical sensors in robotics refer to sensors that interpret the data they receive and categorize it based on certain criteria, allowing the robot to respond in an appropriate manner. Similarly, polymorphism in object-oriented programming allows objects to be treated as objects of their base class or any of its derived classes, making it possible to write code that can work with multiple types of objects in a flexible way. Both concepts are about creating more general and versatile systems that can handle multiple types of inputs, and both aim to make it easier to write code that can handle different situations in an adaptable and flexible way.

16. Define image function. What is the image function for a. the left-right images in a stereo pair? b. the depth map?

The image function in robotics refers to the mathematical representation of the image data obtained by the robot's sensors.

a. The image function for the left-right images in a stereo pair is usually represented as a two-dimensional array, with each pixel representing a specific point in the image. In a stereo pair, the left and right images are related through the stereo geometry and can be used to calculate the depth information of the objects in the scene.

b. The depth map is a two-dimensional representation of the depth information of the scene, where each pixel represents the depth value of a specific point in the scene. The depth map can be obtained through various methods such as stereo triangulation, structured light, or laser rangefinding. The image function for the depth map is usually represented as a matrix, where each element represents the depth value of a specific point in the scene.

17.   What are two disadvantages of light stripers?

**Limited Field of View:** Light stripe sensors have a limited field of view, typically only covering a small area in front of the sensor. This can make it difficult for the sensor to detect objects that are outside of its field of view.

**Sensitivity to Interference:** Light stripe sensors are often susceptible to interference from other light sources, such as bright sunlight or flickering lights. This can cause the sensor to produce false readings, making it difficult to accurately detect objects in the environment.

18.  Consider an obstacle avoidance behavior which consists of a perceptual schema that provides a polar plot of range and motor schema which directs the robot to the most open sector. List all the logical sensors covered in this chapter that can be used interchangeably for the perceptual schema. Which of these are logically redundant? Physically redundant?

The logical sensors that can be used interchangeably for the perceptual schema in an obstacle avoidance behavior include ultrasonic sensors, infrared sensors, laser range finders, stereo vision, and Time of Flight cameras.

Of these, ultrasonic sensors and infrared sensors are logically redundant as they both provide range information. Laser range finders and Time of Flight cameras are also logically redundant as they both provide range information using light-based technologies. Stereo vision can be used as an alternative to these sensors as it provides range information based on the disparity between two images.

In terms of physical redundancy, having multiple ultrasonic sensors or multiple infrared sensors in different locations on the robot can provide physical redundancy. The same is true for having multiple laser range finders or multiple Time of Flight cameras. The use of stereo vision also provides physical redundancy as it requires two cameras to be mounted in different locations on the robot.

19. Assume you had a mobile robot about 0.5 meters high and a planar laser range finder. What angle would you mount the laser at if the robot was intended to navigate a. in a classroom? b. in a hallway or reception area where the primary obstacle is people? c. outdoors in unknown terrain? State any assumptions your design is based on. Is there more information needed; if so, what?

A. For a classroom, the laser range finder would need to be mounted at a low angle, around 20-30 degrees, to ensure that it can detect obstacles close to the ground, such as furniture and people's feet.

B. For a hallway or reception area, the laser range finder would need to be mounted at a slightly higher angle, around 40-50 degrees, to detect people and obstacles at a higher height, such as shoulders and heads.

C. For outdoors in unknown terrain, the laser range finder would need to be mounted at a higher angle, around 60-70 degrees, to detect obstacles at a further distance, such as trees, rocks, and buildings.

Assumptions:

The laser range finder has a range of at least 2 meters.
The robot moves at a relatively slow speed in these environments.
Additional information needed:

The maximum and minimum range of the laser range finder
The field of view of the laser range finder
The type of environment (indoor or outdoor) and any other physical or environmental constraints.

20.  [Programming] Write your own code to give you the threshold of a small interleaved image.


```C
#include <stdio.h>
#include <stdlib.h>

#define ROWS 3
#define COLS 3
#define THRESHOLD 128

int main() {
  int image[ROWS][COLS] = {{100, 200, 150},
                           {50, 125, 75},
                           {150, 100, 200}};

  int i, j;
  for (i = 0; i < ROWS; i++) {
    for (j = 0; j < COLS; j++) {
      if (image[i][j] < THRESHOLD) {
        printf("0 ");
      } else {
        printf("1 ");
      }
    }
    printf("\n");
  }

  return 0;
}
```
This code creates a 3x3 interleaved image stored in the image array. The threshold is set to 128, and the program loops through each element in the image array and compares it to the threshold. If the element is less than the threshold, the program prints "0", otherwise it prints "1". The output of this code will be:

```
0 1 0 
0 0 0 
1 0 1 
```

21.  [World Wide Web] Search for Kludge, another robot built by Ian Horswill. Describe Kludge’s homemade whisker system and how well it works.

- No answer

22. [Programming] Program a mobile robot to find and bump an orange tennis or soccer ball.

```python
import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture(0)

# Set the lower and upper bounds for orange color
lower_bound = np.array([10, 100, 100])
upper_bound = np.array([25, 255, 255])

while True:
    # Capture the frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the image to get only the orange color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Find the contours in the image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours
    for c in contours:
        # Get the center of the contour
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # Check if the contour is large enough to be considered as the ball
        if cv2.contourArea(c) > 1000:
            # Draw a circle around the ball
            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

    # Show the result
    cv2.imshow("Result", frame)
    
    # Bump the ball
    # Add your code here

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()
```


23. [Programming] Create a color histogram program. Construct the color histogram, E, for four different brightly colored objects, such as dolls of the South Park or the Simpsons cartoon characters. Present the program with a different image, I, of one of the characters and compute the histogram intersection with each of the four E. Does the highest match correctly identify the character? Why or why not?

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

def color_histogram(image, bins):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Split the channels into hue, saturation, and value
    hue, saturation, value = cv2.split(hsv)
    # Calculate the histogram of hue channel
    hist = cv2.calcHist([hue], [0], None, [bins], [0, 180])
    return hist

def histogram_intersection(hist1, hist2):
    # Calculate the histogram intersection between two histograms
    min_values = np.minimum(hist1, hist2)
    intersection = np.sum(min_values)
    return intersection

# Load four images of brightly colored objects
object1 = cv2.imread('object1.jpg')
object2 = cv2.imread('object2.jpg')
object3 = cv2.imread('object3.jpg')
object4 = cv2.imread('object4.jpg')

# Calculate the color histograms for each object
bins = 180
hist1 = color_histogram(object1, bins)
hist2 = color_histogram(object2, bins)
hist3 = color_histogram(object3, bins)
hist4 = color_histogram(object4, bins)

# Load the image to be identified
image = cv2.imread('image.jpg')

# Calculate the histogram for the image
hist_image = color_histogram(image, bins)

# Calculate the histogram intersection between the image histogram and each object histogram
intersection1 = histogram_intersection(hist_image, hist1)
intersection2 = histogram_intersection(hist_image, hist2)
intersection3 = histogram_intersection(hist_image, hist3)
intersection4 = histogram_intersection(hist_image, hist4)

# Find the highest match
highest_match = max(intersection1, intersection2, intersection3, intersection4)

# Determine the identity of the object
if highest_match == intersection1:
    print("The object is object1")
elif highest_match == intersection2:
    print("The object is object2")
elif highest_match == intersection3:
    print("The object is object3")
else:
    print("The object is object4")
```

In this code, we first convert the image to HSV color space using the cv2.cvtColor function. The HSV color space is used because it separates the color information (hue) from the brightness and saturation information. The hue channel is used to calculate the color histogram as it gives us information about the color distribution in the image.