"""
API dependencies for FastAPI.
"""
from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.services.ckan_service import ckan_service
from app.db.supabase import supabase_service

def get_ckan_service():
    """
    Dependency to get the CKAN service.
    
    Returns:
        The CKAN service instance
    """
    return ckan_service

def get_supabase_service():
    """
    Dependency to get the Supabase service.
    
    Returns:
        The Supabase service instance
    """
    return supabase_service

# Define annotated dependencies for use in route handlers
CKANService = Annotated[type(ckan_service), Depends(get_ckan_service)]
SupabaseService = Annotated[type(supabase_service), Depends(get_supabase_service)] 