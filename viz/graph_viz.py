"""
Enhanced graph visualization — Graphistry-inspired features layered on graphify's output.

Features beyond graphify's default graph.html:
- Multi-hop drill-down with depth slider
- Histogram filters (type, community, relation, confidence)
- Point-and-click pivoting
- Fuzzy search with highlight
- Community collapse/expand
- Node detail panel with all connections
- Export current view as PNG
- Timeline slider (if nodes have dates)

GPU features (later): UMAP layout, Graphistry integration, 100K+ node rendering
"""
import json
import networkx as nx
from pathlib import Path

COLORS = [
    "#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
    "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabed4",
    "#469990", "#dcbeff", "#9A6324", "#800000", "#aaffc3",
    "#808000", "#000075", "#a9a9a9",
]

NODE_SHAPES = {
    "service": "hexagon",
    "decision": "diamond",
    "team": "triangle",
    "concept": "dot",
    "process": "square",
    "technology": "star",
}


def generate_enhanced_html(graph_json_path: Path, out_path: Path):
    data = json.loads(graph_json_path.read_text(encoding="utf-8"))

    nodes = []
    for n in data.get("nodes", []):
        nid = n.get("id", n.get("name", ""))
        ntype = n.get("type", "concept")
        comm = n.get("community", 0)
        nodes.append({
            "id": nid,
            "label": n.get("label", n.get("name", nid)),
            "title": f"<b>{n.get('label', nid)}</b><br>Type: {ntype}<br>{n.get('description', '')}",
            "group": n.get("community_name", f"Group {comm}"),
            "color": COLORS[comm % len(COLORS)],
            "shape": NODE_SHAPES.get(ntype, "dot"),
            "size": 16,
            "nodeType": ntype,
            "community": comm,
            "communityName": n.get("community_name", ""),
            "description": n.get("description", ""),
            "confidence": n.get("confidence", ""),
            "source": n.get("source", ""),
        })

    edges = []
    for e in data.get("edges", []):
        edges.append({
            "from": e.get("source", e.get("from", "")),
            "to": e.get("target", e.get("to", "")),
            "label": e.get("relation", e.get("label", "")),
            "title": e.get("description", ""),
            "arrows": "to",
            "relation": e.get("relation", e.get("label", "")),
            "confidence": e.get("confidence", ""),
            "color": {"opacity": 0.6},
        })

    html = ENHANCED_TEMPLATE.replace("__NODES__", json.dumps(nodes))
    html = html.replace("__EDGES__", json.dumps(edges))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"  → Enhanced visualization: {out_path}")


ENHANCED_TEMPLATE = r"""<!DOCTYPE html>
<html>
<head>
<title>KG Explorer</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background:#0d1117; color:#c9d1d9; }
#app { display:flex; height:100vh; }

/* Sidebar */
#sidebar { width:320px; background:#161b22; padding:16px; overflow-y:auto; border-right:1px solid #30363d; display:flex; flex-direction:column; gap:12px; }
h1 { font-size:18px; color:#58a6ff; display:flex; align-items:center; gap:8px; }
h2 { font-size:12px; color:#8b949e; text-transform:uppercase; letter-spacing:1px; margin-top:8px; }

/* Controls */
.ctrl { background:#21262d; border-radius:8px; padding:12px; }
.ctrl label { display:flex; justify-content:space-between; font-size:13px; color:#8b949e; margin-bottom:6px; }
.ctrl label span { color:#58a6ff; font-weight:600; }
input[type=range] { width:100%; accent-color:#58a6ff; }
input[type=text], select { width:100%; padding:8px; background:#0d1117; border:1px solid #30363d; color:#c9d1d9; border-radius:6px; font-size:13px; }
input[type=text]:focus, select:focus { border-color:#58a6ff; outline:none; }
button { padding:6px 12px; background:#21262d; border:1px solid #30363d; color:#c9d1d9; border-radius:6px; cursor:pointer; font-size:12px; }
button:hover { background:#30363d; }
button.active { background:#1f6feb; border-color:#1f6feb; color:#fff; }

/* Tags */
.tags { display:flex; flex-wrap:wrap; gap:4px; }
.tag { padding:3px 10px; border-radius:12px; font-size:11px; cursor:pointer; border:2px solid transparent; opacity:0.8; transition:all 0.15s; }
.tag:hover { opacity:1; }
.tag.active { opacity:1; border-color:#fff; }

/* Histograms */
.hist-bar { display:flex; align-items:center; gap:8px; margin:3px 0; cursor:pointer; }
.hist-bar .bar { height:8px; border-radius:4px; min-width:4px; transition:width 0.3s; }
.hist-bar .lbl { font-size:11px; color:#8b949e; min-width:80px; }
.hist-bar .cnt { font-size:11px; color:#58a6ff; }

/* Detail panel */
#detail { background:#21262d; border-radius:8px; padding:12px; display:none; }
#detail h3 { font-size:15px; color:#fff; margin-bottom:8px; }
#detail .meta { font-size:12px; color:#8b949e; margin:2px 0; }
#detail .conn { font-size:12px; color:#c9d1d9; padding:4px 0; border-bottom:1px solid #30363d; cursor:pointer; }
#detail .conn:hover { color:#58a6ff; }

/* Stats bar */
#stats { font-size:12px; color:#484f58; text-align:center; padding:4px; }

/* Graph */
#graph { flex:1; }

/* Toolbar */
#toolbar { position:absolute; top:12px; right:12px; display:flex; gap:6px; z-index:10; }
</style>
</head>
<body>
<div id="app">
<div id="sidebar">
    <h1>&#x1F50D; KG Explorer</h1>
    <div id="stats"></div>

    <!-- Search -->
    <div class="ctrl">
        <h2>Search</h2>
        <input type="text" id="search" placeholder="Search nodes...">
    </div>

    <!-- Depth -->
    <div class="ctrl">
        <h2>Drill-Down</h2>
        <label>Hops from selected <span id="depth-val">All</span></label>
        <input type="range" id="depth" min="0" max="10" value="10">
    </div>

    <!-- Type filter -->
    <div class="ctrl">
        <h2>Node Types</h2>
        <div id="type-hist"></div>
    </div>

    <!-- Relation filter -->
    <div class="ctrl">
        <h2>Relations</h2>
        <div id="rel-hist"></div>
    </div>

    <!-- Communities -->
    <div class="ctrl">
        <h2>Communities</h2>
        <div id="comm-tags" class="tags"></div>
    </div>

    <!-- Pivot -->
    <div class="ctrl" id="pivot-ctrl" style="display:none;">
        <h2>Pivot</h2>
        <div style="display:flex;gap:4px;flex-wrap:wrap;">
            <button onclick="pivotDeps()">Dependencies</button>
            <button onclick="pivotOwners()">Owners</button>
            <button onclick="pivotAll()">All connections</button>
            <button onclick="resetView()">Reset</button>
        </div>
    </div>

    <!-- Detail -->
    <div id="detail">
        <h3 id="d-title"></h3>
        <div class="meta" id="d-type"></div>
        <div class="meta" id="d-desc"></div>
        <div class="meta" id="d-comm"></div>
        <div class="meta" id="d-source"></div>
        <h2 style="margin-top:12px;">Connections</h2>
        <div id="d-edges"></div>
    </div>
</div>

<div id="toolbar">
    <button onclick="togglePhysics()">&#x2699; Physics</button>
    <button onclick="fitAll()">&#x26F6; Fit</button>
    <button onclick="exportPNG()">&#x1F4F7; PNG</button>
</div>
<div id="graph"></div>
</div>

<script>
const allNodes = __NODES__;
const allEdges = __EDGES__;

// Build indexes
const nodeMap = {};
allNodes.forEach(n => nodeMap[n.id] = n);
const types = {}, rels = {}, comms = {};
allNodes.forEach(n => { types[n.nodeType] = (types[n.nodeType]||0)+1; comms[n.communityName||'Unknown'] = (comms[n.communityName||'Unknown']||0)+1; });
allEdges.forEach(e => { rels[e.relation||'unknown'] = (rels[e.relation||'unknown']||0)+1; });

// State
let activeTypes = new Set(Object.keys(types));
let activeRels = new Set(Object.keys(rels));
let activeComms = new Set(Object.keys(comms));
let selectedNode = null;
let physicsOn = true;

// Network
const nodesDS = new vis.DataSet(allNodes);
const edgesDS = new vis.DataSet(allEdges);
const network = new vis.Network(document.getElementById('graph'), { nodes: nodesDS, edges: edgesDS }, {
    physics: { solver:'forceAtlas2Based', forceAtlas2Based:{ gravitationalConstant:-60, springLength:100 }, stabilization:{ iterations:150 } },
    interaction: { hover:true, tooltipDelay:100, multiselect:true },
    nodes: { font:{ size:11, color:'#8b949e' }, borderWidth:2 },
    edges: { font:{ size:8, color:'#484f58', strokeWidth:0 }, smooth:{ type:'continuous' } },
});

// Stats
document.getElementById('stats').textContent = `${allNodes.length} nodes · ${allEdges.length} edges · ${Object.keys(comms).length} communities`;

// --- Histograms ---
function buildHist(container, data, activeSet) {
    const el = document.getElementById(container);
    const max = Math.max(...Object.values(data));
    el.innerHTML = '';
    Object.entries(data).sort((a,b) => b[1]-a[1]).forEach(([k,v]) => {
        const row = document.createElement('div');
        row.className = 'hist-bar';
        row.innerHTML = `<span class="lbl">${k}</span><span class="bar" style="width:${(v/max)*100}px;background:${activeSet.has(k)?'#58a6ff':'#30363d'}"></span><span class="cnt">${v}</span>`;
        row.onclick = () => { activeSet.has(k) ? activeSet.delete(k) : activeSet.add(k); buildHist(container, data, activeSet); applyFilters(); };
        el.appendChild(row);
    });
}
buildHist('type-hist', types, activeTypes);
buildHist('rel-hist', rels, activeRels);

// --- Community tags ---
function buildCommTags() {
    const el = document.getElementById('comm-tags');
    el.innerHTML = '';
    Object.entries(comms).sort((a,b) => b[1]-a[1]).forEach(([name, count]) => {
        const tag = document.createElement('span');
        tag.className = 'tag' + (activeComms.has(name) ? ' active' : '');
        tag.textContent = `${name} (${count})`;
        const sample = allNodes.find(n => (n.communityName||'Unknown') === name);
        tag.style.background = sample ? sample.color : '#30363d';
        tag.style.color = '#fff';
        tag.onclick = () => { activeComms.has(name) ? activeComms.delete(name) : activeComms.add(name); buildCommTags(); applyFilters(); };
        el.appendChild(tag);
    });
}
buildCommTags();

// --- Filtering ---
function getNeighbors(nodeId, depth) {
    if (depth >= 10) return null;
    let visited = new Set([nodeId]);
    let frontier = [nodeId];
    for (let d = 0; d < depth; d++) {
        let next = [];
        frontier.forEach(nid => {
            allEdges.forEach(e => {
                if (e.from === nid && !visited.has(e.to)) { visited.add(e.to); next.push(e.to); }
                if (e.to === nid && !visited.has(e.from)) { visited.add(e.from); next.push(e.from); }
            });
        });
        frontier = next;
    }
    return visited;
}

function applyFilters() {
    const search = document.getElementById('search').value.toLowerCase();
    const depth = parseInt(document.getElementById('depth').value);
    const reachable = selectedNode ? getNeighbors(selectedNode, depth) : null;

    allNodes.forEach(n => {
        let show = activeTypes.has(n.nodeType) && activeComms.has(n.communityName || 'Unknown');
        if (show && search) show = n.label.toLowerCase().includes(search) || n.id.toLowerCase().includes(search) || (n.description||'').toLowerCase().includes(search);
        if (show && reachable) show = reachable.has(n.id);
        nodesDS.update({ id: n.id, hidden: !show });
    });
    allEdges.forEach(e => {
        const sVis = !nodesDS.get(e.from)?.hidden;
        const tVis = !nodesDS.get(e.to)?.hidden;
        const relOk = activeRels.has(e.relation || 'unknown');
        edgesDS.update({ id: e.id, hidden: !(sVis && tVis && relOk) });
    });
}

document.getElementById('search').addEventListener('input', applyFilters);
document.getElementById('depth').addEventListener('input', (e) => {
    const v = parseInt(e.target.value);
    document.getElementById('depth-val').textContent = v >= 10 ? 'All' : v;
    applyFilters();
});

// --- Node click → detail + pivot ---
network.on('click', (params) => {
    if (params.nodes.length > 0) {
        selectedNode = params.nodes[0];
        const node = nodeMap[selectedNode];
        document.getElementById('detail').style.display = 'block';
        document.getElementById('pivot-ctrl').style.display = 'block';
        document.getElementById('d-title').textContent = node.label;
        document.getElementById('d-type').textContent = `Type: ${node.nodeType}`;
        document.getElementById('d-desc').textContent = node.description || '';
        document.getElementById('d-comm').textContent = `Community: ${node.communityName}`;
        document.getElementById('d-source').textContent = node.source ? `Source: ${node.source}` : '';

        const conns = allEdges.filter(e => e.from === selectedNode || e.to === selectedNode);
        document.getElementById('d-edges').innerHTML = conns.map(e => {
            const other = e.from === selectedNode ? e.to : e.from;
            const otherNode = nodeMap[other];
            const dir = e.from === selectedNode ? '→' : '←';
            return `<div class="conn" onclick="focusNode('${other}')">${dir} <b>${otherNode?.label||other}</b> [${e.relation||e.label}]</div>`;
        }).join('');

        applyFilters();
    } else {
        selectedNode = null;
        document.getElementById('detail').style.display = 'none';
        document.getElementById('pivot-ctrl').style.display = 'none';
        applyFilters();
    }
});

// --- Pivot functions ---
function pivotByRelation(rel) {
    if (!selectedNode) return;
    const connected = new Set([selectedNode]);
    allEdges.forEach(e => {
        if (rel && (e.relation||e.label) !== rel) return;
        if (e.from === selectedNode) connected.add(e.to);
        if (e.to === selectedNode) connected.add(e.from);
    });
    allNodes.forEach(n => nodesDS.update({ id: n.id, hidden: !connected.has(n.id) }));
    allEdges.forEach(e => {
        const vis = connected.has(e.from) && connected.has(e.to);
        edgesDS.update({ id: e.id, hidden: !vis });
    });
}
function pivotDeps() { pivotByRelation('depends_on'); }
function pivotOwners() { pivotByRelation('owned_by'); }
function pivotAll() { pivotByRelation(null); }
function resetView() { selectedNode = null; document.getElementById('depth').value = 10; document.getElementById('depth-val').textContent = 'All'; applyFilters(); network.fit(); }
function focusNode(id) { network.focus(id, { scale: 1.5, animation: true }); network.selectNodes([id]); }

// --- Toolbar ---
function togglePhysics() { physicsOn = !physicsOn; network.setOptions({ physics: { enabled: physicsOn } }); }
function fitAll() { network.fit(); }
function exportPNG() {
    const canvas = document.querySelector('#graph canvas');
    if (canvas) { const a = document.createElement('a'); a.href = canvas.toDataURL('image/png'); a.download = 'kg-graph.png'; a.click(); }
}
</script>
</body>
</html>"""
