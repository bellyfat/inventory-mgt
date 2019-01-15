from csv import DictReader, DictWriter
import sys

VEN_CODE = 'VenCode'
PART_NUMBER = 'PartNumber'
QUANTITY = 'TotalQty'


if len(sys.argv) > 2:
    filename_master = sys.argv[1]
    filename_supply = sys.argv[2]
else:
    filename_master = 'MasterInventory.csv'
    filename_supply = 'SupplyInventory.csv'

print("Master filename:", filename_master)
print("Supply filename:", filename_supply)


# def create_filter(keep_set):
#     """Returns a function filter_row that has access to outer parameter of keep_set.
#     The returned function will return True if a row is not in the keep_set.
#     """
    
#     def filter_row(row):
#         """Returns true if row's """
#         return True if row.get('VenCode') not in keep_set else False
#     return filter_row


# def get_value_set(dictionary, key):
#     """Accepts a list of dictionaries and a key string.
#     Returns a set off all the values at keys with the value of key string. 
#     """

#     value_set = set()
#     for id in dictionary:
#         value_set.add(dictionary.get(id).get('VenCode'))
#     return value_set


# def build_dict_from_csv(filename, filter_row=None):
#     """Builds dictionary from csv file.
#     CSV file must include columns: VenCode,PartNumber,TotalQty
#     """
    
#     if not filename.endswith('.csv'):
#         print("This is not a proper csv file.")
#         return False

#     dictionary = {}
#     with open(filename, newline='') as file:
#         reader = DictReader(file) 
#         for row in reader:
#             if filter_row == None or not filter_row(row):

#                 id = f'{row.get("VenCode")}-{row.get("PartNumber")}'
#                 details = {
#                     'VenCode': row.get('VenCode'),
#                     'TotalQty': row.get('TotalQty'),
#                 }
#                 dictionary[id] = details
#     return dictionary



# def update_master_qty():
#     master_dict = build_dict_from_csv(filename_master)

#     ven_codes = get_value_set(master_dict, 'VenCode')

#     filter_cb = create_filter(ven_codes)

#     supply_dict = build_dict_from_csv(filename_supply, filter_cb)


#     fieldnames = ['VenCode', 'PartNumber', 'TotalQty']

#     with open('NewMasterInventory.csv', 'w', newline='') as out_file:
#         # reader = DictReader(in_file)

#         writer = DictWriter(out_file, fieldnames=fieldnames)
#         import pdb; pdb.set_trace()

        
#         for part_id in master_dict:

#             # make a collection of master row-col locations with the new supply values
#             # update_list = [{'loc': [3,4], 'value':223}, ...]
            
#             master_qty = int(master_dict[part_id]['TotalQty'])
#             supply_qty = int(supply_dict[part_id]['TotalQty'])

#             if master_qty < supply_qty:

#                 new_row = master_dict[part_id]
#                 writer.writerow(new_row)
#                 print("master:", master_qty, "supply:", supply_qty)
#             else:
#                 writer.writerow(master_dict[part_id])
            



def create_master_cache():
    index = {}
    with open(filename_master) as csv_file:
        supply = DictReader(csv_file)
        for part in supply:
            code = part[VEN_CODE]
            num = part[PART_NUMBER]
            qty = part[QUANTITY]

            # print(code, num, qty)
            if index.get(code):
                index[code][num] = qty
            else:
                index[code] = {num: qty}
    return index

def search_cache(idx, keys, level=0):
    if level >= len(keys):
        return False
    key = keys[level]
    val = idx.get(key)
    if val and level == len(keys)-1:
        return val   
    if not val:
        return False   
    return search_index(val, keys, level+1)


def update_master():
    try:
        master_cache = create_master_cache()
        print('master_cache', master_cache)
        x = 0
        with open(filename_supply) as csv_file:
            supply = DictReader(csv_file)
            for part in supply:
                supply_code = part[VEN_CODE]
                supply_num = part[PART_NUMBER]
                qty = part[QUANTITY]
                
                val = search_index(
                    master_cache,
                    [supply_code, supply_num]
                )

                if val:
                    print('found in master', supply_code, supply_num)
                    print('master qty', val)
                    print('supply qty', qty)


    except KeyError as e:
        print('Error', e)

dx = {
    'A68': {
        '1041WK': '1', 
        '1021': '61'
        , '1020': '36'
        , '1022': '114'
        , '1036': '19'
        , '1041RK': '2'
        , '1037': '9'
        , '1041AMK': '14'
        , '1041KAM': '1'
        , '1034': '32'
        , '1042AMK': '8'
        , '1007': '0'
        , '1006': '1'
        , '1014K': '24'
        , '1004': '2'
        , '1003': '1'
        , '1002': '2'
        , '1001': '0'
        }, 
    'Y10': {
        '2013Q1CP': '77', 
        '8000158': '19', 
        '8000154': '12',
        '8000151': '13',
        '8000150': '44',
        '8000153': '18',
        '8000152': '41',
        '8000224': '19',
        '8000134': '16',
        '8000221': '274',
        '8000135': '25',
        '8000222': '15',
        '8000148': '256',
        '8000227': '20',
        '8000226': '81',
        '8000225': '12',
        '8000101': '9',
        '8000228': '12',
        '8000146': '128',
        '8000147': '30',
        '8000145': '36',
        '8000124': '103'
    }
}

# print('search for Y10_8000148:', search_index(dx, ['A68', '1001']))

update_master()
# print(index)

