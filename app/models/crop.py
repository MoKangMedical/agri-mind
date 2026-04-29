"""Crop data models."""
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class CropCategory(str, Enum):
    GRAIN = "粮食作物"        # 粮食
    VEGETABLE = "蔬菜"        # 蔬菜
    FRUIT = "水果"            # 水果
    HERB = "中药材"           # 中药材
    CASH = "经济作物"         # 经济作物
    FLOWER = "花卉"           # 花卉

class ClimateZone(str, Enum):
    NORTHEAST = "东北"        # 东北
    NORTH = "华北"            # 华北
    EAST = "华东"             # 华东
    CENTRAL = "华中"          # 华中
    SOUTH = "华南"            # 华南
    SOUTHWEST = "西南"        # 西南
    NORTHWEST = "西北"        # 西北
    TIBET = "青藏"            # 青藏

class GrowthStage(str, Enum):
    SOWING = "播种"
    GERMINATION = "出苗"
    SEEDLING = "幼苗"
    VEGETATIVE = "营养生长期"
    FLOWERING = "开花期"
    FRUITING = "结果期"
    MATURING = "成熟期"
    HARVEST = "收获"

class Crop(BaseModel):
    """A crop with growing guide."""
    id: str
    name: str
    scientific_name: Optional[str] = None
    category: CropCategory
    suitable_zones: list[ClimateZone]
    growing_season: tuple[int, int] = Field(description="适宜月份范围")
    growth_duration_days: int = Field(description="生育期天数")
    optimal_temp: tuple[float, float] = Field(description="最适温度°C范围")
    water_needs: str = Field(description="水分需求: 低/中/高")
    soil_type: str = Field(description="适宜土壤类型")
    companion_plants: list[str] = []
    common_diseases: list[str] = []
    common_pests: list[str] = []
    sowing_depth_cm: Optional[float] = None
    spacing_cm: Optional[float] = None
    yield_per_mu_kg: Optional[float] = Field(None, description="亩产量kg")

class CropGuide(BaseModel):
    """Detailed growing guide for a crop."""
    crop: Crop
    stages: list[dict] = Field(description="各生育期管理要点")
    fertilization: list[dict] = Field(description="施肥方案")
    irrigation: list[dict] = Field(description="灌溉方案")
    pest_prevention: list[dict] = Field(description="病虫害防治日历")

class DiseaseDiagnosis(BaseModel):
    """Disease/pest diagnosis result."""
    image_url: str
    suspected_diseases: list[dict]
    confidence: float
    severity: str  # 轻度/中度/重度
    treatment: list[str]
    prevention: list[str]
