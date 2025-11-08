from supabase import create_client
from src.config import SUPABASE_URL, SUPABASE_KEY

def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_table(table_name, limit=None, batch_size=1000):
    supabase = get_supabase_client()
    all_data = []
    offset = 0

    if limit and limit <= batch_size:
        response = supabase.table(table_name).select("*").limit(limit).execute()
        return response.data

    while True:
        response = (
            supabase.table(table_name)
            .select("*")
            .range(offset, offset + batch_size - 1)
            .execute()
        )
        data = response.data
        if not data:
            break
        all_data.extend(data)
        if limit and len(all_data) >= limit:
            break
        offset += batch_size
    return all_data[:limit] if limit else all_data
