from supabase import create_client
from src.config import SUPABASE_URL, SUPABASE_KEY

def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_table(table_name, limit=5):
    supabase = get_supabase_client()
    response = supabase.table(table_name).select("*").limit(limit).execute()
    return response.data