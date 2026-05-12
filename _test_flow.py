"""Test the full build -> new-graph flow."""
import sys, json, shutil
sys.path.insert(0, '.')
from pathlib import Path
from fastapi.testclient import TestClient

# Setup test project
Path('projects').mkdir(exist_ok=True)
Path('projects/testx').mkdir(exist_ok=True)
Path('projects/testx/meta.json').write_text(json.dumps({'name': 'testx', 'id': 'testx'}))
Path('projects/testx/demo.ttl').write_text(
    '@prefix ex: <http://example.org/> .\n'
    '@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n'
    'ex:Customer a ex:Entity ; rdfs:label "Customer" .\n'
    'ex:Order a ex:Entity ; rdfs:label "Order" .\n'
    'ex:Customer ex:places ex:Order .\n'
)

import explorer.server as srv
client = TestClient(srv.app)

# 1. Build
print("=== STEP 1: Build ===")
resp = client.post('/api/projects/testx/build', json={'filename': 'demo.ttl'})
print(f"  Status: {resp.status_code}")
print(f"  Response: {resp.json()}")

# 2. Check /api/new-graph
print("\n=== STEP 2: /api/new-graph ===")
resp2 = client.get('/api/new-graph')
data = resp2.json()
print(f"  Nodes: {len(data.get('nodes', []))}")
print(f"  Edges: {len(data.get('edges', []))}")
if data.get('nodes'):
    print(f"  First node: {data['nodes'][0]}")
if data.get('edges'):
    print(f"  First edge: {data['edges'][0]}")

# Cleanup
shutil.rmtree('projects/testx', ignore_errors=True)
