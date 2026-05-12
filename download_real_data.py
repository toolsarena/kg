import requests, os, sys

os.makedirs('uploads/real_data', exist_ok=True)

datasets = [
    # FCC Broadband providers - real telecom company data
    ('https://opendata.fcc.gov/api/views/hicn-aujz/rows.csv?accessType=DOWNLOAD', 'fcc_broadband_providers.csv', 50000),
    # UK Ofcom complaints data - real telecom complaints
    ('https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/telecoms/complaints/telecoms-and-pay-tv-complaints/complaints-data-q3-2023.csv', 'ofcom_complaints.csv', 100000),
    # Australian telecom complaints (TIO)
    ('https://data.gov.au/data/dataset/8e6a59b8-1c02-4c2e-b620-7f5a1f4c3f3a/resource/d3c0e2a0-5c5e-4c5e-8c5e-5c5e4c5e8c5e/download/tio-complaints.csv', 'au_telecom_complaints.csv', 100000),
    # NYC 311 telecom service requests
    ('https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv?accessType=DOWNLOAD&query=select%20*%20where%20%60agency%60%20%3D%20%27DOT%27%20limit%205000', 'nyc_311_requests.csv', 100000),
]

for url, fname, max_bytes in datasets:
    print(f'Trying {fname}...', flush=True)
    try:
        r = requests.get(url, verify=False, timeout=30, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
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
            print(f'  OK: {len(content)} bytes, ~{lines} rows', flush=True)
        else:
            print(f'  SKIP: status {r.status_code}', flush=True)
    except Exception as e:
        print(f'  ERR: {e}', flush=True)

print('\nDone. Check uploads/real_data/', flush=True)
