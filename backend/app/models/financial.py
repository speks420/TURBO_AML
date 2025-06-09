"""
Financial data models for TURBO_AML.
Based on Latvia's CKAN API financial statement data structure.
"""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


# ===== ANNUAL REPORT BASIC INFORMATION =====
class FinancialStatementInfo(BaseModel):
    """Annual Report Basic Information (Gada pārskatu pamatinformācija)."""
    id: Optional[int] = None
    file_id: Optional[int] = None
    legal_entity_registration_number: Optional[str] = None
    source_schema: Optional[str] = None
    source_type: Optional[str] = None
    year: Optional[int] = None
    year_started_on: Optional[datetime] = None
    year_ended_on: Optional[datetime] = None
    employees: Optional[int] = None
    rounded_to_nearest: Optional[str] = None  # ONES, THOUSANDS, MILLIONS
    currency: Optional[str] = None  # EUR, LVL
    created_at: Optional[datetime] = None


# ===== BALANCE SHEET DATA =====
class BalanceSheet(BaseModel):
    """Balance Sheet (Bilances) data model."""
    statement_id: Optional[int] = None
    file_id: Optional[int] = None
    year: Optional[int] = None  # Added from statement info
    currency: Optional[str] = None  # Added from statement info
    
    # Current Assets (Apgrozāmie līdzekļi)
    cash: Optional[float] = None
    marketable_securities: Optional[float] = None
    accounts_receivable: Optional[float] = None
    inventories: Optional[float] = None
    total_current_assets: Optional[float] = None
    
    # Non-Current Assets (Ilgtermiņa ieguldījumi)
    investments: Optional[float] = None
    fixed_assets: Optional[float] = None
    intangible_assets: Optional[float] = None
    total_non_current_assets: Optional[float] = None
    total_assets: Optional[float] = None
    
    # Liabilities and Equity (Bilances pasīvi)
    future_housing_repairs_payments: Optional[str] = None
    current_liabilities: Optional[float] = None
    non_current_liabilities: Optional[float] = None
    provisions: Optional[float] = None
    equity: Optional[float] = None
    total_equities: Optional[float] = None


# ===== INCOME STATEMENT DATA =====
class IncomeStatement(BaseModel):
    """Income Statement (Peļņas vai zaudējumu aprēķini) data model."""
    statement_id: Optional[int] = None
    file_id: Optional[int] = None
    year: Optional[int] = None  # Added from statement info
    currency: Optional[str] = None  # Added from statement info
    
    # Revenue and Operating Items
    net_turnover: Optional[float] = None
    
    # By Nature Classification
    by_nature_inventory_change: Optional[float] = None
    by_nature_long_term_investment_expenses: Optional[float] = None
    by_nature_other_operating_revenues: Optional[float] = None
    by_nature_material_expenses: Optional[float] = None
    by_nature_labour_expenses: Optional[float] = None
    by_nature_depreciation_expenses: Optional[float] = None
    
    # By Function Classification
    by_function_cost_of_goods_sold: Optional[float] = None
    by_function_gross_profit: Optional[float] = None
    by_function_selling_expenses: Optional[float] = None
    by_function_administrative_expenses: Optional[float] = None
    by_function_other_operating_revenues: Optional[float] = None
    
    # Other Operating and Financial Items
    other_operating_expenses: Optional[float] = None
    equity_investment_earnings: Optional[float] = None
    other_long_term_investment_earnings: Optional[float] = None
    other_interest_revenues: Optional[float] = None
    investment_fair_value_adjustments: Optional[float] = None
    interest_expenses: Optional[float] = None
    
    # Extraordinary Items
    extra_revenues: Optional[float] = None
    extra_expenses: Optional[float] = None
    
    # Profit/Loss Items
    income_before_income_taxes: Optional[float] = None
    provision_for_income_taxes: Optional[float] = None
    income_after_income_taxes: Optional[float] = None
    other_taxes: Optional[float] = None
    extra_dividends: Optional[float] = None
    net_income: Optional[float] = None


# ===== CASH FLOW STATEMENT DATA =====
class CashFlowStatement(BaseModel):
    """Cash Flow Statement (Naudas plūsmas pārskati) data model."""
    statement_id: Optional[int] = None
    file_id: Optional[int] = None
    year: Optional[int] = None  # Added from statement info
    currency: Optional[str] = None  # Added from statement info
    
    # Operating Cash Flow - Direct Method
    cfo_dm_cash_received_from_customers: Optional[float] = None
    cfo_dm_cash_paid_to_suppliers_employees: Optional[float] = None
    cfo_dm_other_cash_received_paid: Optional[float] = None
    cfo_dm_operating_cash_flow: Optional[float] = None
    cfo_dm_interest_paid: Optional[float] = None
    cfo_dm_income_taxes_paid: Optional[float] = None
    cfo_dm_extra_items_cash_flow: Optional[float] = None
    cfo_dm_net_operating_cash_flow: Optional[float] = None
    
    # Operating Cash Flow - Indirect Method
    cfo_im_income_before_income_taxes: Optional[float] = None
    cfo_im_income_before_changes_in_working_capital: Optional[float] = None
    cfo_im_operating_cash_flow: Optional[float] = None
    cfo_im_interest_paid: Optional[float] = None
    cfo_im_income_taxes_paid: Optional[float] = None
    cfo_im_extra_items_cash_flow: Optional[float] = None
    cfo_im_net_operating_cash_flow: Optional[float] = None
    
    # Investing Cash Flow
    cfi_acquisition_of_stocks_shares: Optional[float] = None
    cfi_sale_proceeds_from_stocks_shares: Optional[float] = None
    cfi_acquisition_of_fixed_assets_intangible_assets: Optional[float] = None
    cfi_sale_proceeds_from_fixed_assets_intangible_assets: Optional[float] = None
    cfi_loans_made: Optional[float] = None
    cfi_repayments_of_loans_received: Optional[float] = None
    cfi_interest_received: Optional[float] = None
    cfi_dividends_received: Optional[float] = None
    cfi_net_investing_cash_flow: Optional[float] = None
    
    # Financing Cash Flow
    cff_proceeds_from_stocks_bonds_issuance_or_contributed_capital: Optional[float] = None
    cff_loans_received: Optional[float] = None
    cff_subsidies_grants_donations_received: Optional[float] = None
    cff_repayments_of_loans_made: Optional[float] = None
    cff_repayments_of_lease_obligations: Optional[float] = None
    cff_dividends_paid: Optional[float] = None
    cff_net_financing_cash_flow: Optional[float] = None
    
    # Net Cash Flow
    effect_of_exchange_rate_change: Optional[float] = None
    net_increase: Optional[float] = None
    at_beginning_of_year: Optional[float] = None
    at_end_of_year: Optional[float] = None


# ===== COMPREHENSIVE FINANCIAL DATA =====
class ComprehensiveFinancialData(BaseModel):
    """Complete financial data for a company across multiple years."""
    registration_number: str
    years_available: List[int] = []
    
    # Financial statements by year
    statements_info: List[FinancialStatementInfo] = []
    balance_sheets: List[BalanceSheet] = []
    income_statements: List[IncomeStatement] = []
    cash_flow_statements: List[CashFlowStatement] = []
    
    # Calculated metrics
    financial_health_score: Optional[float] = None
    risk_level: Optional[str] = None  # LOW, MEDIUM, HIGH
    trend_analysis: Optional[Dict[str, Any]] = None
    ratios: Optional[Dict[str, Any]] = None


# ===== FINANCIAL RATIOS =====
class FinancialRatios(BaseModel):
    """Calculated financial ratios for analysis."""
    
    # Liquidity Ratios
    current_ratio: Optional[float] = None  # Current Assets / Current Liabilities
    quick_ratio: Optional[float] = None  # (Current Assets - Inventory) / Current Liabilities
    cash_ratio: Optional[float] = None  # Cash / Current Liabilities
    
    # Profitability Ratios
    gross_profit_margin: Optional[float] = None  # Gross Profit / Revenue
    net_profit_margin: Optional[float] = None  # Net Income / Revenue
    return_on_assets: Optional[float] = None  # Net Income / Total Assets
    return_on_equity: Optional[float] = None  # Net Income / Equity
    
    # Leverage/Solvency Ratios
    debt_to_equity: Optional[float] = None  # Total Debt / Equity
    debt_to_assets: Optional[float] = None  # Total Debt / Total Assets
    equity_ratio: Optional[float] = None  # Equity / Total Assets
    
    # Efficiency Ratios
    asset_turnover: Optional[float] = None  # Revenue / Total Assets
    inventory_turnover: Optional[float] = None  # COGS / Average Inventory
    receivables_turnover: Optional[float] = None  # Revenue / Average Receivables
    
    # Growth Metrics (Year-over-Year)
    revenue_growth: Optional[float] = None
    profit_growth: Optional[float] = None
    assets_growth: Optional[float] = None


# ===== FINANCIAL HEALTH ASSESSMENT =====
class FinancialHealthAssessment(BaseModel):
    """Comprehensive financial health assessment."""
    registration_number: str
    assessment_date: datetime = Field(default_factory=datetime.now)
    
    # Overall Health Score (0-100)
    health_score: float = Field(ge=0, le=100)
    health_grade: str  # A+, A, B+, B, C+, C, D+, D, F
    
    # Component Scores
    liquidity_score: Optional[float] = None
    profitability_score: Optional[float] = None
    solvency_score: Optional[float] = None
    efficiency_score: Optional[float] = None
    growth_score: Optional[float] = None
    taxpayer_rating_score: Optional[float] = None
    
    # Risk Assessment
    risk_level: str  # LOW, MEDIUM, HIGH, CRITICAL
    bankruptcy_risk: Optional[float] = None  # 0-1 probability
    altman_z_score: Optional[float] = None
    
    # Key Indicators
    strengths: List[str] = []
    weaknesses: List[str] = []
    recommendations: List[str] = []
    
    # Trend Analysis
    trend_direction: Optional[str] = None  # IMPROVING, STABLE, DECLINING
    years_analyzed: int = 0


# ===== INDUSTRY BENCHMARKS =====
class IndustryBenchmark(BaseModel):
    """Industry benchmark data for comparison."""
    industry_sector: str
    metric_name: str
    
    # Benchmark Statistics
    median_value: Optional[float] = None
    percentile_25: Optional[float] = None
    percentile_75: Optional[float] = None
    average_value: Optional[float] = None
    
    # Company Comparison
    company_value: Optional[float] = None
    company_percentile: Optional[float] = None
    performance_vs_median: Optional[str] = None  # ABOVE, BELOW, AVERAGE


# ===== API RESPONSE MODELS =====
class FinancialAnalysisResponse(BaseModel):
    """Response model for financial analysis API endpoints."""
    registration_number: str
    company_name: Optional[str] = None
    analysis_date: datetime = Field(default_factory=datetime.now)
    
    # Financial Data
    statements_info: List[FinancialStatementInfo] = []
    balance_sheets: List[BalanceSheet] = []
    income_statements: List[IncomeStatement] = []
    cash_flow_statements: List[CashFlowStatement] = []
    
    # Analysis Results
    health_assessment: Optional[FinancialHealthAssessment] = None
    ratios: Optional[FinancialRatios] = None
    
    # Status Information
    data_availability: Dict[str, bool] = {}  # Which data types are available
    years_with_data: List[int] = []
    last_financial_year: Optional[int] = None


class FinancialTrendsResponse(BaseModel):
    """Response model for multi-year financial trends."""
    registration_number: str
    years_analyzed: List[int] = []
    
    # Trend Data
    revenue_trend: List[Dict[str, Any]] = []
    profit_trend: List[Dict[str, Any]] = []
    assets_trend: List[Dict[str, Any]] = []
    ratios_trend: List[Dict[str, Any]] = []
    
    # Trend Analysis
    growth_rates: Dict[str, float] = {}
    trend_direction: Dict[str, str] = {}
    volatility_metrics: Dict[str, float] = {}
    
    # Forecasting (if enabled)
    predictions: Dict[str, Any] = {}


class RiskAssessmentResponse(BaseModel):
    """Response model for risk assessment analysis."""
    registration_number: str
    assessment_date: datetime = Field(default_factory=datetime.now)
    
    # Risk Scores
    overall_risk_level: str  # LOW, MEDIUM, HIGH, CRITICAL
    risk_score: float = Field(ge=0, le=100)
    
    # Risk Factors
    financial_risk: Optional[float] = None
    operational_risk: Optional[float] = None
    market_risk: Optional[float] = None
    liquidity_risk: Optional[float] = None
    
    # Predictive Models
    bankruptcy_probability: Optional[float] = None
    altman_z_score: Optional[float] = None
    piotroski_f_score: Optional[int] = None
    
    # Risk Indicators
    risk_factors: List[str] = []
    warning_signs: List[str] = []
    positive_indicators: List[str] = []
    
    # Recommendations
    risk_mitigation: List[str] = [] 