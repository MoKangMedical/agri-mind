"""🌾 农智云 AgriMind — Main Application."""
import sys
from pathlib import Path

def cli():
    """Command-line interface."""
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "serve":
            port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
            start_server(port)
        elif cmd == "query":
            query_crop(sys.argv[2] if len(sys.argv) > 2 else "水稻")
        else:
            print_help()
    else:
        print_help()

def print_help():
    print("""
🌾 农智云 AgriMind v0.1.0

用法:
  agri-mind serve [PORT]     启动 Web 服务
  agri-mind query CROP       查询作物种植指南
  agri-mind help             显示帮助

示例:
  agri-mind query 水稻
  agri-mind serve 8000
""")

def start_server(port: int):
    try:
        import uvicorn
        from app.api.server import create_app
        print(f"🌾 农智云启动: http://localhost:{port}")
        uvicorn.run(create_app(), host="0.0.0.0", port=port)
    except ImportError:
        print("❌ 需要安装 uvicorn: pip install uvicorn")

def query_crop(crop_name: str):
    from app.agents.crop_expert import CropExpertAgent
    expert = CropExpertAgent()
    guide = expert.get_crop_guide(crop_name)
    if "error" in guide:
        print(f"❌ {guide['error']}")
        return

    print(f"\n🌾 {crop_name} 种植指南")
    print(f"类别: {guide['category']}")
    print(f"适宜区域: {', '.join(guide['zones'])}")
    print(f"生育期: {guide['duration']}天")
    print(f"最适温度: {guide['temp'][0]}-{guide['temp'][1]}°C")
    print(f"水分需求: {guide['water']}")
    print(f"\n📅 生育期管理:")
    for stage in guide.get("stages", []):
        print(f"  [{stage['stage']}] {stage['days']}: {stage['要点']}")
    print()

if __name__ == "__main__":
    cli()
