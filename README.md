A PaddleOCR-based numerical recognition project for extracting trajectory data from evacuation experiments using Minecraft.<br />We used the NetEase-represented Minecraft version and purchased a server to build the experiment platform, which could support up to 40 simultaneous participants. ([https://mc.163.com](https://mc.163.com)), Minecraft version 1.12.2 (Java version)
<a name="hLKaw"></a>
### **Experimental videos and data processing process**
<a name="Yitjy"></a>
#### 1. **Experimental videos**
<a name="RiUze"></a>
##### 1.1 **Researcher's view**
[2-2.mp4](https://www.yuque.com/attachments/yuque/0/2023/mp4/22618877/1682763678905-76ef7508-80b6-444f-b7f5-f745bea2efd0.mp4?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2023%2Fmp4%2F22618877%2F1682763678905-76ef7508-80b6-444f-b7f5-f745bea2efd0.mp4%22%2C%22name%22%3A%222-2.mp4%22%2C%22size%22%3A10139648%2C%22ext%22%3A%22mp4%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u71093e0c-c73a-48de-acc0-e2abba8deda%22%2C%22taskType%22%3A%22upload%22%2C%22type%22%3A%22video%2Fmp4%22%2C%22__spacing%22%3A%22both%22%2C%22mode%22%3A%22title%22%2C%22id%22%3A%22oQBHY%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)
[![2-2.mp4](https://gw.alipayobjects.com/mdn/prod_resou/afts/img/A*NNs6TKOR3isAAAAAAAAAAABkARQnAQ)]()<a name="LLhKq"></a>
##### 1.2 **Participant view**
[02-2-2.mp4](https://www.yuque.com/attachments/yuque/0/2023/mp4/22618877/1682763696957-e963960a-1e54-49a0-917b-34e9b612c8f9.mp4?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2023%2Fmp4%2F22618877%2F1682763696957-e963960a-1e54-49a0-917b-34e9b612c8f9.mp4%22%2C%22name%22%3A%2202-2-2.mp4%22%2C%22size%22%3A13401728%2C%22ext%22%3A%22mp4%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u22656892-044d-404b-a190-ea0ebb586a3%22%2C%22taskType%22%3A%22upload%22%2C%22type%22%3A%22video%2Fmp4%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u3bc19426%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)
[![02-2-2.mp4](https://gw.alipayobjects.com/mdn/prod_resou/afts/img/A*NNs6TKOR3isAAAAAAAAAAABkARQnAQ)]()<a name="J19kV"></a>
#### 2. **Data extraction**：
**he processing process of extracting coordinate data from experimental video is shown as follows:**<br />![处理流程2.png](https://cdn.nlark.com/yuque/0/2023/png/22618877/1682761807503-fbbed9e7-2f52-472e-8f41-5c9929bcebd2.png#averageHue=%237e7a73&clientId=u7d54e50b-0b2c-4&from=paste&height=902&id=ue904a193&originHeight=1804&originWidth=7628&originalType=binary&ratio=2&rotation=0&showTitle=false&size=3147110&status=done&style=none&taskId=u165f3cf0-2b8c-46e7-a8fe-f39a9a95d02&title=&width=3814)
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
The experiment uses two viewpoints to record the video, the participant uses the first-person viewpoint and the researcher uses the top-down viewpoint.<br />The participant's viewpoint (left) obtains the real-time coordinates of the character by calling the debugging interface, so the study can achieve accurate trajectory tracking by extracting the coordinate data<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/22618877/1682761282219-ffa2cb8e-7418-4674-b13e-3ad9f7d86279.png#averageHue=%231d6b79&clientId=u7d54e50b-0b2c-4&from=paste&height=285&id=ub5271d21&originHeight=470&originWidth=1332&originalType=binary&ratio=2&rotation=0&showTitle=false&size=872149&status=done&style=none&taskId=u77169f7e-a2c8-4639-96d6-a87cbbb926c&title=&width=807)
<a name="QWcts"></a>
#### 1.2 Coordinate extraction - implemented using the get_location module:

1. processing_video.py: Extracts each frame of the video
2. processing_pictures.py: capture the coordinate area in the picture
3. recognize_location.py: OCR recognition of coordinate values
4. merge.py: merge the coordinate data files of each person
5. relative_location.py: Calculate the relative coordinates of the person in the experiment
<a name="B9OiO"></a>
#### 2. Data processing

1. calculate_velocaty.py: Calculate the instantaneous velocity of each person in the experiment
2. draw_track: plot the experiment trajectory
3. remain_peo: calculate the number of people left in the room
<a name="Ufx7M"></a>
### Experimental process
<a name="IP2IE"></a>
#### 1.Interface settings
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
