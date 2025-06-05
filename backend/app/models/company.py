"""
Data models for company information.
"""
from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

class CompanyBase(BaseModel):
    """Base company model with common fields."""
    registration_number: str = Field(..., description="Company registration number")
    name: str = Field(..., description="Company name")

class CompanySearch(BaseModel):
    """Model for company search parameters."""
    q: str = Field(..., description="Search query")
    limit: int = Field(10, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")

class CapitalData(BaseModel):
    """Model for company capital data."""
    regcode: Optional[str] = Field(None, description="Registration code")
    capital: Optional[str] = Field(None, description="Capital amount")
    capital_reg_date: Optional[str] = Field(None, description="Capital registration date")
    capital_curr: Optional[str] = Field(None, description="Capital currency")
    # Add other capital fields as needed

class BeneficiaryData(BaseModel):
    """Model for company beneficial owner data."""
    forename: Optional[str] = Field(None, description="First name")
    surname: Optional[str] = Field(None, description="Last name")
    birth_date: Optional[str] = Field(None, description="Birth date")
    nationality: Optional[str] = Field(None, description="Nationality (ISO code)")
    residence: Optional[str] = Field(None, description="Country of residence (ISO code)")
    registered_on: Optional[str] = Field(None, description="Registration date")
    latvian_identity_number_masked: Optional[str] = Field(None, description="Masked Latvian identity number")
    # Add other beneficiary fields as needed

class MemberData(BaseModel):
    """Model for company member data."""
    name: Optional[str] = Field(None, description="Member name")
    entity_type: Optional[str] = Field(None, description="Entity type (NATURAL_PERSON or LEGAL_ENTITY)")
    latvian_identity_number_masked: Optional[str] = Field(None, description="Masked Latvian identity number")
    birth_date: Optional[str] = Field(None, description="Birth date")
    legal_entity_registration_number: Optional[str] = Field(None, description="Legal entity registration number")
    number_of_shares: Optional[str] = Field(None, description="Number of shares")
    share_nominal_value: Optional[str] = Field(None, description="Share nominal value")
    share_currency: Optional[str] = Field(None, description="Share currency")
    date_from: Optional[str] = Field(None, description="Date from")
    registered_on: Optional[str] = Field(None, description="Registration date")
    # Add other member fields as needed

class OfficerData(BaseModel):
    """Model for company officer data."""
    entity_type: Optional[str] = Field(None, description="Entity type")
    position: Optional[str] = Field(None, description="Position")
    governing_body: Optional[str] = Field(None, description="Governing body")
    name: Optional[str] = Field(None, description="Officer name")
    latvian_identity_number_masked: Optional[str] = Field(None, description="Masked Latvian identity number")
    birth_date: Optional[str] = Field(None, description="Birth date")
    legal_entity_registration_number: Optional[str] = Field(None, description="Legal entity registration number")
    rights_of_representation_type: Optional[str] = Field(None, description="Rights of representation type")
    representation_with_at_least: Optional[str] = Field(None, description="Representation with at least")
    registered_on: Optional[str] = Field(None, description="Registration date")
    last_modified_at: Optional[str] = Field(None, description="Last modified date")
    # Add other officer fields as needed

class StockholderData(BaseModel):
    """Model for company stockholder data."""
    entity_type: Optional[str] = Field(None, description="Entity type")
    name: Optional[str] = Field(None, description="Stockholder name")
    latvian_identity_number_masked: Optional[str] = Field(None, description="Masked Latvian identity number")
    birth_date: Optional[str] = Field(None, description="Birth date")
    legal_entity_registration_number: Optional[str] = Field(None, description="Legal entity registration number")
    number_of_shares: Optional[str] = Field(None, description="Number of shares")
    share_nominal_value: Optional[str] = Field(None, description="Share nominal value")
    share_currency: Optional[str] = Field(None, description="Share currency")
    votes: Optional[str] = Field(None, description="Votes")
    stock_type: Optional[str] = Field(None, description="Stock type")
    depository_registration_number: Optional[str] = Field(None, description="Depository registration number")
    depository_name: Optional[str] = Field(None, description="Depository name")
    date_from: Optional[str] = Field(None, description="Date from")
    registered_on: Optional[str] = Field(None, description="Registration date")
    last_modified_at: Optional[str] = Field(None, description="Last modified date")
    # Add other stockholder fields as needed

class BusinessData(BaseModel):
    """Model for company business activity data."""
    legal_entity_registration_number: Optional[str] = Field(None, description="Legal entity registration number")
    name: Optional[str] = Field(None, description="Company name")
    legal_form_code: Optional[str] = Field(None, description="Legal form code")
    legal_form_code_text: Optional[str] = Field(None, description="Legal form code text")
    area_of_activity: Optional[str] = Field(None, description="Area of activity")
    # Add other business fields as needed

class LiquidationData(BaseModel):
    """Model for company liquidation process data."""
    legal_entity_registration_number: Optional[str] = Field(None, description="Legal entity registration number")
    liquidation_type: Optional[str] = Field(None, description="Liquidation type")
    liquidation_type_text: Optional[str] = Field(None, description="Liquidation type text")
    date_from: Optional[str] = Field(None, description="Date from")
    grounds_for_liquidation: Optional[str] = Field(None, description="Grounds for liquidation")
    registered_on: Optional[str] = Field(None, description="Registration date")
    last_modified_at: Optional[str] = Field(None, description="Last modified date")
    # Add other liquidation fields as needed

class CompanyResponse(CompanyBase):
    """Model for company response data."""
    status: Optional[str] = Field(None, description="Company status")
    address: Optional[str] = Field(None, description="Company address")
    founded_date: Optional[str] = Field(None, description="Company founding date")
    
    # Add all fields from the data table - with more flexible types
    regcode: Optional[str] = Field(None, description="Registration code")
    sepa: Optional[str] = Field(None, description="SEPA code")
    name_before_quotes: Optional[str] = Field(None, description="Name before quotes")
    name_in_quotes: Optional[str] = Field(None, description="Name in quotes")
    name_after_quotes: Optional[str] = Field(None, description="Name after quotes")
    without_quotes: Optional[Union[int, str, None]] = Field(None, description="Without quotes")
    regtype: Optional[str] = Field(None, description="Registration type")
    regtype_text: Optional[str] = Field(None, description="Registration type text")
    type: Optional[str] = Field(None, description="Company type")
    type_text: Optional[str] = Field(None, description="Company type text")
    registered: Optional[str] = Field(None, description="Registration date")
    terminated: Optional[str] = Field(None, description="Termination date")
    closed: Optional[str] = Field(None, description="Closed status")
    index: Optional[Union[int, str, None]] = Field(None, description="Postal index")
    addressid: Optional[Union[int, str, None]] = Field(None, description="Address ID")
    region: Optional[Union[int, str, None]] = Field(None, description="Region")
    city: Optional[Union[int, str, None]] = Field(None, description="City")
    atvk: Optional[Union[int, str, None]] = Field(None, description="ATVK code")
    
    # Add capital data field to hold data from the second source
    capital_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company capital data")
    
    # Add beneficial owner data field to hold data from the third source
    beneficiary_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company beneficial owners")
    
    # Add members data field to hold data from the fourth source
    members_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company members data")
    
    # Add business activity data field to hold data from the fifth source
    business_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company business activity data")
    
    # Add liquidation data field to hold data from the sixth source
    liquidation_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company liquidation process data")
    
    # Add officers data field to hold data from the seventh source
    officers_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company officers data")
    
    # Add stockholders data field to hold data from the eighth source
    stockholders_data: Optional[List[Dict[str, Any]]] = Field(None, description="Company stockholders data")
    
    # Flag to indicate if the company has any liquidation processes
    has_liquidation_process: bool = Field(False, description="Flag indicating if the company has liquidation processes")
    
    # Flag to indicate if the company is an AS type (Akciju Sabiedrība)
    is_stock_company: bool = Field(False, description="Flag indicating if the company is a stock company (AS)")
    
    registry_data: Optional[Dict[str, Any]] = Field(None, description="Raw registry data")
    
    class Config:
        """Pydantic config."""
        from_attributes = True
        
class CompanyListResponse(BaseModel):
    """Model for company list response."""
    count: int = Field(..., description="Total number of results")
    companies: List[CompanyResponse] = Field(..., description="List of companies")
    
    class Config:
        """Pydantic config."""
        from_attributes = True

class SearchHistoryItem(BaseModel):
    """Model for search history item."""
    reg_number: str = Field(..., description="Company registration number")
    name: str = Field(..., description="Company name")
    search_time: str = Field(..., description="Search timestamp") 