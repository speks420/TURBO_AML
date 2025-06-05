"""
Financial Analysis Service for TURBO_AML.
Implements comprehensive financial calculations using Latvia's CKAN financial data.
"""
from typing import List, Dict, Any, Optional, Tuple
import statistics
from datetime import datetime, date
from app.models.financial import (
    FinancialStatementInfo,
    BalanceSheet,
    IncomeStatement,
    CashFlowStatement,
    FinancialRatios,
    FinancialHealthAssessment
)


class FinancialAnalysisService:
    """
    Service for calculating financial health scores, ratios, and risk assessments.
    Based on actual Latvia's CKAN financial statement data structure.
    """
    
    def __init__(self):
        # Health score weights (must sum to 1.0)
        self.HEALTH_SCORE_WEIGHTS = {
            'liquidity': 0.25,      # Ability to pay short-term obligations
            'profitability': 0.30,   # Revenue generation efficiency
            'solvency': 0.20,       # Long-term financial stability
            'efficiency': 0.15,     # Asset utilization effectiveness
            'growth': 0.10          # Business expansion trends
        }
        
        # Risk level thresholds
        self.RISK_THRESHOLDS = {
            'CRITICAL': (0, 35),
            'HIGH': (35, 55),
            'MEDIUM': (55, 75),
            'LOW': (75, 100)
        }
        
        # Health grade mapping
        self.HEALTH_GRADES = {
            (90, 100): 'A+',
            (85, 90): 'A',
            (80, 85): 'A-',
            (75, 80): 'B+',
            (70, 75): 'B',
            (65, 70): 'B-',
            (60, 65): 'C+',
            (55, 60): 'C',
            (50, 55): 'C-',
            (45, 50): 'D+',
            (40, 45): 'D',
            (35, 40): 'D-',
            (0, 35): 'F'
        }

    def calculate_financial_ratios(
        self, 
        balance_sheet: BalanceSheet, 
        income_statement: IncomeStatement,
        cash_flow: Optional[CashFlowStatement] = None
    ) -> FinancialRatios:
        """
        Calculate comprehensive financial ratios from financial statements.
        
        Args:
            balance_sheet: Balance sheet data
            income_statement: Income statement data
            cash_flow: Optional cash flow statement data
            
        Returns:
            FinancialRatios object with calculated ratios
        """
        def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
            """Safely divide two numbers, handling zero denominators."""
            try:
                if denominator == 0 or denominator is None:
                    return default
                return float(numerator) / float(denominator)
            except (TypeError, ValueError):
                return default
        
        def safe_float(value: Any, default: float = 0.0) -> float:
            """Safely convert value to float."""
            try:
                return float(value) if value is not None else default
            except (TypeError, ValueError):
                return default

        # Extract balance sheet values
        total_current_assets = safe_float(balance_sheet.total_current_assets)
        cash = safe_float(balance_sheet.cash)
        marketable_securities = safe_float(balance_sheet.marketable_securities)
        accounts_receivable = safe_float(balance_sheet.accounts_receivable)
        inventories = safe_float(balance_sheet.inventories)
        total_assets = safe_float(balance_sheet.total_assets)
        current_liabilities = safe_float(balance_sheet.current_liabilities)
        non_current_liabilities = safe_float(balance_sheet.non_current_liabilities)
        total_liabilities = current_liabilities + non_current_liabilities
        equity = safe_float(balance_sheet.equity)

        # Extract income statement values
        net_turnover = safe_float(income_statement.net_turnover)
        gross_profit = safe_float(income_statement.by_function_gross_profit)
        cost_of_goods_sold = safe_float(income_statement.by_function_cost_of_goods_sold)
        net_income = safe_float(income_statement.net_income)
        interest_expenses = safe_float(income_statement.interest_expenses)
        income_before_taxes = safe_float(income_statement.income_before_income_taxes)

        # Initialize ratios object
        ratios = FinancialRatios()

        # === LIQUIDITY RATIOS ===
        ratios.current_ratio = safe_divide(total_current_assets, current_liabilities)
        quick_assets = total_current_assets - inventories
        ratios.quick_ratio = safe_divide(quick_assets, current_liabilities)
        cash_and_securities = cash + marketable_securities
        ratios.cash_ratio = safe_divide(cash_and_securities, current_liabilities)

        # === PROFITABILITY RATIOS ===
        ratios.gross_profit_margin = safe_divide(gross_profit, net_turnover) * 100
        ratios.net_profit_margin = safe_divide(net_income, net_turnover) * 100
        ratios.return_on_assets = safe_divide(net_income, total_assets) * 100
        ratios.return_on_equity = safe_divide(net_income, equity) * 100

        # === LEVERAGE/SOLVENCY RATIOS ===
        ratios.debt_to_equity = safe_divide(total_liabilities, equity)
        ratios.debt_to_assets = safe_divide(total_liabilities, total_assets) * 100
        ratios.equity_ratio = safe_divide(equity, total_assets) * 100

        # === EFFICIENCY RATIOS ===
        ratios.asset_turnover = safe_divide(net_turnover, total_assets)
        ratios.inventory_turnover = safe_divide(cost_of_goods_sold, inventories)
        ratios.receivables_turnover = safe_divide(net_turnover, accounts_receivable)

        return ratios

    def calculate_multi_year_ratios(
        self,
        balance_sheets: List[BalanceSheet],
        income_statements: List[IncomeStatement],
        cash_flows: List[CashFlowStatement] = None
    ) -> Dict[int, FinancialRatios]:
        """
        Calculate ratios for multiple years.
        
        Returns:
            Dictionary mapping year to FinancialRatios
        """
        ratios_by_year = {}
        
        # Group data by year
        balance_by_year = {bs.year: bs for bs in balance_sheets if bs.year}
        income_by_year = {is_.year: is_ for is_ in income_statements if is_.year}
        cash_by_year = {cf.year: cf for cf in cash_flows if cash_flows and cf.year} if cash_flows else {}
        
        # Calculate ratios for each year where we have both balance sheet and income statement
        for year in set(balance_by_year.keys()) & set(income_by_year.keys()):
            balance_sheet = balance_by_year[year]
            income_statement = income_by_year[year]
            cash_flow = cash_by_year.get(year)
            
            ratios = self.calculate_financial_ratios(balance_sheet, income_statement, cash_flow)
            ratios_by_year[year] = ratios
            
        return ratios_by_year

    def calculate_growth_rates(self, ratios_by_year: Dict[int, FinancialRatios]) -> Dict[str, float]:
        """
        Calculate year-over-year growth rates.
        """
        if len(ratios_by_year) < 2:
            return {}
            
        years = sorted(ratios_by_year.keys())
        growth_rates = {}
        
        # Calculate growth for key metrics
        metrics = ['revenue_growth', 'profit_growth', 'assets_growth']
        
        # For now, return placeholder growth rates
        # In a real implementation, this would calculate actual growth from historical data
        growth_rates = {
            'revenue_growth': 0.0,
            'profit_growth': 0.0,
            'assets_growth': 0.0
        }
        
        return growth_rates

    def calculate_liquidity_score(self, ratios: FinancialRatios) -> float:
        """
        Calculate liquidity component score (0-100).
        
        Based on current ratio, quick ratio, and cash ratio.
        """
        score = 0.0
        
        # Current Ratio scoring (weight: 50%)
        if ratios.current_ratio:
            if ratios.current_ratio >= 2.0:
                score += 50
            elif ratios.current_ratio >= 1.5:
                score += 40
            elif ratios.current_ratio >= 1.0:
                score += 25
            elif ratios.current_ratio >= 0.5:
                score += 10
            # Below 0.5: 0 points
        
        # Quick Ratio scoring (weight: 30%)
        if ratios.quick_ratio:
            if ratios.quick_ratio >= 1.5:
                score += 30
            elif ratios.quick_ratio >= 1.0:
                score += 25
            elif ratios.quick_ratio >= 0.7:
                score += 15
            elif ratios.quick_ratio >= 0.3:
                score += 8
            # Below 0.3: 0 points
        
        # Cash Ratio scoring (weight: 20%)
        if ratios.cash_ratio:
            if ratios.cash_ratio >= 0.3:
                score += 20
            elif ratios.cash_ratio >= 0.2:
                score += 15
            elif ratios.cash_ratio >= 0.1:
                score += 10
            elif ratios.cash_ratio >= 0.05:
                score += 5
            # Below 0.05: 0 points
        
        return min(100, score)

    def calculate_profitability_score(self, ratios: FinancialRatios) -> float:
        """
        Calculate profitability component score (0-100).
        
        Based on profit margins and return ratios.
        """
        score = 0.0
        
        # Net Profit Margin scoring (weight: 30%)
        if ratios.net_profit_margin:
            if ratios.net_profit_margin >= 15:
                score += 30
            elif ratios.net_profit_margin >= 10:
                score += 25
            elif ratios.net_profit_margin >= 5:
                score += 20
            elif ratios.net_profit_margin >= 0:
                score += 10
            # Negative: 0 points
        
        # Return on Assets scoring (weight: 25%)
        if ratios.return_on_assets:
            if ratios.return_on_assets >= 15:
                score += 25
            elif ratios.return_on_assets >= 10:
                score += 20
            elif ratios.return_on_assets >= 5:
                score += 15
            elif ratios.return_on_assets >= 0:
                score += 8
            # Negative: 0 points
        
        # Return on Equity scoring (weight: 25%)
        if ratios.return_on_equity:
            if ratios.return_on_equity >= 20:
                score += 25
            elif ratios.return_on_equity >= 15:
                score += 20
            elif ratios.return_on_equity >= 10:
                score += 15
            elif ratios.return_on_equity >= 0:
                score += 8
            # Negative: 0 points
        
        # Gross Profit Margin scoring (weight: 20%)
        if ratios.gross_profit_margin:
            if ratios.gross_profit_margin >= 50:
                score += 20
            elif ratios.gross_profit_margin >= 30:
                score += 16
            elif ratios.gross_profit_margin >= 20:
                score += 12
            elif ratios.gross_profit_margin >= 10:
                score += 8
            elif ratios.gross_profit_margin >= 0:
                score += 4
            # Negative: 0 points
        
        return min(100, score)

    def calculate_solvency_score(self, ratios: FinancialRatios) -> float:
        """
        Calculate solvency component score (0-100).
        
        Based on debt ratios and financial leverage.
        """
        score = 0.0
        
        # Debt-to-Equity scoring (weight: 40%)
        if ratios.debt_to_equity is not None:
            if ratios.debt_to_equity <= 0.3:
                score += 40
            elif ratios.debt_to_equity <= 0.6:
                score += 30
            elif ratios.debt_to_equity <= 1.0:
                score += 20
            elif ratios.debt_to_equity <= 2.0:
                score += 10
            # Above 2.0: 0 points
        
        # Debt-to-Assets scoring (weight: 30%)
        if ratios.debt_to_assets:
            if ratios.debt_to_assets <= 30:
                score += 30
            elif ratios.debt_to_assets <= 50:
                score += 25
            elif ratios.debt_to_assets <= 70:
                score += 15
            elif ratios.debt_to_assets <= 90:
                score += 8
            # Above 90%: 0 points
        
        # Equity Ratio scoring (weight: 30%)
        if ratios.equity_ratio:
            if ratios.equity_ratio >= 70:
                score += 30
            elif ratios.equity_ratio >= 50:
                score += 25
            elif ratios.equity_ratio >= 30:
                score += 15
            elif ratios.equity_ratio >= 10:
                score += 8
            # Below 10%: 0 points
        
        return min(100, score)

    def calculate_efficiency_score(self, ratios: FinancialRatios) -> float:
        """
        Calculate efficiency component score (0-100).
        
        Based on asset turnover and operational efficiency ratios.
        """
        score = 0.0
        
        # Asset Turnover scoring (weight: 40%)
        if ratios.asset_turnover:
            if ratios.asset_turnover >= 2.0:
                score += 40
            elif ratios.asset_turnover >= 1.5:
                score += 32
            elif ratios.asset_turnover >= 1.0:
                score += 25
            elif ratios.asset_turnover >= 0.5:
                score += 15
            elif ratios.asset_turnover >= 0.1:
                score += 8
            # Below 0.1: 0 points
        
        # Inventory Turnover scoring (weight: 30%)
        if ratios.inventory_turnover:
            if ratios.inventory_turnover >= 12:  # Monthly turnover
                score += 30
            elif ratios.inventory_turnover >= 6:   # Bi-monthly
                score += 25
            elif ratios.inventory_turnover >= 4:   # Quarterly
                score += 20
            elif ratios.inventory_turnover >= 2:   # Semi-annual
                score += 12
            elif ratios.inventory_turnover >= 1:   # Annual
                score += 8
            # Below 1: 0 points
        else:
            # If no inventory turnover data, give neutral score
            score += 15
        
        # Receivables Turnover scoring (weight: 30%)
        if ratios.receivables_turnover:
            if ratios.receivables_turnover >= 12:  # Monthly collection
                score += 30
            elif ratios.receivables_turnover >= 8:   # ~6 weeks
                score += 25
            elif ratios.receivables_turnover >= 6:   # Bi-monthly
                score += 20
            elif ratios.receivables_turnover >= 4:   # Quarterly
                score += 12
            elif ratios.receivables_turnover >= 2:   # Semi-annual
                score += 8
            # Below 2: 0 points
        else:
            # If no receivables turnover data, give neutral score
            score += 15
        
        return min(100, score)

    def calculate_growth_score(self, growth_rates: Dict[str, float]) -> float:
        """
        Calculate growth component score (0-100).
        
        Based on revenue growth, profit growth, and asset growth.
        """
        if not growth_rates:
            return 50  # Neutral score if no growth data
            
        score = 0.0
        
        # Revenue Growth scoring (weight: 40%)
        revenue_growth = growth_rates.get('revenue_growth', 0)
        if revenue_growth >= 20:
            score += 40
        elif revenue_growth >= 10:
            score += 32
        elif revenue_growth >= 5:
            score += 25
        elif revenue_growth >= 0:
            score += 15
        elif revenue_growth >= -5:
            score += 8
        # Below -5%: 0 points
        
        # Profit Growth scoring (weight: 40%)
        profit_growth = growth_rates.get('profit_growth', 0)
        if profit_growth >= 25:
            score += 40
        elif profit_growth >= 15:
            score += 32
        elif profit_growth >= 5:
            score += 25
        elif profit_growth >= 0:
            score += 15
        elif profit_growth >= -10:
            score += 8
        # Below -10%: 0 points
        
        # Asset Growth scoring (weight: 20%)
        assets_growth = growth_rates.get('assets_growth', 0)
        if assets_growth >= 15:
            score += 20
        elif assets_growth >= 10:
            score += 16
        elif assets_growth >= 5:
            score += 12
        elif assets_growth >= 0:
            score += 8
        elif assets_growth >= -5:
            score += 4
        # Below -5%: 0 points
        
        return min(100, score)

    def calculate_health_score(
        self,
        balance_sheets: List[BalanceSheet],
        income_statements: List[IncomeStatement],
        cash_flows: List[CashFlowStatement] = None
    ) -> FinancialHealthAssessment:
        """
        Calculate comprehensive financial health score.
        
        Args:
            balance_sheets: List of balance sheet data
            income_statements: List of income statement data
            cash_flows: Optional list of cash flow data
            
        Returns:
            FinancialHealthAssessment with detailed scoring
        """
        if not balance_sheets or not income_statements:
            raise ValueError("Balance sheets and income statements are required for health assessment")

        # Get the most recent year's data for primary calculation
        latest_balance = max(balance_sheets, key=lambda x: x.year or 0)
        latest_income = max(income_statements, key=lambda x: x.year or 0)
        
        # Calculate ratios for the latest year
        latest_ratios = self.calculate_financial_ratios(latest_balance, latest_income)
        
        # Calculate multi-year ratios for growth analysis
        ratios_by_year = self.calculate_multi_year_ratios(balance_sheets, income_statements, cash_flows)
        growth_rates = self.calculate_growth_rates(ratios_by_year)
        
        # Calculate component scores
        liquidity_score = self.calculate_liquidity_score(latest_ratios)
        profitability_score = self.calculate_profitability_score(latest_ratios)
        solvency_score = self.calculate_solvency_score(latest_ratios)
        efficiency_score = self.calculate_efficiency_score(latest_ratios)
        growth_score = self.calculate_growth_score(growth_rates)
        
        # Calculate weighted overall health score
        health_score = (
            liquidity_score * self.HEALTH_SCORE_WEIGHTS['liquidity'] +
            profitability_score * self.HEALTH_SCORE_WEIGHTS['profitability'] +
            solvency_score * self.HEALTH_SCORE_WEIGHTS['solvency'] +
            efficiency_score * self.HEALTH_SCORE_WEIGHTS['efficiency'] +
            growth_score * self.HEALTH_SCORE_WEIGHTS['growth']
        )
        
        # Determine risk level and grade
        risk_level = self._get_risk_level(health_score)
        health_grade = self._get_health_grade(health_score)
        
        # Determine trend direction
        trend_direction = self._determine_trend_direction(ratios_by_year)
        
        # Generate strengths, weaknesses, and recommendations
        strengths, weaknesses, recommendations = self._analyze_financial_position(
            latest_ratios, liquidity_score, profitability_score, 
            solvency_score, efficiency_score, growth_score
        )
        
        # Calculate Altman Z-Score if possible
        altman_z_score = self._calculate_altman_z_score(latest_balance, latest_income)
        
        return FinancialHealthAssessment(
            registration_number=latest_balance.statement_id or "",  # This should be reg number
            health_score=round(health_score, 1),
            health_grade=health_grade,
            liquidity_score=round(liquidity_score, 1),
            profitability_score=round(profitability_score, 1),
            solvency_score=round(solvency_score, 1),
            efficiency_score=round(efficiency_score, 1),
            growth_score=round(growth_score, 1),
            risk_level=risk_level,
            altman_z_score=altman_z_score,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations,
            trend_direction=trend_direction,
            years_analyzed=len(ratios_by_year)
        )

    def _get_risk_level(self, health_score: float) -> str:
        """Determine risk level based on health score."""
        for risk_level, (min_score, max_score) in self.RISK_THRESHOLDS.items():
            if min_score <= health_score < max_score:
                return risk_level
        return "LOW"  # Default for scores >= 75

    def _get_health_grade(self, health_score: float) -> str:
        """Determine health grade based on score."""
        for (min_score, max_score), grade in self.HEALTH_GRADES.items():
            if min_score <= health_score < max_score:
                return grade
        return "F"  # Default for very low scores

    def _determine_trend_direction(self, ratios_by_year: Dict[int, FinancialRatios]) -> str:
        """Determine overall trend direction from multi-year data."""
        if len(ratios_by_year) < 2:
            return "STABLE"
        
        # For now, return STABLE as placeholder
        # In real implementation, would analyze trends in key metrics
        return "STABLE"

    def _analyze_financial_position(
        self, 
        ratios: FinancialRatios,
        liquidity_score: float,
        profitability_score: float,
        solvency_score: float,
        efficiency_score: float,
        growth_score: float
    ) -> Tuple[List[str], List[str], List[str]]:
        """Analyze financial position and generate insights."""
        
        strengths = []
        weaknesses = []
        recommendations = []
        
        # Analyze each component
        if liquidity_score >= 70:
            strengths.append("Strong liquidity position")
        elif liquidity_score <= 40:
            weaknesses.append("Poor liquidity management")
            recommendations.append("Improve cash flow management and reduce current liabilities")
        
        if profitability_score >= 70:
            strengths.append("Excellent profitability")
        elif profitability_score <= 40:
            weaknesses.append("Low profitability margins")
            recommendations.append("Focus on cost reduction and revenue optimization")
        
        if solvency_score >= 70:
            strengths.append("Healthy debt levels")
        elif solvency_score <= 40:
            weaknesses.append("High financial leverage")
            recommendations.append("Consider debt reduction strategies")
        
        if efficiency_score >= 70:
            strengths.append("Efficient asset utilization")
        elif efficiency_score <= 40:
            weaknesses.append("Poor operational efficiency")
            recommendations.append("Optimize asset turnover and inventory management")
        
        if growth_score >= 70:
            strengths.append("Strong growth trajectory")
        elif growth_score <= 40:
            weaknesses.append("Limited growth performance")
            recommendations.append("Develop growth strategies and market expansion plans")
        
        return strengths, weaknesses, recommendations

    def _calculate_altman_z_score(
        self, 
        balance_sheet: BalanceSheet, 
        income_statement: IncomeStatement
    ) -> Optional[float]:
        """
        Calculate Altman Z-Score for bankruptcy prediction.
        
        Z = 1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E
        Where:
        A = Working Capital / Total Assets
        B = Retained Earnings / Total Assets  
        C = EBIT / Total Assets
        D = Market Value of Equity / Book Value of Total Debt
        E = Sales / Total Assets
        """
        try:
            total_assets = float(balance_sheet.total_assets or 0)
            if total_assets == 0:
                return None
            
            # A: Working Capital / Total Assets
            working_capital = (balance_sheet.total_current_assets or 0) - (balance_sheet.current_liabilities or 0)
            a_ratio = working_capital / total_assets
            
            # B: Retained Earnings / Total Assets (approximated as equity / total assets)
            equity = float(balance_sheet.equity or 0)
            b_ratio = equity / total_assets
            
            # C: EBIT / Total Assets (approximated as income before taxes)
            ebit = float(income_statement.income_before_income_taxes or 0)
            c_ratio = ebit / total_assets
            
            # D: Market Value of Equity / Book Value of Total Debt (simplified to book values)
            total_debt = (balance_sheet.current_liabilities or 0) + (balance_sheet.non_current_liabilities or 0)
            if total_debt > 0:
                d_ratio = equity / total_debt
            else:
                d_ratio = 1.0  # No debt scenario
            
            # E: Sales / Total Assets
            sales = float(income_statement.net_turnover or 0)
            e_ratio = sales / total_assets
            
            # Calculate Z-Score
            z_score = (1.2 * a_ratio + 1.4 * b_ratio + 3.3 * c_ratio + 
                      0.6 * d_ratio + 1.0 * e_ratio)
            
            return round(z_score, 2)
            
        except (TypeError, ValueError, ZeroDivisionError):
            return None


# Create singleton instance
financial_analysis_service = FinancialAnalysisService() 