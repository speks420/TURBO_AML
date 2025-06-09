from fastapi import APIRouter, Path, HTTPException, Query
from typing import Optional
from app.services.ckan_service import ckan_service
from app.services.financial_analysis import financial_analysis_service
from app.models.financial import BalanceSheet, IncomeStatement, CashFlowStatement, FinancialHealthAssessment

router = APIRouter()

@router.get("/financial/{reg_number}/statements")
async def get_financial_statements(
    reg_number: str = Path(..., description="Company registration number"),
    year: Optional[int] = Query(None, description="Specific year (optional)")
):
    """Get comprehensive financial statements for a company."""
    try:
        if year:
            balance_sheets = ckan_service.get_balance_sheets(reg_number, year)
            income_statements = ckan_service.get_income_statements(reg_number, year)
            cash_flows = ckan_service.get_cash_flow_statements(reg_number, year)
            statements_info = [stmt for stmt in ckan_service.get_financial_statements(reg_number) if stmt.get("year") == year]
        else:
            multi_year_data = ckan_service.get_multi_year_financial_data(reg_number)
            balance_sheets = multi_year_data.get("balance_sheets", [])
            income_statements = multi_year_data.get("income_statements", [])
            cash_flows = multi_year_data.get("cash_flows", [])
            statements_info = multi_year_data.get("basic_info", [])

        years_with_data = sorted(list(set(
            [stmt.get("year") for stmt in statements_info if stmt.get("year")] +
            [sheet.get("year") for sheet in balance_sheets if sheet.get("year")] +
            [stmt.get("year") for stmt in income_statements if stmt.get("year")] +
            [flow.get("year") for flow in cash_flows if flow.get("year")]
        )), reverse=True)

        return {
            "registration_number": reg_number,
            "statements_info": statements_info,
            "balance_sheets": balance_sheets,
            "income_statements": income_statements,
            "cash_flow_statements": cash_flows,
            "data_availability": {
                "balance_sheets": len(balance_sheets) > 0,
                "income_statements": len(income_statements) > 0,
                "cash_flows": len(cash_flows) > 0
            },
            "years_with_data": years_with_data,
            "last_financial_year": years_with_data[0] if years_with_data else None
        }

    except Exception as e:
        print(f"Financial statements error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving financial statements: {str(e)}")

@router.get("/financial/{reg_number}/balance-sheet")
async def get_balance_sheet_data(
    reg_number: str = Path(..., description="Company registration number"),
    year: Optional[int] = Query(None, description="Specific year (optional)")
):
    """Get balance sheet data for a company."""
    try:
        balance_sheets = ckan_service.get_balance_sheets(reg_number, year)
        
        if not balance_sheets:
            raise HTTPException(status_code=404, detail=f"No balance sheet data found for company {reg_number}")

        return {
            "registration_number": reg_number,
            "balance_sheets": balance_sheets,
            "years_available": sorted(list(set([sheet.get("year") for sheet in balance_sheets if sheet.get("year")])), reverse=True)
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"Balance sheet error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving balance sheet data: {str(e)}")

@router.get("/financial/{reg_number}/income-statement")
async def get_income_statement_data(
    reg_number: str = Path(..., description="Company registration number"),
    year: Optional[int] = Query(None, description="Specific year (optional)")
):
    """Get income statement data for a company."""
    try:
        income_statements = ckan_service.get_income_statements(reg_number, year)
        
        if not income_statements:
            raise HTTPException(status_code=404, detail=f"No income statement data found for company {reg_number}")

        return {
            "registration_number": reg_number,
            "income_statements": income_statements,
            "years_available": sorted(list(set([stmt.get("year") for stmt in income_statements if stmt.get("year")])), reverse=True)
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"Income statement error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving income statement data: {str(e)}")

@router.get("/financial/{reg_number}/cash-flow")
async def get_cash_flow_data(
    reg_number: str = Path(..., description="Company registration number"),
    year: Optional[int] = Query(None, description="Specific year (optional)")
):
    """Get cash flow statement data for a company."""
    try:
        cash_flows = ckan_service.get_cash_flow_statements(reg_number, year)
        
        if not cash_flows:
            raise HTTPException(status_code=404, detail=f"No cash flow data found for company {reg_number}")

        return {
            "registration_number": reg_number,
            "cash_flow_statements": cash_flows,
            "years_available": sorted(list(set([flow.get("year") for flow in cash_flows if flow.get("year")])), reverse=True)
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"Cash flow error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving cash flow data: {str(e)}")

@router.get("/financial/{reg_number}/test")
async def test_financial_data(reg_number: str):
    """Simple test endpoint to check if financial data exists."""
    try:
        statements = ckan_service.get_financial_statements(reg_number)
        return {
            "registration_number": reg_number,
            "message": "Financial endpoint working!",
            "statements_found": len(statements),
            "statements_sample": statements[:2] if statements else []
        }
    except Exception as e:
        return {
            "registration_number": reg_number,
            "message": "Financial endpoint working, but no data found",
            "error": str(e)
        }

@router.get("/financial/{reg_number}/debug")
async def debug_financial_data(reg_number: str):
    """DEBUG: See actual field names and data structure from CKAN API."""
    try:
        print(f"\n🔍 DEBUG: Checking financial data for {reg_number}")
        
        # Get raw data from all sources
        balance_sheets = ckan_service.get_balance_sheets(reg_number)
        income_statements = ckan_service.get_income_statements(reg_number)
        cash_flows = ckan_service.get_cash_flow_statements(reg_number)
        statements_info = ckan_service.get_financial_statements(reg_number)
        
        # Debug output
        debug_info = {
            "registration_number": reg_number,
            "timestamp": "Debug info",
            "balance_sheets": {
                "count": len(balance_sheets),
                "sample_fields": list(balance_sheets[0].keys()) if balance_sheets else [],
                "sample_data": balance_sheets[0] if balance_sheets else None
            },
            "income_statements": {
                "count": len(income_statements),
                "sample_fields": list(income_statements[0].keys()) if income_statements else [],
                "sample_data": income_statements[0] if income_statements else None
            },
            "cash_flows": {
                "count": len(cash_flows),
                "sample_fields": list(cash_flows[0].keys()) if cash_flows else [],
                "sample_data": cash_flows[0] if cash_flows else None
            },
            "statements_info": {
                "count": len(statements_info),
                "sample_fields": list(statements_info[0].keys()) if statements_info else [],
                "sample_data": statements_info[0] if statements_info else None
            }
        }
        
        print(f"Balance Sheet Fields: {debug_info['balance_sheets']['sample_fields']}")
        print(f"Income Statement Fields: {debug_info['income_statements']['sample_fields']}")
        print(f"Cash Flow Fields: {debug_info['cash_flows']['sample_fields']}")
        
        return debug_info
        
    except Exception as e:
        return {
            "registration_number": reg_number,
            "error": str(e),
            "message": "Error during debug - check console logs"
        }

@router.get("/financial/{reg_number}/health-score", response_model=FinancialHealthAssessment)
async def get_company_health_score(
    reg_number: str = Path(..., description="Company registration number"),
    years: Optional[int] = Query(5, description="Number of years to analyze")
):
    """Get comprehensive financial health score including taxpayer ratings."""
    try:
        # Get financial data
        multi_year_data = ckan_service.get_multi_year_financial_data(reg_number, years)
        balance_sheets_data = multi_year_data.get("balance_sheets", [])
        income_statements_data = multi_year_data.get("income_statements", [])
        cash_flows_data = multi_year_data.get("cash_flows", [])
        
        # Get taxpayer ratings
        taxpayer_ratings = ckan_service.get_taxpayer_ratings(reg_number)
        
        if not balance_sheets_data or not income_statements_data:
            raise HTTPException(status_code=404, detail=f"Insufficient financial data for health assessment of company {reg_number}")
        
        # Convert to Pydantic models
        balance_sheets = [BalanceSheet(**sheet) for sheet in balance_sheets_data]
        income_statements = [IncomeStatement(**stmt) for stmt in income_statements_data]
        cash_flows = [CashFlowStatement(**flow) for flow in cash_flows_data] if cash_flows_data else None
        
        # Calculate health score with taxpayer ratings
        health_assessment = financial_analysis_service.calculate_health_score(
            registration_number=reg_number,
            balance_sheets=balance_sheets,
            income_statements=income_statements,
            cash_flows=cash_flows,
            taxpayer_ratings=taxpayer_ratings
        )
        
        return health_assessment
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Health score calculation error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error calculating health score: {str(e)}")
