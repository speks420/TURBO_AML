"""
Company details endpoints for the API.
"""
from fastapi import APIRouter, Path, HTTPException, Depends, Request, Response
from app.api.dependencies import CKANService, SupabaseService
from app.models.company import CompanyResponse, SearchHistoryItem
from datetime import datetime
import json

router = APIRouter()

@router.get("/company/{reg_number}", response_model=CompanyResponse)
async def get_company_details(
    request: Request,
    response: Response,
    reg_number: str = Path(..., description="Company registration number"),
    ckan_service: CKANService = None,
    supabase_service: SupabaseService = None,
):
    """
    Get detailed information for a specific company.
    """
    try:
        # Get company details from CKAN API
        record = ckan_service.get_company_by_reg_number(reg_number)
        
        if not record:
            raise HTTPException(status_code=404, detail=f"Company with registration number {reg_number} not found")
        
        # Try to get supplementary data from Supabase
        try:
            supabase_data = supabase_service.get_company_data(reg_number)
            # Merge data if available
            if supabase_data:
                # Update only the fields that exist in Supabase data
                for key, value in supabase_data.items():
                    if key not in record and value is not None:
                        record[key] = value
        except Exception as supabase_error:
            # Log the error but continue with CKAN data
            print(f"Error getting Supabase data: {supabase_error}")
        
        # Get company capital data from second CKAN resource
        capital_data = []
        try:
            capital_records = ckan_service.get_company_capital_data(reg_number)
            # Convert all capital records to have string values
            for capital_record in capital_records:
                capital_record_clean = {}
                for key, value in capital_record.items():
                    if value is not None:
                        capital_record_clean[key] = str(value)
                    else:
                        capital_record_clean[key] = None
                capital_data.append(capital_record_clean)
            print(f"Found {len(capital_data)} capital records for company {reg_number}")
        except Exception as capital_error:
            # Log the error but continue without capital data
            print(f"Error getting capital data: {capital_error}")
            
        # Get company beneficial owners from third CKAN resource
        beneficiary_data = []
        try:
            beneficiary_records = ckan_service.get_company_beneficiaries(reg_number)
            # Convert all beneficiary records to have string values
            for beneficiary_record in beneficiary_records:
                beneficiary_record_clean = {}
                for key, value in beneficiary_record.items():
                    if value is not None:
                        beneficiary_record_clean[key] = str(value)
                    else:
                        beneficiary_record_clean[key] = None
                beneficiary_data.append(beneficiary_record_clean)
            print(f"Found {len(beneficiary_data)} beneficiary records for company {reg_number}")
        except Exception as beneficiary_error:
            # Log the error but continue without beneficiary data
            print(f"Error getting beneficiary data: {beneficiary_error}")
            
        # Get company members data from fourth CKAN resource
        members_data = []
        try:
            members_records = ckan_service.get_company_members(reg_number)
            # Convert all members records to have string values
            for member_record in members_records:
                member_record_clean = {}
                for key, value in member_record.items():
                    if value is not None:
                        member_record_clean[key] = str(value)
                    else:
                        member_record_clean[key] = None
                members_data.append(member_record_clean)
            print(f"Found {len(members_data)} member records for company {reg_number}")
        except Exception as members_error:
            # Log the error but continue without members data
            print(f"Error getting members data: {members_error}")
            
        # Get company business activity data from fifth CKAN resource
        business_data = []
        try:
            business_records = ckan_service.get_company_business_data(reg_number)
            # Convert all business records to have string values
            for business_record in business_records:
                business_record_clean = {}
                for key, value in business_record.items():
                    if value is not None:
                        business_record_clean[key] = str(value)
                    else:
                        business_record_clean[key] = None
                business_data.append(business_record_clean)
            print(f"Found {len(business_data)} business activity records for company {reg_number}")
        except Exception as business_error:
            # Log the error but continue without business data
            print(f"Error getting business activity data: {business_error}")
            
        # Get company liquidation data from sixth CKAN resource
        liquidation_data = []
        has_liquidation_process = False
        try:
            liquidation_records = ckan_service.get_company_liquidation_data(reg_number)
            # Convert all liquidation records to have string values
            for liquidation_record in liquidation_records:
                liquidation_record_clean = {}
                for key, value in liquidation_record.items():
                    if value is not None:
                        liquidation_record_clean[key] = str(value)
                    else:
                        liquidation_record_clean[key] = None
                liquidation_data.append(liquidation_record_clean)
            
            # Set has_liquidation_process flag if any liquidation records exist
            has_liquidation_process = len(liquidation_data) > 0
            print(f"Found {len(liquidation_data)} liquidation records for company {reg_number}")
            print(f"Company has liquidation process: {has_liquidation_process}")
        except Exception as liquidation_error:
            # Log the error but continue without liquidation data
            print(f"Error getting liquidation data: {liquidation_error}")
            
        # Get company officers data from seventh CKAN resource
        officers_data = []
        try:
            officers_records = ckan_service.get_company_officers(reg_number)
            # Convert all officers records to have string values
            for officer_record in officers_records:
                officer_record_clean = {}
                for key, value in officer_record.items():
                    if value is not None:
                        officer_record_clean[key] = str(value)
                    else:
                        officer_record_clean[key] = None
                officers_data.append(officer_record_clean)
            print(f"Found {len(officers_data)} officer records for company {reg_number}")
        except Exception as officers_error:
            # Log the error but continue without officers data
            print(f"Error getting officers data: {officers_error}")
            
        # Get company stockholders data from eighth CKAN resource
        stockholders_data = []
        try:
            stockholders_records = ckan_service.get_company_stockholders(reg_number)
            # Convert all stockholders records to have string values
            for stockholder_record in stockholders_records:
                stockholder_record_clean = {}
                for key, value in stockholder_record.items():
                    if value is not None:
                        stockholder_record_clean[key] = str(value)
                    else:
                        stockholder_record_clean[key] = None
                stockholders_data.append(stockholder_record_clean)
            print(f"Found {len(stockholders_data)} stockholder records for company {reg_number}")
        except Exception as stockholders_error:
            # Log the error but continue without stockholders data
            print(f"Error getting stockholders data: {stockholders_error}")
        
        # Check if company is of type AS (Akciju Sabiedrība)
        is_stock_company = False
        try:
            if record.get("type_text") == "Akciju Sabiedrība" or record.get("type") == "AS":
                is_stock_company = True
            print(f"Company is stock company (AS): {is_stock_company}")
        except Exception as type_error:
            # Log the error but continue
            print(f"Error checking company type: {type_error}")
        
        # Store search in history cookie
        company_name = record.get("name", "")
        try:
            search_history = request.cookies.get("search_history", "[]")
            search_history = json.loads(search_history)
            
            # Create new history entry
            new_entry = {
                "reg_number": reg_number,
                "name": company_name,
                "search_time": datetime.now().isoformat()
            }
            
            # Check if this company is already in history
            existing_entries = [entry for entry in search_history if entry.get("reg_number") == reg_number]
            if existing_entries:
                # Update existing entry
                for entry in existing_entries:
                    entry["search_time"] = new_entry["search_time"]
            else:
                # Add new entry
                search_history.append(new_entry)
                
            # Limit history to 10 most recent searches
            search_history = sorted(search_history, key=lambda x: x["search_time"], reverse=True)[:10]
            
            # Store updated history for middleware to handle
            response.cookies = {"search_history": json.dumps(search_history)}
        except Exception as history_error:
            # Log the error but continue
            print(f"Error updating search history: {history_error}")
        
        # Print record keys and types to debug
        print(f"Company details fields: {list(record.keys())}")
        
        # Convert fields to string to avoid type errors
        record_clean = {}
        for key, value in record.items():
            # Convert all values to strings for safety
            if value is not None:
                record_clean[key] = str(value)
            else:
                record_clean[key] = None
        
        # Convert to our response model - map from regcode to registration_number 
        # and include all other fields directly
        try:
            company = CompanyResponse(
                registration_number=record_clean.get("regcode", ""),
                name=record_clean.get("name", ""),
                status=record_clean.get("status", ""),
                address=record_clean.get("address", ""),
                founded_date=record_clean.get("registered", ""),  # Use 'registered' field for founded date
                # Add direct mapping of all the fields - all as strings now
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
                # Add the capital data
                capital_data=capital_data,
                # Add the beneficiary data
                beneficiary_data=beneficiary_data,
                # Add the members data
                members_data=members_data,
                # Add the business activity data
                business_data=business_data,
                # Add the liquidation data and flag
                liquidation_data=liquidation_data,
                has_liquidation_process=has_liquidation_process,
                # Add the officers data
                officers_data=officers_data,
                # Add the stockholders data and flag
                stockholders_data=stockholders_data,
                is_stock_company=is_stock_company,
                registry_data=record  # Keep original data in registry_data
            )
            return company
        except Exception as validation_error:
            print(f"Validation error for company details: {validation_error}")
            raise
    except HTTPException:
        raise
    except Exception as e:
        # Print detailed error for debugging
        import traceback
        print(f"Company details error: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error getting company details: {str(e)}")

@router.get("/search-history", response_model=list[SearchHistoryItem])
async def get_search_history(request: Request):
    """
    Get the user's company search history.
    """
    try:
        search_history = request.cookies.get("search_history", "[]")
        return json.loads(search_history)
    except Exception as e:
        print(f"Error getting search history: {e}")
        return [] 