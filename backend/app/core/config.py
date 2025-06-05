"""
Configuration settings for the application.
"""
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    # API settings
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    
    # CKAN API settings
    CKAN_BASE_URL: str = os.getenv("CKAN_BASE_URL", "https://data.gov.lv/dati/lv/")
    # For backward compatibility, check both new and old env var names
    CKAN_COMPANY_RESOURCE_ID: str = os.getenv("CKAN_COMPANY_RESOURCE_ID", 
                                            os.getenv("CKAN_RESOURCE_ID", "25e80bf3-f107-4ab4-89ef-251b5b9374e9"))
    
    # ===== FINANCIAL DATA RESOURCES =====
    # Annual Report Basic Information (Gada pārskatu pamatinformācija)
    CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID: str = os.getenv("CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID", "27fcc5ec-c63b-4bfd-bb08-01f073a52d04")
    # Balance Sheets (Bilances)
    CKAN_BALANCE_SHEETS_RESOURCE_ID: str = os.getenv("CKAN_BALANCE_SHEETS_RESOURCE_ID", "50ef4f26-f410-4007-b296-22043ca3dc43")
    # Income Statements (Peļņas vai zaudējumu aprēķini)
    CKAN_INCOME_STATEMENTS_RESOURCE_ID: str = os.getenv("CKAN_INCOME_STATEMENTS_RESOURCE_ID", "d5fd17ef-d32e-40cb-8399-82b780095af0")
    # Cash Flow Statements (Naudas plūsmas pārskati)
    CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID: str = os.getenv("CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID", "1a11fc29-ba7c-4e5a-8edc-7a28cea24988")
    
    # ===== COMPANY DATA RESOURCES =====
    # Capital and investment data
    CKAN_CAPITAL_RESOURCE_ID: str = os.getenv("CKAN_CAPITAL_RESOURCE_ID", "7910fef5-93eb-4d03-acf0-f45465d67414")
    # Beneficial owners data
    CKAN_BENEFICIARY_RESOURCE_ID: str = os.getenv("CKAN_BENEFICIARY_RESOURCE_ID", "20a9b26d-d056-4dbb-ae18-9ff23c87bdee")
    # Company members data
    CKAN_MEMBERS_RESOURCE_ID: str = os.getenv("CKAN_MEMBERS_RESOURCE_ID", "837b451a-4833-4fd1-bfdd-b45b35a994fd")
    # Business activity data
    CKAN_BUSINESS_RESOURCE_ID: str = os.getenv("CKAN_BUSINESS_RESOURCE_ID", "49bbd751-3fa2-4d78-8c35-ae0e1c5250d6")
    # Liquidation process data
    CKAN_LIQUIDATION_RESOURCE_ID: str = os.getenv("CKAN_LIQUIDATION_RESOURCE_ID", "59e7ec49-f1c6-4410-8ee6-e7737ac5eaee")
    # Company officers data
    CKAN_OFFICERS_RESOURCE_ID: str = os.getenv("CKAN_OFFICERS_RESOURCE_ID", "e665114a-73c2-4375-9470-55874b4cfa6b")
    # Company stockholders data
    CKAN_STOCKHOLDERS_RESOURCE_ID: str = os.getenv("CKAN_STOCKHOLDERS_RESOURCE_ID", "6adabd83-93f9-4d7f-bebd-fa109bbf794a")
    
    # Supabase settings
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"  # Ignore extra environment variables

# Create settings instance
settings = Settings() 