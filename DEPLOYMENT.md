# 🚀 TURBO_AML Deployment Guide

Complete deployment instructions for the **Advanced Latvian Business Intelligence Platform** with financial analysis capabilities.

## 📋 Prerequisites

### **System Requirements**
- **OS**: Windows 10/11, Ubuntu 20.04+, or macOS 12+
- **RAM**: Minimum 8GB (16GB recommended for full stack)
- **Storage**: 50GB free space (100GB recommended)
- **CPU**: 4 cores minimum (8 cores recommended)
- **Network**: Stable internet connection for API access

### **Software Requirements**
- **Docker**: Version 20.10+
- **Docker Compose**: Version 2.0+
- **Git**: Latest version
- **Node.js**: Version 18+ (for local development)
- **Python**: Version 3.10+ (for local development)

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    TURBO_AML Architecture                   │
├─────────────────────────────────────────────────────────────┤
│  Load Balancer (Nginx)                                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Frontend      │    Backend      │    Analytics            │
│   (React+Nginx) │    (FastAPI)    │    (Prometheus+Grafana) │
├─────────────────┼─────────────────┼─────────────────────────┤
│        Cache Layer (Redis)        │    Database             │
│                                   │    (Supabase/PostgreSQL)│
├─────────────────────────────────────────────────────────────┤
│            External APIs (data.gov.lv CKAN)                │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Configuration Setup

### **Step 1: Clone Repository**
```bash
git clone https://github.com/your-username/TURBO_AML.git
cd TURBO_AML
```

### **Step 2: Environment Configuration**

#### **Backend Environment** (`backend/.env`)
```bash
# Copy your existing configuration
cp backend/.env.example backend/.env

# Your current configuration:
SUPABASE_URL=https://padpihlwiriychsmsoyo.supabase.co
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# CKAN API Configuration
CKAN_BASE_URL=https://data.gov.lv/dati/lv/
CKAN_COMPANY_RESOURCE_ID=25e80bf3-f107-4ab4-89ef-251b5b9374e9
# Financial data resource IDs (CONFIRMED)
CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID=27fcc5ec-c63b-4bfd-bb08-01f073a52d04
CKAN_BALANCE_SHEETS_RESOURCE_ID=50ef4f26-f410-4007-b296-22043ca3dc43
CKAN_INCOME_STATEMENTS_RESOURCE_ID=d5fd17ef-d32e-40cb-8399-82b780095af0
CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID=1a11fc29-ba7c-4e5a-8edc-7a28cea24988

# Existing resource IDs
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
```

#### **Frontend Environment** (`frontend/.env`)
```bash
# Your current configuration:
VITE_API_URL=http://localhost:8000
VITE_SUPABASE_URL=https://padpihlwiriychsmsoyo.supabase.co
VITE_SUPABASE_ANON_KEY=your_anon_key

# New financial dashboard features
VITE_ENABLE_ADVANCED_CHARTS=true
VITE_ENABLE_EXPORT_FEATURES=true
VITE_ENABLE_REAL_TIME_UPDATES=true
VITE_FINANCIAL_DATA_CACHE_TTL=3600
```

#### **Production Environment** (`.env.prod`)
```bash
# Production-specific settings
POSTGRES_USER=turbo_aml
POSTGRES_PASSWORD=your_secure_password
GRAFANA_PASSWORD=your_grafana_password
FRONTEND_API_URL=http://localhost/api
```

## 🚢 Deployment Options

### **Option 1: Development Environment**
Perfect for testing and development with hot reloading:

```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up -d

# Access services:
# Frontend: http://localhost:5173
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### **Option 2: Production Environment**
Optimized for standalone PC deployment with monitoring:

```bash
# Build and start production environment
docker-compose -f docker-compose.prod.yml up -d

# Access services:
# Application: http://localhost
# Monitoring: http://localhost:3000 (Grafana)
# Metrics: http://localhost:9090 (Prometheus)
```

## 📊 Financial Intelligence Implementation Plan

### **Phase 1: Core Financial Data Integration**

#### **Week 1: Backend Financial Integration** ✅
1. **Financial Data Integration Complete**
   ```bash
   ✅ Resource IDs identified and configured:
   # Annual Report Basic Info: 27fcc5ec-c63b-4bfd-bb08-01f073a52d04
   # Balance Sheets: 50ef4f26-f410-4007-b296-22043ca3dc43
   # Income Statements: d5fd17ef-d32e-40cb-8399-82b780095af0
   # Cash Flow Statements: 1a11fc29-ba7c-4e5a-8edc-7a28cea24988
   ```

2. **Backend Models Complete** ✅
   ```python
   ✅ Financial models created with full data structure:
   - FinancialStatementInfo (Annual report metadata)
   - BalanceSheet (Assets, liabilities, equity)
   - IncomeStatement (Revenue, expenses, profit/loss)
   - CashFlowStatement (Operating, investing, financing flows)
   - FinancialRatios (20+ calculated ratios)
   - FinancialHealthAssessment (Health scoring)
   ```

3. **CKAN Service Extended** ✅
   ```python
   ✅ New methods added to CKANService:
   - get_financial_statements() 
   - get_balance_sheets()
   - get_income_statements()
   - get_cash_flow_statements()
   - get_multi_year_financial_data()
   ```

4. **Financial Analysis Service Created** ✅
   ```python
   ✅ Financial analysis service implemented:
   # backend/app/services/financial_analysis.py
   class FinancialAnalysisService:
       def calculate_health_score()           # 100-point algorithm ✅
       def calculate_financial_ratios()       # 20+ ratios ✅
       def calculate_liquidity_score()        # Liquidity analysis ✅
       def calculate_profitability_score()    # Profitability metrics ✅
       def calculate_solvency_score()         # Debt analysis ✅
       def calculate_efficiency_score()       # Asset utilization ✅
       def calculate_growth_score()           # Growth trends ✅
       def _calculate_altman_z_score()        # Bankruptcy prediction ✅
   ```

5. **API Endpoints Ready** ✅
   ```python
   ✅ Financial API endpoints created:
   # backend/app/api/endpoints/financial.py
   GET /financial/{reg_number}/statements      # Complete financial data
   GET /financial/{reg_number}/balance-sheet   # Balance sheet analysis
   GET /financial/{reg_number}/income-statement # Income statement data
   GET /financial/{reg_number}/cash-flow       # Cash flow analysis
   GET /financial/{reg_number}/ratios          # Financial ratios
   GET /financial/{reg_number}/health-score    # Health assessment
   GET /financial/{reg_number}/trends          # Multi-year trends
   ```

#### **Week 2: Advanced Analytics Engine**
1. **Health Score Algorithm**
   - Liquidity ratios (25% weight)
   - Profitability metrics (30% weight)
   - Solvency indicators (20% weight)
   - Efficiency ratios (15% weight)
   - Growth trends (10% weight)

2. **Risk Assessment Framework**
   - Altman Z-Score implementation
   - Piotroski F-Score calculation
   - Custom risk indicators
   - Industry-specific factors

### **Phase 2: Frontend Financial Dashboard**

#### **Week 3: Dashboard Components**
1. **Create Financial Components**
   ```jsx
   // frontend/src/components/financial/
   - HealthScoreCard.jsx      // Visual health score
   - FinancialCharts.jsx      // Trend analysis
   - RiskAssessment.jsx       // Risk indicators  
   - RatiosTable.jsx          // Financial ratios
   - BenchmarkChart.jsx       // Industry comparison
   ```

2. **Chart Library Integration**
   ```bash
   # Add advanced charting
   npm install recharts
   npm install react-chartjs-2 chart.js
   ```

#### **Week 4: User Experience Enhancement**
1. **Advanced Search Filters**
2. **Export Functionality**
3. **Real-time Updates**
4. **Mobile Optimization**

### **Phase 3: Production Deployment**

#### **Week 5: Docker & Infrastructure**
1. **Container Optimization**
2. **Monitoring Setup**
3. **Backup Systems**
4. **Performance Tuning**

## 🛠️ Development Workflow

### **Local Development Setup**
```bash
# Backend development
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend development
cd frontend
npm install
npm run dev
```

### **Adding Financial Features**
1. **Backend**: Add new endpoints in `app/api/endpoints/financial.py`
2. **Frontend**: Create components in `src/components/financial/`
3. **Models**: Define data structures in `app/models/financial.py`
4. **Services**: Implement business logic in `app/services/`

## 📈 Monitoring & Analytics

### **System Monitoring**
- **Prometheus**: Metrics collection (`http://localhost:9090`)
- **Grafana**: Dashboard visualization (`http://localhost:3000`)
- **Log Aggregation**: Loki + Promtail
- **Health Checks**: Automated service monitoring

### **Application Metrics**
- API response times
- Financial calculation performance
- Database query optimization
- User engagement analytics

## 🔒 Security Configuration

### **Production Security**
```bash
# SSL/TLS Setup
mkdir -p nginx/ssl
# Add your SSL certificates

# Database Security
# Use strong passwords in .env.prod
# Enable connection encryption

# API Security
# Rate limiting configured in Nginx
# Input validation in FastAPI
```

### **Backup Strategy**
```bash
# Automated daily backups
./scripts/backup.sh

# Manual backup
docker exec turbo_aml_postgres_prod pg_dump -U turbo_aml turbo_aml > backup.sql
```

## 🧪 Testing Strategy

### **Backend Testing**
```bash
cd backend
pytest tests/ -v --cov=app --cov-report=html
```

### **Frontend Testing**
```bash
cd frontend
npm run test              # Unit tests
npm run test:e2e          # End-to-end tests
npm run test:coverage     # Coverage report
```

### **Financial Algorithm Testing**
- Validate health score calculations
- Test risk assessment accuracy
- Benchmark performance metrics
- Verify data integrity

## 🚀 Deployment Timeline

### **Immediate (Week 1)**
- [x] Documentation updated
- [x] Docker configuration created  
- [x] Financial data source research (COMPLETE)
- [x] Backend models extended (COMPLETE)
- [x] CKAN service financial integration (COMPLETE)
- [x] Financial analysis service (COMPLETE)
- [x] API endpoints created (COMPLETE)

### **Short Term (Weeks 2-4)**
- [ ] Financial analysis engine
- [ ] Dashboard components
- [ ] Chart integration
- [ ] Export functionality

### **Medium Term (Weeks 5-8)**
- [ ] Production deployment
- [ ] Monitoring setup
- [ ] Performance optimization
- [ ] User testing

### **Long Term (Months 2-3)**
- [ ] Machine learning integration
- [ ] Advanced analytics
- [ ] Mobile application
- [ ] API marketplace

## 📋 Troubleshooting

### **Common Issues**
1. **Port Conflicts**: Ensure ports 80, 8000, 5173 are available
2. **Memory Issues**: Increase Docker memory allocation
3. **API Rate Limits**: Implement caching and request throttling
4. **Database Connections**: Check Supabase connection limits

### **Performance Optimization**
1. **Enable Redis Caching**: Financial data caching
2. **Database Indexing**: Optimize query performance
3. **CDN Integration**: Static asset delivery
4. **Load Balancing**: Scale horizontally

## 🎯 Success Metrics

### **Technical KPIs**
- **API Response Time**: <500ms average
- **Page Load Speed**: <2s first contentful paint
- **Uptime**: 99.9% availability
- **Data Accuracy**: 98%+ financial calculations

### **Business KPIs**
- **User Adoption**: 1000+ active users (Year 1)
- **Company Coverage**: 95%+ of active Latvian companies
- **Analysis Speed**: <2s for comprehensive reports
- **User Satisfaction**: 4.5+ rating

---

## 🎉 Ready to Launch!

Your **TURBO_AML** platform is now ready for implementation! With this comprehensive setup, you'll have:

✅ **Complete Docker Environment** - Development and production ready  
✅ **Financial Intelligence Engine** - Advanced analytics and scoring  
✅ **Professional Dashboard** - Intuitive business intelligence interface  
✅ **Monitoring & Backup** - Production-grade reliability  
✅ **Scalable Architecture** - Ready for growth and expansion  

**Next Step**: Start with financial data source research and begin implementing the health score algorithm!

---

*TURBO_AML - Empowering Business Intelligence Through Advanced Financial Analysis* 