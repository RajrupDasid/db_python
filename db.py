import json
import os
from dotenv import load_dotenv
from supabase import create_client,Client
from faker import Faker
import fake_commerce

def add_vendor(supabase,vendor_count):
    fake=Faker()
    foreign_key_list = []
    fake.add_provider(fake_commerce.Provider)
    main_list = []
    for i in range(vendor_count):
        value = {'vendor_name':fake.company(),'total_employees':fake.random_int(40,169),
        'vendor_location':fake.country()}
        print(value)
        main_list.append(value)
        print(main_list)
    data = supabase.table('Vendor').insert(main_list).execute()
    data_json =  json.loads(data.json())
    data_entries = data_json['data']
    for i in range(len(data_entries)):
        foreign_key_list.append(int(data_entries[i]['vendor_id']))
    return foreign_key_list