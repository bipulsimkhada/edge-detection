# Edge Detection
## Description
In this project, I have used different types of edge operators of my own trying to mimic the behavior of simple cells. The threshold for the edge has been set to 25 pixels. For detecting the edges, the input image is convolved with the edge operator with a threshold applied to result in the image with the edge detected. In addition, I have compared the resulting image from my own edge detector to the Kirsch operator, Prewitt compass, and Laplacian.  
 
## Libraries 
* numpy
* PIL - Image
* matplotlib
* os

## Tool
* Python IDE

## Method
#### 1.	Input Image:
As an example, a picture of the Statue of Liberty is used and has been converted into grayscale before applying edge operators. 

<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/statue%20of%20liberty.png">


#### 2.	Own Edge Operator:
For my edge operator, I have used a 3X3 matrix with operators focusing on the center. 

<img src="https://raw.githubusercontent.com/bipulsimkhada/Image/main/edge%20detection/edge%20operator.png">
The image is convolved with the edge operator and is normalized with the factor of 10 and further normalized to 0-255 for proper formatting of the pixel values in the image. We used the threshold for the edge to be around 10% (25 pixels). <br> <br>

The superimposed image generated after applying the edge operator is:

<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/eo%20sol.png">

#### 3.	Kirsch Operator:
The Kirsch Operators are given by the below matrices: 

<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/kirsch.png">
The comparison of edge detection of my edge operator to the Kirsch Operator is shown in the picture below.

<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/kirsch%20compare.png">

#### 4.	Prewitt Compass:
The edge operator matrices for Prewitt Compass are given by:

<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/Prewitt%20Compass.png">

Below is the comparison of the input image, my edge operator result, and Prewitt Compass:
<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/Prewitt%20Compass%20compare.png">


#### 5. Laplacian:
The edge operator matrices for Laplacian is given by:

<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/Laplacian.png">

Below is the comparison of the input image, my edge operator result, and Prewitt Compass:
<img src="https://github.com/bipulsimkhada/Image/blob/main/edge%20detection/Laplacian%20compare.png">

