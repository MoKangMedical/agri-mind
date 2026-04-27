"""Crop Expert Agent — answers all crop growing questions."""
from pydantic import BaseModel

CROP_KNOWLEDGE = {
    "水稻": {
        "category": "粮食作物",
        "zones": ["华东", "华中", "华南", "西南"],
        "season": [4, 10],
        "duration": 150,
        "temp": [20, 35],
        "water": "高",
        "soil": "水稻土、粘壤土",
        "stages": [
            {"stage": "播种", "days": "1-7", "要点": "浸种催芽，温水浸种48h"},
            {"stage": "育秧", "days": "7-30", "要点": "保持湿润，温度25-30°C"},
            {"stage": "移栽", "days": "30-35", "要点": "秧龄30天，3-4叶期移栽"},
            {"stage": "分蘖", "days": "35-70", "要点": "浅水灌溉，追施分蘖肥"},
            {"stage": "孕穗", "days": "70-95", "要点": "保持水层3-5cm，施穗肥"},
            {"stage": "抽穗扬花", "days": "95-110", "要点": "保持浅水层，注意稻瘟病"},
            {"stage": "灌浆", "days": "110-130", "要点": "干湿交替灌溉"},
            {"stage": "成熟收获", "days": "130-150", "要点": "收获前7天断水"},
        ],
        "fertilization": [
            {"时期": "基肥", "种类": "有机肥+复合肥", "用量": "有机肥1000kg/亩"},
            {"时期": "分蘖肥", "种类": "尿素", "用量": "10-15kg/亩"},
            {"时期": "穗肥", "种类": "复合肥", "用量": "10kg/亩"},
        ],
    },
    "小麦": {
        "category": "粮食作物",
        "zones": ["华北", "西北", "华东"],
        "season": [10, 6],
        "duration": 240,
        "temp": [0, 25],
        "water": "中",
        "soil": "壤土、粘壤土",
        "stages": [
            {"stage": "播种", "days": "10月", "要点": "适期播种，播深3-5cm"},
            {"stage": "出苗", "days": "播种后7-10天", "要点": "保证出苗均匀"},
            {"stage": "分蘖", "days": "11-12月", "要点": "冬前促分蘖"},
            {"stage": "越冬", "days": "12-2月", "要点": "浇冻水，防冻害"},
            {"stage": "返青拔节", "days": "3-4月", "要点": "追施拔节肥"},
            {"stage": "抽穗扬花", "days": "4-5月", "要点": "防治赤霉病"},
            {"stage": "灌浆成熟", "days": "5-6月", "要点": "适时收获"},
        ],
    },
}

class CropExpertAgent:
    """AI crop growing expert."""

    def __init__(self):
        self.knowledge = CROP_KNOWLEDGE

    def get_crop_guide(self, crop_name: str) -> dict:
        """Get growing guide for a crop."""
        return self.knowledge.get(crop_name, {"error": f"未找到{crop_name}的种植信息"})

    def get_seasonal_advice(self, crop_name: str, month: int, zone: str) -> dict:
        """Get what to do this month."""
        crop = self.knowledge.get(crop_name)
        if not crop:
            return {"error": f"未找到{crop_name}"}

        advice = {
            "crop": crop_name,
            "month": month,
            "zone": zone,
            "current_tasks": [],
            "reminders": [],
        }

        for stage in crop.get("stages", []):
            advice["current_tasks"].append(f"关注{stage['stage']}: {stage['要点']}")

        return advice

    def search(self, query: str) -> list:
        """Search knowledge base."""
        results = []
        for name, data in self.knowledge.items():
            if query in name or query in str(data):
                results.append({"name": name, "category": data["category"]})
        return results
