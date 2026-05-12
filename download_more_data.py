import requests, os

os.makedirs('uploads/real_data', exist_ok=True)

datasets = [
    # FCC Form 477 - ALL broadband providers in US (bigger dataset)
    ('https://opendata.fcc.gov/api/views/sgz3-kiqt/rows.csv?accessType=DOWNLOAD', 'fcc_fixed_broadband_deployment.csv', 500000),
    # FCC Network Outage Reporting System (NORS) - public summary
    ('https://opendata.fcc.gov/api/views/jxhg-mrkr/rows.csv?accessType=DOWNLOAD', 'fcc_network_outages.csv', 500000),
    # UK Ofcom connected nations data
    ('https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/telecoms/connected-nations/connected-nations-2023/connected-nations-uk-report.csv', 'ofcom_connected_nations.csv', 200000),
    # Canadian CRTC telecom data
    ('https://open.canada.ca/data/dataset/d3533e92-d801-4e69-8f9b-30ca9a030a5c/resource/e3e3e3e3-e3e3-4e3e-8e3e-3e3e3e3e3e3e/download/crtc-telecom.csv', 'crtc_telecom.csv', 200000),
]

for url, fname, max_bytes in datasets:
    if os.path.exists(f'uploads/real_data/{fname}') and os.path.getsize(f'uploads/real_data/{fname}') > 1000:
        print(f'SKIP {fname} (already exists)', flush=True)
        continue
    print(f'Trying {fname}...', flush=True)
    try:
        r = requests.get(url, verify=False, timeout=60, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            content = b''
            for chunk in r.iter_content(8192):
                content += chunk
                if len(content) > max_bytes:
                    break
            path = f'uploads/real_data/{fname}'
            with open(path, 'wb') as f:
                f.write(content)
            lines = content.decode('utf-8', errors='ignore').count('\n')
            print(f'  OK: {len(content)//1024}KB, ~{lines} rows', flush=True)
        else:
            print(f'  SKIP: status {r.status_code}', flush=True)
    except Exception as e:
        print(f'  ERR: {e}', flush=True)

# Also list what we have
print('\n=== Files in uploads/real_data/ ===', flush=True)
for f in os.listdir('uploads/real_data'):
    size = os.path.getsize(f'uploads/real_data/{f}')
    print(f'  {f}: {size//1024}KB', flush=True)
