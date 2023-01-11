import json
import os
from dotenv import load_dotenv
from supabase import create_client,Client
from faker import Faker
import faker_commerce

def add_vendor(supabase,vendor_count):
    fake=Faker()
    foreign_key_list = []
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    for i in range(vendor_count):
        value = {'vendor_name':fake.company(),'employee_count':fake.random_int(10,200),
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
def add_product(supabase,vendor_id):
    fake=Faker()
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    iterator = fake.random_int(1,200)
    for i in range(iterator):
        value = {'vendor_id':vendor_id,'product_name':fake.ecommerce_name(),'inventory_count':fake.random_int(1,9000),'pricing':fake.random_int(45,9000)}
        main_list.append(value)
        print(value)
        print(main_list)
    data = supabase.table('Product').insert(main_list).execute()
    print(data)
def main():
    vendor_count = 50
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url,key)
    fk_list = add_vendor(supabase,vendor_count)
    for i in range(len(fk_list)):
        add_product(supabase,fk_list[i])
main()