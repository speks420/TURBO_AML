# TURBO_AML Backend - Financial Intelligence API

Advanced FastAPI backend providing comprehensive financial analysis and business intelligence for Latvian companies.

## 🚀 Overview

The TURBO_AML backend is a high-performance financial analysis engine that processes multiple government data sources to provide deep business insights, risk assessments, and predictive analytics.

### **Core Capabilities**
- **12+ Government Data Sources** - Complete company information integration
- **Advanced Financial Analysis** - Balance sheets, income statements, cash flow
- **Risk Assessment Engine** - Proprietary scoring algorithms
- **Real-time Data Processing** - Sub-second response times
- **Predictive Analytics** - ML-based business forecasting

## 🏗️ Architecture

### **Service Layer Architecture**
```
├── API Layer (FastAPI)
├── Business Logic Services
├── Financial Analysis Engine
├── Data Integration Layer (CKAN + Supabase)
├── Caching & Performance Layer
└── Security & Authentication
```

### **Financial Analysis Engine**
- **Health Score Calculator** - Proprietary 100-point algorithm
- **Ratio Analysis** - 20+ financial ratios and metrics
- **Trend Detection** - Multi-year pattern analysis
- **Risk Assessment** - Bankruptcy prediction models
- **Industry Benchmarking** - Comparative analysis tools

## 📊 Data Sources Integration

### **CKAN Government APIs**
1. **Company Registry** (`CKAN_COMPANY_RESOURCE_ID`)
2. **Financial Statements** (`CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID`)
3. **Balance Sheets** (`CKAN_BALANCE_SHEETS_RESOURCE_ID`)
4. **Income Statements** (`CKAN_INCOME_STATEMENTS_RESOURCE_ID`)
5. **Cash Flow Statements** (`CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID`)
6. **Capital Structure** (`CKAN_CAPITAL_RESOURCE_ID`)
7. **Beneficial Owners** (`CKAN_BENEFICIARY_RESOURCE_ID`)
8. **Company Members** (`CKAN_MEMBERS_RESOURCE_ID`)
9. **Business Activities** (`CKAN_BUSINESS_RESOURCE_ID`)
10. **Liquidation Processes** (`CKAN_LIQUIDATION_RESOURCE_ID`)
11. **Officers** (`CKAN_OFFICERS_RESOURCE_ID`)
12. **Stockholders** (`CKAN_STOCKHOLDERS_RESOURCE_ID`)

### **Supabase Analytics Database**
- **Company Profiles** - Enhanced company data
- **Financial Analysis Cache** - Pre-calculated metrics
- **User Preferences** - Search history, favorites
- **Industry Benchmarks** - Comparative data sets
- **Risk Alerts** - Automated monitoring system

## 🔧 Setup Instructions

### **Environment Configuration**

Create `backend/.env`:
```bash
# Supabase Configuration
SUPABASE_URL=https://padpihlwiriychsmsoyo.supabase.co
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# CKAN API Configuration
CKAN_BASE_URL=https://data.gov.lv/dati/lv/
CKAN_COMPANY_RESOURCE_ID=25e80bf3-f107-4ab4-89ef-251b5b9374e9
CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID=27fcc5ec-c63b-4bfd-bb08-01f073a52d04
CKAN_BALANCE_SHEETS_RESOURCE_ID=50ef4f26-f410-4007-b296-22043ca3dc43
CKAN_INCOME_STATEMENTS_RESOURCE_ID=d5fd17ef-d32e-40cb-8399-82b780095af0
CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID=1a11fc29-ba7c-4e5a-8edc-7a28cea24988
CKAN_CAPITAL_RESOURCE_ID=7910fef5-93eb-4d03-acf0-f45465d67414
CKAN_BENEFICIARY_RESOURCE_ID=20a9b26d-d056-4dbb-ae18-9ff23c87bdee
CKAN_MEMBERS_RESOURCE_ID=837b451a-4833-4fd1-bfdd-b45b35a994fd
CKAN_BUSINESS_RESOURCE_ID=49bbd751-3fa2-4d78-8c35-ae0e1c5250d6
CKAN_LIQUIDATION_RESOURCE_ID=59e7ec49-f1c6-4410-8ee6-e7737ac5eaee
CKAN_OFFICERS_RESOURCE_ID=e665114a-73c2-4375-9470-55874b4cfa6b
CKAN_STOCKHOLDERS_RESOURCE_ID=6adabd83-93f9-4d7f-bebd-fa109bbf794a

# Financial Analysis Configuration
FINANCIAL_HEALTH_ALGORITHM_VERSION=v2.1
RISK_ASSESSMENT_MODEL=enhanced_2024
ENABLE_PREDICTIVE_ANALYTICS=true
CACHE_FINANCIAL_DATA_TTL=3600
MIN_YEARS_FOR_TREND_ANALYSIS=3

# Performance Configuration
API_RATE_LIMIT_PER_MINUTE=100
MAX_CONCURRENT_REQUESTS=50
ENABLE_REQUEST_CACHING=true
```

### **Development Setup**

1. **Create virtual environment**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Unix/MacOS
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start development server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access API documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## 📡 API Endpoints

### **Company Search & Discovery**
```python
GET /api/search
    ?q=company_name
    &industry=technology
    &min_employees=10
    &max_employees=500
    &financial_health_min=70
    &status=active
    &limit=10
    &offset=0
```

### **Company Information**
```python
GET /api/company/{reg_number}                    # Complete company profile
GET /api/company/{reg_number}/basic              # Basic company info
GET /api/company/{reg_number}/officers           # Management team
GET /api/company/{reg_number}/shareholders       # Ownership structure
GET /api/company/{reg_number}/activities         # Business activities
```

### **Financial Analysis**
```python
GET /api/financial/{reg_number}/health-score     # Overall financial health (0-100)
GET /api/financial/{reg_number}/statements       # Annual financial statements
GET /api/financial/{reg_number}/balance-sheet    # Balance sheet data
GET /api/financial/{reg_number}/income-statement # Profit & loss statements
GET /api/financial/{reg_number}/cash-flow        # Cash flow analysis
GET /api/financial/{reg_number}/ratios           # Financial ratios
GET /api/financial/{reg_number}/trends           # Multi-year trends
GET /api/financial/{reg_number}/risk-assessment  # Risk evaluation
GET /api/financial/{reg_number}/predictions      # Future performance forecast
```

### **Advanced Analytics**
```python
GET /api/analytics/industry/{sector}/overview    # Industry analysis
GET /api/analytics/market-opportunities          # Investment opportunities
GET /api/analytics/risk-alerts                   # Portfolio monitoring
POST /api/analytics/bulk-analysis                # Batch company analysis
GET /api/analytics/benchmarks/{reg_number}       # Peer comparison
```

### **Monitoring & Alerts**
```python
POST /api/alerts/create                          # Setup monitoring alerts
GET /api/alerts/user/{user_id}                   # User's active alerts
GET /api/monitoring/portfolio                    # Portfolio health monitoring
```

## 🧮 Financial Calculation Engine

### **Health Score Algorithm (v2.1)**
```python
def calculate_health_score(company_data):
    """
    Proprietary algorithm combining multiple financial indicators
    Returns: 0-100 score (100 = excellent financial health)
    """
    factors = {
        'liquidity_ratio': 0.25,          # Current assets / Current liabilities
        'profitability': 0.30,            # ROA, ROE, profit margins
        'solvency': 0.20,                  # Debt-to-equity ratios
        'efficiency': 0.15,                # Asset turnover ratios
        'growth_trends': 0.10              # Revenue/profit growth patterns
    }
    # Implementation details in /app/services/financial_analysis.py
```

### **Risk Assessment Framework**
- **Altman Z-Score** - Bankruptcy prediction
- **Piotroski F-Score** - Financial strength
- **Custom Risk Indicators** - Industry-specific factors
- **Trend Analysis** - Early warning signals

### **Financial Ratios Calculated**
- **Liquidity**: Current, Quick, Cash ratios
- **Profitability**: ROA, ROE, Gross/Net margins, EBITDA
- **Solvency**: Debt-to-equity, Interest coverage, Debt service
- **Efficiency**: Asset turnover, Inventory turnover, Receivables
- **Growth**: Revenue CAGR, Profit growth, Asset expansion

## 🗄️ Database Schema

### **Supabase Tables**

#### **companies** (Enhanced company profiles)
```sql
CREATE TABLE companies (
    registration_number VARCHAR PRIMARY KEY,
    name VARCHAR,
    status VARCHAR,
    address VARCHAR,
    founded_date DATE,
    industry_sector VARCHAR,
    employee_count INTEGER,
    last_financial_update TIMESTAMP,
    health_score INTEGER,
    risk_level VARCHAR,
    additional_data JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### **financial_statements** (Processed financial data)
```sql
CREATE TABLE financial_statements (
    id SERIAL PRIMARY KEY,
    registration_number VARCHAR REFERENCES companies(registration_number),
    statement_year INTEGER,
    statement_type VARCHAR, -- 'balance_sheet', 'income_statement', 'cash_flow'
    data JSONB,
    calculated_ratios JSONB,
    health_indicators JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### **financial_analysis** (Pre-calculated analysis)
```sql
CREATE TABLE financial_analysis (
    id SERIAL PRIMARY KEY,
    registration_number VARCHAR REFERENCES companies(registration_number),
    analysis_date DATE,
    health_score INTEGER,
    risk_assessment JSONB,
    trend_analysis JSONB,
    industry_benchmarks JSONB,
    predictions JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🚀 Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                          # FastAPI application
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── search.py               # Company search
│   │   │   ├── company.py              # Company details
│   │   │   ├── financial.py            # Financial analysis endpoints
│   │   │   ├── analytics.py            # Advanced analytics
│   │   │   └── monitoring.py           # Alerts & monitoring
│   │   └── dependencies.py             # API dependencies
│   ├── core/
│   │   ├── config.py                   # Configuration management
│   │   ├── security.py                 # Security utilities
│   │   └── constants.py                # Business constants
│   ├── db/
│   │   ├── supabase.py                 # Supabase client
│   │   └── migrations/                 # Database migrations
│   ├── models/
│   │   ├── company.py                  # Company data models
│   │   ├── financial.py                # Financial data models
│   │   └── analytics.py                # Analytics models
│   ├── services/
│   │   ├── ckan_service.py             # CKAN API integration
│   │   ├── financial_analysis.py       # Financial calculations
│   │   ├── risk_assessment.py          # Risk evaluation
│   │   ├── trend_analysis.py           # Trend detection
│   │   ├── industry_benchmarks.py      # Comparative analysis
│   │   └── predictive_analytics.py     # ML forecasting
│   └── utils/
│       ├── helpers.py                  # Helper utilities
│       ├── validators.py               # Data validation
│       └── formatters.py               # Data formatting
├── tests/                              # Comprehensive test suite
├── docker/                             # Docker configuration
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Container definition
└── README.md                           # This file
```

## 🧪 Testing

### **Run test suite**
```bash
pytest tests/ -v --cov=app --cov-report=html
```

### **Test categories**
- **Unit tests** - Individual function testing
- **Integration tests** - API endpoint testing
- **Financial calculation tests** - Algorithm accuracy
- **Performance tests** - Load and stress testing

## 🔒 Security

### **API Security**
- **Rate limiting** - Prevent abuse
- **Input validation** - Sanitize all inputs
- **CORS configuration** - Controlled cross-origin access
- **Error handling** - Secure error responses

### **Data Security**
- **Environment variables** - Secure credential storage
- **Database encryption** - Data at rest protection
- **API key management** - Secure external service access

## 📈 Performance Optimization

### **Caching Strategy**
- **Financial data cache** - 1-hour TTL for calculated metrics
- **Company profile cache** - 6-hour TTL for basic data
- **Industry benchmarks** - Daily refresh cycle

### **Database Optimization**
- **Indexed queries** - Fast lookup performance
- **Connection pooling** - Efficient database connections
- **Query optimization** - Minimize database load

## 🐳 Docker Support

### **Development container**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### **Production container**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

## 🔧 Dependencies

### **Core Dependencies**
```
fastapi==0.110.0                # Web framework
uvicorn==0.29.0                 # ASGI server
pydantic==2.7.1                 # Data validation
supabase==2.5.2                 # Database client
ckanapi==4.7.0                  # Government API client
httpx>=0.27.0,<0.29.0          # Async HTTP client
```

### **Financial Analysis**
```
numpy>=1.24.0                   # Numerical computing
pandas>=2.0.0                   # Data analysis
scikit-learn>=1.3.0             # Machine learning
scipy>=1.10.0                   # Scientific computing
```

### **Performance & Monitoring**
```
redis>=4.5.0                    # Caching
prometheus-client>=0.16.0       # Metrics
structlog>=23.1.0               # Logging
```

## 🚀 Deployment

### **Local Development**
```bash
uvicorn app.main:app --reload
```

### **Production Deployment**
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### **Docker Deployment**
```bash
docker build -t turbo-aml-backend .
docker run -p 8000:8000 --env-file .env turbo-aml-backend
```

## 📊 Monitoring & Analytics

### **Application Metrics**
- Request/response times
- Error rates and types
- Financial calculation performance
- Database query performance

### **Business Metrics**
- API usage patterns
- Popular company searches
- Financial analysis request volume
- User engagement metrics

---

**TURBO_AML Backend** - *Powering Advanced Business Intelligence* 