import requests, os
os.makedirs('uploads/tmf_docs', exist_ok=True)

urls = [
    ('https://raw.githubusercontent.com/tmforum-apis/Open_Api_And_Data_Model/master/README.md', 'tmf_overview.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF620_ProductCatalog/master/README.md', 'tmf620_product_catalog.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF629_CustomerManagement/master/README.md', 'tmf629_customer.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF633_ServiceCatalog/master/README.md', 'tmf633_service_catalog.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF634_ResourceCatalog/master/README.md', 'tmf634_resource_catalog.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF638_ServiceInventory/master/README.md', 'tmf638_service_inventory.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF639_ResourceInventory/master/README.md', 'tmf639_resource_inventory.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF641_ServiceOrder/master/README.md', 'tmf641_service_order.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF622_ProductOrder/master/README.md', 'tmf622_product_order.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF632_PartyManagement/master/README.md', 'tmf632_party.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF621_TroubleTicket/master/README.md', 'tmf621_trouble_ticket.md'),
    ('https://raw.githubusercontent.com/tmforum-apis/TMF642_AlarmManagement/master/README.md', 'tmf642_alarm.md'),
]

count = 0
for url, fname in urls:
    try:
        r = requests.get(url, verify=False, timeout=15)
        if r.status_code == 200 and len(r.text) > 100:
            with open(f'uploads/tmf_docs/{fname}', 'w', encoding='utf-8') as f:
                f.write(r.text)
            count += 1
            print(f'OK {fname} ({len(r.text)} bytes)', flush=True)
        else:
            print(f'SKIP {fname}: status={r.status_code}', flush=True)
    except Exception as e:
        print(f'ERR {fname}: {e}', flush=True)
print(f'\nTotal: {count} docs downloaded to uploads/tmf_docs/', flush=True)
