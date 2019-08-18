# Captcha-Recognition-of-CSU-TchMngInfoSys
## 中南大学教务系统验证码识别，Keras实现。Captcha Recognition of Center South University's Teaching Manager Infomation System,based on Keras.
### 下面对各文件作用进行说明：
GetCaptchaJpg.py:爬取中南大学教务系统验证码图片代码；
CutCaptchaJpg.py:验证码图片预处理，包括灰度化，去除干扰线和切割；
PredictToMark.py：对切割后未预测图片进行分类。验证码训练集显然不可能全部手动标记，故采取先标记一小部分，使用少量样本训练模型，再用有一定准确率的模型帮助标记的方式标记样本；
CreateModel.py:根据训练集生成模型；
PredictCaptcha.py:使用已生成的模型预测从中南大学教务系统爬取的验证码图片；
PredictModel.h5:生成的预测模型：
CaptchaJpg.rar:从中南大学教务系统爬取的10000张验证码图片及其去除干扰线的灰度化；
set.rar:预处理后的分类完毕的图片，为模型重现提供训练集。
