# Yooou
Yooou是一套由Python编写的家庭中控系统，当前运行在树莓派中。系统使用Python2.7作为python运行环境。系统由以下几部分构成。

~~1.显示模块。通过flask搭建web显示。~~

~~2.API模块。为不同的设备，硬件提供访问和控制接口。~~

~~3.module模块。这个模块是主要种功能的实现。~~

#### 音乐播放功能实现
通过调用百度开放的APi获取音乐地址，使用mpg123作为播放器播放。

整个播放器控制模式采用，豆瓣电台/百度电台的方式。

播放器最新版本：v20170217

v20170217
* 播放界面显示（Flask+nginx）
* 实现音乐播放功能
* 下一曲功能
* 停止功能
* 切换频道

#### 获取天气预报信息
通过获取百度、新浪、国家气象局的天气信息，进行对比。然后在早上上班前，或者起床的时候，语音
提示穿衣服，带雨伞等等信息。

#### 闹铃功能
更具我们两个人上班作息时间表，智能的制定闹铃计划。

#### TODO功能
代办事项提示，对在某个时间或者某个时间段需要完成的事情，做一个烦人的提示

#### 重要日期提示功能
对生日，节日问候等做一个提示。考虑通过手机APP控制短信群发等，或者通过微信群发自定义的祝福信息。

#### 社会关系维护
对社会关系档案进行管理，对每一个人的亲密度进行分析。让后智能的提示我们去维护这个亲密度。

