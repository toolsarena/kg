import requests, json, os, sys

BASE = "https://api.github.com/repos/tmforum-apis/Open_Api_And_Data_Model/contents/schemas"
OUT = "uploads/tmf_sid"
os.makedirs(OUT, exist_ok=True)

DOMAINS = ["Common", "Customer", "EngagedParty", "Product", "Resource", "Service"]
total = 0

for domain in DOMAINS:
    r = requests.get(f"{BASE}/{domain}", verify=False, timeout=15)
    if r.status_code != 200:
        print(f"SKIP {domain}: {r.status_code}", flush=True)
        continue
    files = json.loads(r.text)
    schemas = [f for f in files if f["name"].endswith(".schema.json")]
    print(f"{domain}: {len(schemas)} schemas", flush=True)
    for sf in schemas:
        try:
            dr = requests.get(sf["download_url"], verify=False, timeout=15)
            if dr.status_code == 200:
                path = os.path.join(OUT, f"{domain}__{sf['name']}")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(dr.text)
                total += 1
                if total % 20 == 0:
                    print(f"  ...{total} downloaded", flush=True)
        except Exception as e:
            print(f"  ERR {sf['name']}: {e}", flush=True)

print(f"\nDone: {total} schema files in {OUT}/", flush=True)
