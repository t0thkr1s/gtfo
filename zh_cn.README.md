# gtfo

[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://forthebadge.com/images/badges/built-with-love.svg)](https://gitHub.com/t0thkr1s/)

这是一个为[GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io)编写的Python脚本。
您可以搜索来绕过系统安全限制的Unix二进制文件，这些二进制文件可用于获得限制的shell提权，传输文件，生成绑定和反向外壳等等

这些功能来自[https://github.com/GTFOBins/GTFOBins.github.io](https://github.com/GTFOBins/GTFOBins.github.io)所有贡献都归功于各个的贡献者。在这里它们被简化（不需要环境变量）启用了高亮语法。

## 下载

```
git clone https://github.com/t0thkr1s/gtfo
```

## 安装

该脚本有2个依赖项：

*   [colorama](https://pypi.org/project/colorama/)
*   [pygments](https://pypi.org/project/Pygments/)

您可以通过键入以下命令来安装它们：

```
python3 setup.py install
```

## Run

```
python3 gtfo.py [binary]
```

## 屏幕截屏


屏幕截屏1             |  屏幕键盘2
:-----------------------:|:-----------------------:
![Screenshot1](https://i.imgur.com/1EzFiGQ.png)  |  ![Screenshot2](https://i.imgur.com/icgmDct.png)


### 免责声明

> 该工具仅用于测试和学习，并且只能在经过同意的情况下使用。请勿将其用于非法目的！所有的用户有义务遵守各地法律。开发人员对此工具和软件造成任何违法行和损失为我们不承担任何责任，也不会承担任何责任。

## 许可证

此项目已获得GPLv3许可-请参阅[LICENSE](LICENSE) 文件
