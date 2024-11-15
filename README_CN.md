# Xin-anjiang-Model | 新安江模型

[English Version](./README.md) | [中文版](./README_CN.md)

[新安江模型](https://baike.baidu.com/item/%E6%96%B0%E5%AE%89%E6%B1%9F%E6%A8%A1%E5%9E%8B/8901233)是华东水利学院(现河海大学)赵人俊教授团队提出的一个水文模型，是中国少有的一个具有世界影响力的水文模型。新安江模型是集总式水文模型（划分子流域时成为分散式水文模型），可用于湿润地区与半湿润地区的湿润季节。当流域面积较小时(按照经验决定面积大小，比如50平方公里)，新安江模型采用集总模型，当面积较大时，采用分散模型。它把全流域分为许多块水文响应单元（HRU），对每个单元流域作产汇流计算，得出单元流域的出口流量过程。再进行出口以下的河道洪水演算，求得流域出口的流量过程。把每个单元流域的出流过程相加，就求得了流域的总出流过程。

## 版本要求
 - python >=3.8 
 - pandas
## 安装
 执行`git clone`命令以下载本项目，然后`python pyXinAnJiang.py`即可获得执行结果。
## 文件说明
 - PEdata.xlsx 降雨、蒸发，数据文件。 
 - pyXinAnJiang.py 源代码文件