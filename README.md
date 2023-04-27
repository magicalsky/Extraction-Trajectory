Experimental research project on pedestrian evacuation using Minecraft.<br />We used the NetEase-represented Minecraft version and purchased a server to build the experiment platform, which could support up to 40 simultaneous participants. ([https://mc.163.com](https://mc.163.com)), Minecraft version 1.12.2 (Java version)<br />If you want to test, you can search for the rental service game by server number within the launcher: xxx, room password: 123456

<a name="Wnvtp"></a>
### Getting Start
Clone this project. This is the logical code for MCTrack to extract data and calculate relative coordinates, containing the functions:
> 1. Extracting coordinate data
> 2. Calculate relative coordinates
> 3. Merge coordinate files
> 4. Calculate pedestrian velocity
> 5. Plot trajectory
> 6. Calculate the number of people remaining in the room

<a name="r54c7"></a>
### Prerequisites

1. Install PaddlePaddle and build a deep learning environment([https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html))
> python -m pip install paddlepaddle-gpu==2.4.2 -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)

2. Install PaddleOCR and build OCR service
> pip install paddleocr

<a name="ScNgj"></a>
### Instructions
<a name="Kz840"></a>
#### 1. Extracting coordinate data
<a name="umoRI"></a>
#### 1.1 Introduction to the experimental video
The experiment uses two viewpoints to record the video, the participant uses the first-person viewpoint and the researcher uses the top-down viewpoint.<br />The participant's viewpoint (left) obtains the real-time coordinates of the character by calling the debugging interface, so the study can achieve accurate trajectory tracking by extracting the coordinate data<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/22618877/1681627759520-d826b906-38f8-464d-aa2e-722c863a3cc9.png#averageHue=%231c6a77&clientId=u07c89d2b-a828-4&from=paste&height=321&id=uedd0a988&originHeight=321&originWidth=906&originalType=binary&ratio=1&rotation=0&showTitle=false&size=571284&status=done&style=none&taskId=u4fcf20dd-c2d8-4dfd-a63b-be52e368641&title=&width=906)
<a name="QWcts"></a>
#### 1.2 Coordinate extraction - implemented using the get_location module:

1. processing_video.py: Extracts each frame of the video
2. processing_pictures.py: capture the coordinate area in the picture
3. recognize_location.py: OCR recognition of coordinate values
4. merge.py: merge the coordinate data files of each person
5. relative_location.py: Calculate the relative coordinates of the person in the experiment

![image.png](https://cdn.nlark.com/yuque/0/2023/png/22618877/1681629880208-449eeb92-a20f-4b04-a00b-22bc120b1891.png#averageHue=%233e3125&clientId=u07c89d2b-a828-4&from=paste&height=892&id=u03f12de6&originHeight=892&originWidth=800&originalType=binary&ratio=1&rotation=0&showTitle=false&size=330141&status=done&style=none&taskId=uf48a17de-277c-4b93-a679-9f71ef1be51&title=&width=800)
<a name="B9OiO"></a>
#### 2. Data processing

1. calculate_velocaty.py: Calculate the instantaneous velocity of each person in the experiment
2. draw_track: plot the experiment trajectory
3. remain_peo: calculate the number of people left in the room
<a name="Ufx7M"></a>
### Experimental process
<a name="IP2IE"></a>
#### 1. Interface settings
Please maximize the game interface<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/22618877/1669187627058-e39e0010-a3d8-4536-9a45-3bc1c1b1211f.png#averageHue=%233a4641&clientId=ufd09b4ab-7a15-4&from=paste&height=557&id=J9JCI&originHeight=1080&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=382954&status=done&style=stroke&taskId=u62ee0892-b942-4213-bbc5-83a3219674b&title=&width=990)
<a name="w2Ycg"></a>
#### 2. Debugging information acquisition
Press F3 to open the debug interface and get the game background data. The video display is set to auto, which enables the debug information to be displayed in a larger font.<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/22618877/1650016789599-03719b1f-3446-4110-ada8-ae5a1b685338.png#averageHue=%23495d31&clientId=uc159d2c6-a042-4&from=paste&height=541&id=M62AM&originHeight=1017&originWidth=1916&originalType=binary&ratio=1&rotation=0&showTitle=false&size=591657&status=done&style=none&taskId=u378a929f-54bd-4d73-98ba-eed8d4be39b&title=&width=1020)
<a name="QwjN4"></a>
#### 3. Pedestrian movement
Use the WASD keys on the keyboard to control the movement of the character, the mouse to control the direction, and stop the recording screen after leaving the room through the exit.
<a name="sPx4m"></a>
### Appendix: Recognition Model Training
If your coordinate value recognition is not accurate, you may need to use PaddleOCR training data, which requires cloning the PaddleOCR project ([https://github.com/PaddlePaddle/PaddleOCR).](https://github.com/PaddlePaddle/PaddleOCR).) Image annotation can be done using PaddleLable, a semi-automatic annotation tool provided by PaddleOCR.
> python PPOCRLabel.py 

![image.png](https://cdn.nlark.com/yuque/0/2023/png/22618877/1681630556708-b37239fd-ff83-4589-bc2d-1598fd3fd15d.png#averageHue=%23f0f0ef&clientId=u07c89d2b-a828-4&from=paste&height=844&id=ucd064da5&originHeight=844&originWidth=1247&originalType=binary&ratio=1&rotation=0&showTitle=false&size=87262&status=done&style=none&taskId=u6516ba06-7524-4054-8052-4f8bcaa4d7c&title=&width=1247)
