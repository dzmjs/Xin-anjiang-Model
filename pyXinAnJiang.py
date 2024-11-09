# 三层蒸发蓄满产流模型（新安江模型）python计算程序
import pandas as pd

wum, wlm, wdm = 15, 85, 20  # 上层土壤蓄水容量、下层土壤蓄水容量、深层土壤蓄水容量
wm = wum + wlm + wdm  # 流域土壤平均蓄水容量
wu0, wl0, wd0 = 0, 2.2, 20  # 上层土壤蓄水量初值、下层土壤蓄水量初值、深层土壤蓄水量初值
w0 = wu0 + wl0 + wd0  # 流域平均土壤蓄水量初值
b, k, c = 0.3, 0.95, 0.14  # 流域不均匀系数、蒸发折算系数、蒸发扩散系数
wmm = wm * (1 + b)  # 最大土壤蓄水容量
filename = './PEdata.xlsx'
pedata = pd.read_excel(filename, sheet_name='Sheet1')  # 读取excel数据：时间、蒸发能力、降水
timelen = pedata.shape[0]  # 时段数，即数据行数(不包含表头）
t = list(pedata.iloc[:, 0])  # 日期
ep = list(pedata.iloc[:, 1])  # 日蒸发能力
p = list(pedata.iloc[:, 2])  # 日降水量
eu = [0] * timelen  # 上层蒸发
el = [0] * timelen  # 下层蒸发
ed = [0] * timelen  # 深层蒸发
e = [0] * timelen  # 日蒸发量
pe = [0] * timelen  # 扣除降水的蒸发量
dw = [0] * timelen  # 日土壤蓄水变量
r = [0] * timelen  # 产流
wu = [0] * (timelen + 1)  # 上层蓄水量
wl = [0] * (timelen + 1)  # 下层蓄水量
wd = [0] * (timelen + 1)  # 深层蓄水量
w = [0] * (timelen + 1)  # 日蓄水量
wu[0] = wu0
wl[0] = wl0
wd[0] = wd0
w[0] = w0
a = [0] * timelen  # 蓄满产流模型参数A
a[0] = wmm * (1 - (1 - w0 / wm) ** (1 / (1 + b)))
for i in range(timelen):
    if wu[i] + p[i] >= ep[i]:  # 计算eu
        eu[i] = ep[i]
    else:
        eu[i] = p[i] + wu[i]

    if p[i] + wu[i] >= ep[i]:  # 计算el
        el[i] = 0
    else:
        if wl[i] >= c * wlm:
            el[i] = (ep[i] - eu[i]) * wl[i] / wlm
        else:
            if wl[i] >= c * (ep[i] - eu[i]):
                el[i] = c * (ep[i] - eu[i])
            else:
                el[i] = wl[i]
    if wu[i] + p[i] < ep[i]:  # 计算ed
        if wl[i] < c * (ep[i] - eu[i]):
            ed[i] = c * (ep[i] - eu[i]) - el[i]
        else:
            ed[i] = 0
    else:
        ed[i] = 0
    e[i] = eu[i] + el[i] + ed[i]  # 计算e
    pe[i] = p[i] - e[i]  # 计算pe
    if pe[i] > 0:  # 计算r
        a[i] = wmm * (1 - (1 - w[i] / wm) ** (1 / (1 + b)))
        if a[i] + pe[i] < wmm:
            r[i] = pe[i] - (wm - w[i]) + wm * (1 - (a[i] + pe[i]) / wmm) ** (1 + b)
        else:
            r[i] = pe[i] - (wm - w[i])
    else:
        r[i] = 0
    dw[i] = pe[i] - r[i]  # 计算dw
    if dw[i] + wu[i] > wum:  # 计算wu
        wu[i + 1] = wum
    else:
        if dw[i] + wu[i] > 0:
            wu[i + 1] = dw[i] + wu[i]
        else:
            wu[i + 1] = 0
    if dw[i] + wu[i] + wl[i] - wu[i + 1] >= wlm:  # 计算wl
        wl[i + 1] = wlm
    else:
        if dw[i] + wu[i] + wl[i] - wu[i + 1] <= 0:
            wl[i + 1] = 0
        else:
            wl[i + 1] = dw[i] + wu[i] + wl[i] - wu[i + 1]

    if dw[i] + w[i] - wu[i + 1] - wl[i + 1] >= wdm:  # 计算wd
        wd[i + 1] = wdm
    else:
        wd[i + 1] = dw[i] + w[i] - wu[i + 1] - wl[i + 1]
    w[i + 1] = dw[i] + w[i]  # 计算w
for i in range(timelen):
    eu[i] = round(eu[i], 1)
    el[i] = round(el[i], 1)
    ed[i] = round(ed[i], 1)
    e[i] = round(e[i], 1)
    r[i] = round(r[i], 1)
    wu[i + 1] = round(wu[i + 1], 1)
    wl[i + 1] = round(wl[i + 1], 1)
    wd[i + 1] = round(wd[i + 1], 1)
    w[i + 1] = round(w[i + 1], 1)
print('降水过程：', p)
print('径流过程：', r)
print('蒸发过程：', e)
print('土壤蓄水量变化过程：', w)
