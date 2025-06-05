"""
Supabase client and utilities.
"""
from supabase import create_client
from app.core.config import settings

def get_supabase_client():
    """
    Get a Supabase client instance.
    
    Returns:
        A configured Supabase client
    """
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_ANON_KEY
    
    if not url or not key:
        raise ValueError("Supabase URL and key must be configured")
    
    return create_client(url, key)

def get_service_role_client():
    """
    Get a Supabase client with service role privileges.
    
    Returns:
        A configured Supabase client with service role privileges
    """
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_SERVICE_ROLE_KEY
    
    if not url or not key:
        raise ValueError("Supabase URL and service role key must be configured")
    
    return create_client(url, key)

class SupabaseService:
    """Service for interacting with Supabase."""
    
    def __init__(self):
        """Initialize the Supabase service."""
        self.client = get_supabase_client()
    
    def save_company_data(self, company_data):
        """
        Save supplementary company data to Supabase.
        
        Args:
            company_data: The company data to save
            
        Returns:
            The result of the operation
        """
        # Ensure we have required fields
        if 'registration_number' not in company_data or 'name' not in company_data:
            raise ValueError("Company data must include registration_number and name")
            
        # Prepare data for upsert
        upsert_data = {
            'registration_number': company_data.get('registration_number'),
            'name': company_data.get('name'),
            'status': company_data.get('status'),
            'address': company_data.get('address'),
            'founded_date': company_data.get('founded_date')
        }
        
        # Add any additional data as JSON
        additional_data = {}
        for key, value in company_data.items():
            if key not in upsert_data and value is not None:
                additional_data[key] = value
                
        if additional_data:
            upsert_data['additional_data'] = additional_data
        
        try:
            # Upsert into companies table
            result = self.client.table("companies").upsert(upsert_data).execute()
            return result
        except Exception as e:
            print(f"Supabase error: {e}")
            raise
    
    def get_company_data(self, reg_number):
        """
        Get supplementary company data from Supabase.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company data
        """
        try:
            result = self.client.table("companies").select("*").eq("registration_number", reg_number).execute()
            data = result.data
            
            # If we have data, merge additional_data back into the result
            if data and data[0]:
                company = data[0]
                additional_data = company.pop('additional_data', None) or {}
                
                # Merge additional data fields into the main company object
                if additional_data and isinstance(additional_data, dict):
                    company.update(additional_data)
                    
                return company
            return None
        except Exception as e:
            print(f"Supabase error: {e}")
            raise

# Create a singleton instance
supabase_service = SupabaseService() 