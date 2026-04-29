# 农智云 AgriMind

AI驱动的中国智慧种植知识平台

## 一句话定义

农智云不卖农业SaaS，卖种植决策结果。输入地块信息+气候数据+种植目标，输出最优种植方案（品种选择/施肥/灌溉/病虫害预防）。

## 解决什么问题

| 痛点 | 传统方式 | 农智云 |
|------|---------|--------|
| 品种选择 | 经验判断 | AI数据驱动 |
| 施肥方案 | 固定配方 | 精准变量施肥 |
| 病虫害 | 发现后治疗 | 预测+预防 |
| 产量预估 | 粗略估计 | 模型预测 |

## 核心能力

- 知识图谱: 作物-土壤-气候-病虫害关联
- 多Agent协作: 农艺师+气象师+植保师AI
- 决策引擎: 输入地块→输出种植方案
- 产量模型: 基于历史数据的产量预测

## 快速开始

    git clone https://github.com/MoKangMedical/agri-mind.git
    cd agri-mind
    pip install -r requirements.txt
    python src/main.py --location "山东省济南市" --crop "小麦"

MIT License
