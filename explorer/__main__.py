"""Run: python -m explorer [--ttl path/to/file.ttl] [--port 8899]"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from explorer.server import load_ttl, app
import argparse, uvicorn

parser = argparse.ArgumentParser()
parser.add_argument("--ttl", default="graphify-out/graph.ttl")
parser.add_argument("--port", type=int, default=8899)
parser.add_argument("--host", default="127.0.0.1")
args = parser.parse_args()
load_ttl(args.ttl)
print(f"\n  🔬 KG Explorer → http://{args.host}:{args.port}\n")
uvicorn.run(app, host=args.host, port=args.port, log_level="warning")
