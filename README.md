# 🌾 农智云 AgriMind

> AI驱动的中国智慧种植知识平台  
> 种植百科 × 病虫害AI诊断 × 时令指导 × 产量预测

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)

## ✨ 核心功能

### 🌱 种植百科
- **500+ 中国常见作物**种植指南
- 覆盖粮食/蔬菜/水果/中药材/经济作物
- 按地区适配（东北/华北/华东/华南/西南/西北）
- 全生育期管理：播种→育苗→定植→田管→收获

### 🔍 病虫害AI诊断
- **拍照识别** — 上传叶片/果实照片，秒级诊断
- **200+ 常见病虫害**数据库
- AI 推荐防治方案（生物防治优先）
- 预警系统：根据天气预测病虫害风险

### 📅 时令农事日历
- 根据经纬度 + 品种自动计算最佳播种/收获窗口
- 24节气 × 作物管理指导
- 天气预警联动（霜冻/暴雨/干旱）

### 📊 产量预测
- 作物模型 × 历史数据 × 实时天气
- 区域产量对比分析
- 市场价格趋势整合

### 🤖 AI 农技问答
- 多Agent协同：病虫害专家 × 土壤专家 × 气象专家
- 支持方言语音输入
- 对接农技推广站数据

## 🏗️ 技术架构

```
agri-mind/
├── app/
│   ├── api/              # FastAPI REST API
│   ├── models/           # 数据模型 (Pydantic)
│   ├── agents/           # AI Agents
│   │   ├── crop_expert.py      # 作物专家
│   │   ├── pest_diagnoser.py   # 病虫害诊断
│   │   ├── weather_advisor.py  # 气象顾问
│   │   └── market_analyst.py   # 市场分析师
│   ├── tools/            # MCP 工具
│   │   ├── weather_api.py      # 中国气象数据
│   │   ├── soil_database.py    # 土壤数据库
│   │   ├── pest_recognizer.py  # 病虫害识别
│   │   └── satellite_ndvi.py   # 卫星遥感
│   ├── services/         # 业务逻辑
│   ├── knowledge/        # 知识库
│   │   ├── crops/              # 作物数据 (JSON)
│   │   ├── diseases/           # 病害图谱
│   │   ├── pesticides/         # 农药信息
│   │   └── calendar/           # 农事日历
│   └── web/              # Web UI
├── data/                 # 数据集
├── tests/
└── docs/
```

## 🚀 快速开始

```bash
pip install agri-mind[all]
agri-mind serve --port 8000
```

## 📊 数据来源

| 数据 | 来源 | 覆盖 |
|------|------|------|
| 作物品种 | 中国种子数据库 | 500+ 品种 |
| 病虫害 | 中国农业病虫害信息库 | 200+ 种类 |
| 土壤 | 全国土壤普查数据 | 全国 |
| 气象 | 中国气象局 API | 实时+历史 |
| 农药 | 中国农药信息网 | 3000+ 农药 |
| 价格 | 全国农产品批发市场价格 | 500+ 品种 |

## 🤝 贡献

欢迎农业专家、开发者、农技推广员参与贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 📜 License

MIT License
