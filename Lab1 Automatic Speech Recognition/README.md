## Lab1: Automatic Speech Recognition

###### 简易版语音助手 ---- mySiri

#### 背景介绍

当今，市面上有很多语音助手，讯飞、google、搜狗等很多大公司都相继推出了自己的语音助手服务和相应的API接口。使得我们可以很容易的使用其提供的接口进而构建自己的语音助手并实现些简单的功能。

<a name="功能介绍"></a>  

#### 功能介绍

1. "**Hey Siri**"以  *<u>唤醒语音助手</u>*
2. 起始页面中**双击底部**语音助手以查看  *<u>帮助说明</u>*
3. 唤醒Siri后:
   1. "**Play music**"以  *<u>播放音乐</u>*
   
   2. "**Open Notepad**"以  *<u>打开记事本</u>*
   
   3. "**Open the calculator**"以  *<u>打开计算器</u>*
   
      <a name="开发环境"></a>  

#### 开发环境

1. **PyCharm** *2019.1.1.PC-191.6605.12*
2. **Qt Designer** *v5.11.2.0*

> 引用块内容
>
> > SpeecnRecognition
> >
> > PocketSphinx
> >
> > PyAudio
> >
> > PyQt5
> >
> > pyqt5-tools

<a name="具体功能实现"></a>  

#### 具体功能实现

<a name="语音识别"></a>  

##### 1. 语音识别

通过麦克风检测用户的语音指令, 当无法检测到声音时自动停止, 并通过recognize_sphinx进行语音识别

```python
import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
command = r.recognize_sphinx(audio)
```

<a name="指令相似度匹配"></a>  

##### 2. 指令相似度匹配

通过string_similar进行指令相似度的匹配

- 唤醒过程: 用户command与"Hey Siri"的相似度大于0.1认为唤醒成功
  - 唤醒成功: 调用self.WakeSuccess(), 让用户输入希望执行的语音指令
  - 唤醒失败: 调用self.WakeFailed(), 定时器重新进行唤醒识别
- 指令识别过程: 将用户指令与四个预设指令分别进行字符换相似度匹配
  - 最大的匹配度小于0.2: 在屏幕上显示I guess you want to..., 并随机执行一个指令
  - 最大的匹配度大于0.2: 执行匹配度最高的指令

```python
import difflib

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

similar = string_similar(command, "Hey Siri")
print("The similar is ", similar)

if similar > 0.1:
    if self.flag == False:    # 如果此时正在看帮助信息则识别不成功
         self.WakeSuccess()
    else:
         self.WakeFailed()
    else:
         self.WakeFailed()
```

```python
list = [string_similar(command, "play music"),
        string_similar(command, "open notepad"),
        string_similar(command, "open the calculator")]

max_value = max(list)           	  # 最大值
max_index = list.index(max_value)     # 最大值的索引

if max_value < 0.2:
    print("I guess you want to...")
    max_index = random.randint(0, 2)
    self.label_12.setVisible(True)
    time.sleep(3)
    self.label_12.setVisible(False)
```

<a name="定时器"></a>  

##### 3. 定时器

- 通过threading.Timer(), start(), cancel(), 使用定时器

- 每5.1s进行一次唤醒识别

- 在用户查看帮助信息的时候停止定时器, 返回主页后重新打开定时器

```python
import threading, time

global timer
timer = threading.Timer(5.1, self.siri_recognition)
timer.start()
print("Time clock...")

# 关闭定时器
timer.cancel()
```

<a name="监听鼠标双击事件"></a>  

##### 4. 监听鼠标双击事件

- 在主页的时候, 用户可以双击底部的gif查看帮助信息

- 在进入帮助信息页面后, 可以双击同样的位置返回主页

- 当唤醒Kerr后, 双击不会进入帮助页面

```python
def mouseDoubleClickEvent(self, event):
    if self.label_10.isVisible()==True:     # 当语音助手已经被唤醒时, 取消双击事件 => 直接返回
         return

    self.label_7.setVisible(self.flag)
    self.label_8.setVisible(self.flag)

    global timer
    # 交替显示
    if self.flag == True:
        self.flag = False
        # 打开定时器
        timer = threading.Timer(0.1, self.siri_recognition)
        timer.start()
        print("==============Timer is start==============")
     else:
        self.flag = True
        # 关闭定时器
        timer.cancel()
        print("==============Timer is cancel==============")
```

<a name="调用系统接口,执行用户指令"></a>  

##### 5. 调用系统接口, 执行用户指令

- os.startfile()播放音乐
- os.system()打开记事本
- os.system()打开计算器

```python
if max_index == 0:
   os.startfile(r"Resources\music\music.mp3")
elif max_index == 1:
   os.system("C:\\Windows\\System32\\notepad.exe")
elif max_index == 2:
   os.system("C:\\Windows\\System32\\calc.exe")
```

<a name="功能实现截屏显示"></a>  

