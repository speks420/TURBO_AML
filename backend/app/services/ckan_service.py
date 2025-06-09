"""
Service for interacting with the CKAN API.
"""
import ckanapi
from app.core.config import settings

class CKANService:
    """Service for interacting with the CKAN API."""
    
    def __init__(self):
        """Initialize the CKAN API client."""
        self.client = ckanapi.RemoteCKAN(settings.CKAN_BASE_URL)
        
        # Company data resources
        self.company_resource_id = settings.CKAN_COMPANY_RESOURCE_ID
        self.capital_resource_id = settings.CKAN_CAPITAL_RESOURCE_ID
        self.beneficiary_resource_id = settings.CKAN_BENEFICIARY_RESOURCE_ID
        self.members_resource_id = settings.CKAN_MEMBERS_RESOURCE_ID
        self.business_resource_id = settings.CKAN_BUSINESS_RESOURCE_ID
        self.liquidation_resource_id = settings.CKAN_LIQUIDATION_RESOURCE_ID
        self.officers_resource_id = settings.CKAN_OFFICERS_RESOURCE_ID
        self.stockholders_resource_id = settings.CKAN_STOCKHOLDERS_RESOURCE_ID
        self.taxpayer_ratings_resource_id = settings.CKAN_TAXPAYER_RATINGS_RESOURCE_ID
        
        # Financial data resources
        self.financial_statements_resource_id = settings.CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID
        self.balance_sheets_resource_id = settings.CKAN_BALANCE_SHEETS_RESOURCE_ID
        self.income_statements_resource_id = settings.CKAN_INCOME_STATEMENTS_RESOURCE_ID
        self.cash_flow_statements_resource_id = settings.CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID
    
    def search_companies(self, query: str, limit: int = 10, offset: int = 0):
        """
        Search for companies using the CKAN API.
        
        Args:
            query: The search query
            limit: Maximum number of results to return
            offset: Offset for pagination
            
        Returns:
            The search results
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.company_resource_id,
                q=query,
                limit=limit,
                offset=offset
            )
            return result
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error: {e}")
            raise
    
    def get_company_by_reg_number(self, reg_number: str):
        """
        Get company details by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company details
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.company_resource_id,
                filters={"regcode": reg_number}
            )
            
            # Return the first record if any
            records = result.get("records", [])
            return records[0] if records else None
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error: {e}")
            raise
            
    def get_company_capital_data(self, reg_number: str):
        """
        Get company capital data by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company capital data records
        """
        try:
            # Changed from 'regcode' to 'legal_entity_registration_number' based on actual data schema
            result = self.client.action.datastore_search(
                resource_id=self.capital_resource_id,
                filters={"legal_entity_registration_number": reg_number}
            )
            
            # Return all records as capital data may have multiple entries
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching capital data: {e}")
            return []
    
    def get_company_beneficiaries(self, reg_number: str):
        """
        Get company beneficial owners by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company beneficial owners records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.beneficiary_resource_id,
                filters={"legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple beneficial owners
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching beneficiary data: {e}")
            return []
            
    def get_company_members(self, reg_number: str):
        """
        Get company members data by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company members records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.members_resource_id,
                filters={"at_legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple members
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching members data: {e}")
            return []
            
    def get_company_business_data(self, reg_number: str):
        """
        Get company business activity data by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company business activity records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.business_resource_id,
                filters={"legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple business activities
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching business activity data: {e}")
            return []
            
    def get_company_liquidation_data(self, reg_number: str):
        """
        Get company liquidation process data by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company liquidation process records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.liquidation_resource_id,
                filters={"legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple liquidation processes
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching liquidation data: {e}")
            return []
            
    def get_company_officers(self, reg_number: str):
        """
        Get company officers data by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company officers records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.officers_resource_id,
                filters={"at_legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple officers
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching officers data: {e}")
            return []
            
    def get_company_stockholders(self, reg_number: str):
        """
        Get company stockholders data by registration number.
        This will only return data for companies of type 'Akciju Sabiedrība' (AS).
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The company stockholders records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.stockholders_resource_id,
                filters={"at_legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple stockholders
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching stockholders data: {e}")
            return []
            
    def get_taxpayer_ratings(self, reg_number: str):
        """
        Get taxpayer rating data by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The taxpayer rating records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.taxpayer_ratings_resource_id,
                filters={"registracijas_kods": reg_number}
            )
            
            # Return all records as a company may have multiple rating entries
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching taxpayer ratings: {e}")
            return []
            
    # ===== FINANCIAL DATA METHODS =====
    
    def get_financial_statements(self, reg_number: str):
        """
        Get annual report basic information by registration number.
        
        Args:
            reg_number: The company registration number
            
        Returns:
            The annual report basic information records
        """
        try:
            result = self.client.action.datastore_search(
                resource_id=self.financial_statements_resource_id,
                filters={"legal_entity_registration_number": reg_number}
            )
            
            # Return all records as a company may have multiple years
            records = result.get("records", [])
            return records
        except ckanapi.errors.CKANAPIError as e:
            # Log error and reraise
            print(f"CKAN API error when fetching financial statements: {e}")
            return []
    
    def get_balance_sheets(self, reg_number: str, year: int = None):
        """
        Get balance sheet data by registration number and optionally by year.
        
        Args:
            reg_number: The company registration number
            year: Optional specific year to filter by
            
        Returns:
            The balance sheet records
        """
        try:
            # First get the statement IDs from financial statements
            financial_statements = self.get_financial_statements(reg_number)
            if not financial_statements:
                return []
            
            statement_ids = [str(stmt["id"]) for stmt in financial_statements]
            if year:
                # Filter by year if specified
                statement_ids = [str(stmt["id"]) for stmt in financial_statements if stmt.get("year") == year]
            
            # Get balance sheet data using statement IDs
            all_balance_sheets = []
            for statement_id in statement_ids:
                result = self.client.action.datastore_search(
                    resource_id=self.balance_sheets_resource_id,
                    filters={"statement_id": statement_id}
                )
                records = result.get("records", [])
                # Add year information to each record
                for record in records:
                    matching_stmt = next((stmt for stmt in financial_statements if str(stmt["id"]) == statement_id), None)
                    if matching_stmt:
                        record["year"] = matching_stmt.get("year")
                        record["currency"] = matching_stmt.get("currency")
                all_balance_sheets.extend(records)
            
            return all_balance_sheets
        except ckanapi.errors.CKANAPIError as e:
            print(f"CKAN API error when fetching balance sheets: {e}")
            return []
    
    def get_income_statements(self, reg_number: str, year: int = None):
        """
        Get income statement data by registration number and optionally by year.
        
        Args:
            reg_number: The company registration number
            year: Optional specific year to filter by
            
        Returns:
            The income statement records
        """
        try:
            # First get the statement IDs from financial statements
            financial_statements = self.get_financial_statements(reg_number)
            if not financial_statements:
                return []
            
            statement_ids = [str(stmt["id"]) for stmt in financial_statements]
            if year:
                # Filter by year if specified
                statement_ids = [str(stmt["id"]) for stmt in financial_statements if stmt.get("year") == year]
            
            # Get income statement data using statement IDs
            all_income_statements = []
            for statement_id in statement_ids:
                result = self.client.action.datastore_search(
                    resource_id=self.income_statements_resource_id,
                    filters={"statement_id": statement_id}
                )
                records = result.get("records", [])
                # Add year information to each record
                for record in records:
                    matching_stmt = next((stmt for stmt in financial_statements if str(stmt["id"]) == statement_id), None)
                    if matching_stmt:
                        record["year"] = matching_stmt.get("year")
                        record["currency"] = matching_stmt.get("currency")
                all_income_statements.extend(records)
            
            return all_income_statements
        except ckanapi.errors.CKANAPIError as e:
            print(f"CKAN API error when fetching income statements: {e}")
            return []
    
    def get_cash_flow_statements(self, reg_number: str, year: int = None):
        """
        Get cash flow statement data by registration number and optionally by year.
        
        Args:
            reg_number: The company registration number
            year: Optional specific year to filter by
            
        Returns:
            The cash flow statement records
        """
        try:
            # First get the statement IDs from financial statements
            financial_statements = self.get_financial_statements(reg_number)
            if not financial_statements:
                return []
            
            statement_ids = [str(stmt["id"]) for stmt in financial_statements]
            if year:
                # Filter by year if specified
                statement_ids = [str(stmt["id"]) for stmt in financial_statements if stmt.get("year") == year]
            
            # Get cash flow statement data using statement IDs
            all_cash_flows = []
            for statement_id in statement_ids:
                result = self.client.action.datastore_search(
                    resource_id=self.cash_flow_statements_resource_id,
                    filters={"statement_id": statement_id}
                )
                records = result.get("records", [])
                # Add year information to each record
                for record in records:
                    matching_stmt = next((stmt for stmt in financial_statements if str(stmt["id"]) == statement_id), None)
                    if matching_stmt:
                        record["year"] = matching_stmt.get("year")
                        record["currency"] = matching_stmt.get("currency")
                all_cash_flows.extend(records)
            
            return all_cash_flows
        except ckanapi.errors.CKANAPIError as e:
            print(f"CKAN API error when fetching cash flow statements: {e}")
            return []
    
    def get_multi_year_financial_data(self, reg_number: str, years: int = 5):
        """
        Get comprehensive multi-year financial data for trend analysis.
        
        Args:
            reg_number: The company registration number
            years: Number of years to retrieve (default: 5)
            
        Returns:
            Dictionary with organized financial data by year
        """
        try:
            # Get basic financial statements info
            financial_statements = self.get_financial_statements(reg_number)
            if not financial_statements:
                return {}
            
            # Sort by year descending and limit to requested years
            financial_statements = sorted(financial_statements, key=lambda x: x.get("year", 0), reverse=True)[:years]
            
            result = {
                "years": [],
                "balance_sheets": [],
                "income_statements": [],
                "cash_flows": [],
                "basic_info": financial_statements
            }
            
            for stmt in financial_statements:
                year = stmt.get("year")
                result["years"].append(year)
                
                # Get data for each year
                balance_data = self.get_balance_sheets(reg_number, year)
                income_data = self.get_income_statements(reg_number, year)
                cash_flow_data = self.get_cash_flow_statements(reg_number, year)
                
                result["balance_sheets"].extend(balance_data)
                result["income_statements"].extend(income_data)
                result["cash_flows"].extend(cash_flow_data)
            
            return result
        except Exception as e:
            print(f"Error getting multi-year financial data: {e}")
            return {}

# Create a singleton instance
ckan_service = CKANService() 