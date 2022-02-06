Real Cascade U-Nets for Anime Image Super Resolution

Just a simple cli wrapper for personal usage, project origin repo https://github.com/bilibili/ailab
-------------------------------------------

[中文](README.md) **|** [English](README_EN.md)


:fire: **Real-CUGAN**:fire: 是一个使用百万级动漫数据进行训练的，结构与Waifu2x兼容的通用动漫图像超分辨率模型。它支持**2x\3x\4x**倍超分辨率，其中2倍模型支持4种降噪强度与保守修复，3倍/4倍模型支持2种降噪强度与保守修复。

**Real-CUGAN** 为windows用户打包了一个可执行环境，未来将支持GUI。

### 1. 效果对比


https://user-images.githubusercontent.com/61866546/147812864-52fdde74-602f-4f64-ac05-4d34cc58aa79.mp4


- **效果图对比**(推荐点开大图在原图分辨率下对比)
  <br>
  纹理挑战型(注意地板纹理涂抹)(图源:《侦探已死》第一集10分20秒)
  ![compare1](demos/title-compare1.png)
  线条挑战型(注意线条中心与边缘的虚实)(《东之伊甸》第四集7分30秒)
  ![compare2](demos/compare2.png)
  极致渣清型(注意画风保留、杂线、线条)(图源:Real-ESRGAN官方测试样例)
  ![compare3](demos/compare3.png)
  景深虚化型(蜡烛为后景，刻意加入了虚化特效，应该尽量保留原始版本不经过处理)(图源:《～闘志の華～戦国乙女2ボナ楽曲PV》第16秒)
  ![compare4](demos/compare4.png)
- **详细对比**

|                | Waifu2x(CUNet)                                               | Real-ESRGAN(Anime6B)                                         | Real-CUGAN                                              |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 训练集         | 私有二次元训练集，量级与质量未知                             | 私有二次元训练集，量级与质量未知                             | 百万级高清二次元patch dataset                                |
| 推理耗时(1080P)    | Baseline                                                     | 2.2x                                                         | 1x                                                           |
| 效果(见对比图) | 无法去模糊，artifact去除不干净                               | 锐化强度最大，容易改变画风，线条可能错判，<br />虚化区域可能强行清晰化 | 更锐利的线条，更好的纹理保留，虚化区域保留                   |
| 兼容性         | 大量windows-APP使用，VapourSynth支持，<br />Caffe支持，PyTorch支持，NCNN支持 | PyTorch支持，VapourSynth支持，NCNN支持                       | 同Waifu2x，结构相同，参数不同，与Waifu2x无缝兼容             |
| 强度调整       | 仅支持多种降噪强度                                           | 不支持                                                       | 已完成4种降噪程度版本和保守版，未来将支持调节不同去模糊、<br />去JPEG伪影、锐化、降噪强度 |
| 尺度           | 仅支持1倍和2倍                                               | 仅支持4倍                                                    | 已支持2倍、3倍、4倍，1倍训练中              |


### 3. Waifu2x-caffe玩家

#### 我们目前为waifu2x-caffe玩家提供了两套参数：
:fire: **Real-CUGAN2x标准版(denoise-level3)** 和 :fire: **Real-CUGAN2x无切割线版**

:heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark: 由于waifu2x-caffe的切割机制，对于标准版，crop_size应该尽量调大，否则可能造成切割线。如果**发现出现切割线，** 请移步下载windows应用，它支持无切割线痕迹的crop(tile_mode），既能有效降低显存占用需求，crop也是无损的。或者使用我们额外提供的无切割线版，它会造成更多的纹理涂抹和虚化区域清晰化。

>开发者可以很轻松地进行适配，推荐使用整张图像作为输入。如果顾及显存问题，建议基于PyTorch版本进行开发，使用tile_mode降低显存占用需求。


### 4. Python玩家
环境依赖 <br>
:white_check_mark:  **torch>=1.0.0**      <br>
:white_check_mark:  **numpy**             <br>
:white_check_mark:  **opencv-python**     <br>
:white_check_mark:  **moviepy**           <br>
upcunet_v3.py:模型+图像推理 <br>
inference_video.py:一个简单的使用Real-CUGAN推理视频的脚本

### 5. VapourSynth玩家
移步[Readme](VapourSynth/README.md)

### 6.:european_castle: Model Zoo

可在网盘路径下载完整包与更新参数包获取各模型参数。

<table>
	<tr>
	    <th align="center"></th>
        <th align="center">1倍</th>
	    <th align="center">2倍</th>
	    <th align="center">3倍/4倍</th>  
	</tr >
	<tr>
	    <td align="center" >降噪程度</td>
	    <td align="center">仅支持无降噪，训练中</td>
	    <td align="center">现支持无降噪/1x/2x/3x</td>
        <td align="center">现支持无降噪/3x，1x/2x训练中</td>
	</tr>
	<tr>
	    <td  align="center">保守模型</td>
	    <td  align="center">训练中</td>
	    <td  colspan="2" align="center">已支持</td>
	</tr>
	<tr>
        <td  align="center">快速模型</td>
	    <td  colspan="3" align="center">调研中</td>
	</tr>
</table>

### 7. TODO：
- [ ]  快速模型，提高推理速度，降低显存占用需求
- [ ]  可调整的增强锐度，降噪强度，去模糊强度
- [ ]  一步超到任意指定分辨率
- [ ]  优化纹理保留，削减模型处理痕迹
- [ ]  简单的GUI

:stuck_out_tongue_closed_eyes: 欢迎各位大佬在**issue**:innocent: 进行留言,提出各种建议和需求:thumbsup: ! 

### 8. 感谢
这里不公开训练代码，训练步骤参考了但不局限于 :star2: [RealESRGAN](https://github.com/xinntao/Real-ESRGAN/blob/master/Training.md):star2: . 想自行训练的请移步该仓库。<br>

模型结构魔改自Waifu2x官方:star2: [CUNet](https://github.com/nagadomi/nunif/blob/master/nunif/models/waifu2x/cunet.py):star2: .



