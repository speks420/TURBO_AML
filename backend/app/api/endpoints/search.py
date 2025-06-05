"""
Search endpoints for the API.
"""
from fastapi import APIRouter, Query, HTTPException
from app.api.dependencies import CKANService, SupabaseService
from app.models.company import CompanySearch, CompanyListResponse, CompanyResponse

router = APIRouter()

@router.get("/search", response_model=CompanyListResponse)
async def search_companies(
    q: str = Query(..., description="Search query"),
    limit: int = Query(10, description="Maximum number of results to return"),
    offset: int = Query(0, description="Offset for pagination"),
    ckan_service: CKANService = None,
    supabase_service: SupabaseService = None,
):
    """
    Search for companies by name, registration number, etc.
    """
    try:
        # Search using CKAN API
        result = ckan_service.search_companies(q, limit, offset)
        
        # Process the response into our model
        records = result.get("records", [])
        total = result.get("total", len(records))
        
        # Convert to our response model
        companies = []
        for record in records:
            # Print record keys and types to debug
            print(f"Record fields: {list(record.keys())}")
            # Manually convert types that could cause issues
            record_clean = {}
            for key, value in record.items():
                # Convert all values to strings for safety
                if value is not None:
                    record_clean[key] = str(value)
                else:
                    record_clean[key] = None
            
            try:
                company = CompanyResponse(
                    registration_number=record_clean.get("regcode", ""),
                    name=record_clean.get("name", ""),
                    status=record_clean.get("status", ""),
                    address=record_clean.get("address", ""),
                    founded_date=record_clean.get("registered", ""),
                    # Add direct mapping of all the fields - all as strings
                    regcode=record_clean.get("regcode", ""),
                    sepa=record_clean.get("sepa", ""),
                    name_before_quotes=record_clean.get("name_before_quotes", ""),
                    name_in_quotes=record_clean.get("name_in_quotes", ""),
                    name_after_quotes=record_clean.get("name_after_quotes", ""),
                    without_quotes=record_clean.get("without_quotes", ""),
                    regtype=record_clean.get("regtype", ""),
                    regtype_text=record_clean.get("regtype_text", ""),
                    type=record_clean.get("type", ""),
                    type_text=record_clean.get("type_text", ""),
                    registered=record_clean.get("registered", ""),
                    terminated=record_clean.get("terminated", ""),
                    closed=record_clean.get("closed", ""),
                    index=record_clean.get("index", ""),
                    addressid=record_clean.get("addressid", ""),
                    region=record_clean.get("region", ""),
                    city=record_clean.get("city", ""),
                    atvk=record_clean.get("atvk", ""),
                    registry_data=record
                )
                companies.append(company)
            except Exception as validation_error:
                print(f"Validation error for record: {validation_error}")
                # Continue without this record
        
        return CompanyListResponse(count=total, companies=companies)
    except Exception as e:
        # Print detailed error for debugging
        import traceback
        print(f"Search error: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error searching companies: {str(e)}")
 