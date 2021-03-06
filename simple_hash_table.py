def entry_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None
 
def hashtable_update(htable,key,value):
    # Your code here
    bucket = hashtable_get_bucket(htable,key)
    entry = entry_find(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])
     
 
def hashtable_lookup(htable,key):
    entry = entry_find(hashtable_get_bucket(htable,key), key)
    if entry:
        return entry[1]
    else:
        return None
 
def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])
 
 
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]
 
def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out
 
def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
 
 
table = make_hashtable(3)
hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
print hashtable_lookup(table, 'Bill')



