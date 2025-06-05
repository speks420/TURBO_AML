# TURBO_AML - Advanced Latvian Business Intelligence Platform

A comprehensive business intelligence application that provides deep financial analysis and insights for Latvian companies using data.gov.lv CKAN API and Supabase for enhanced data storage and analytics.

## 🚀 Project Vision

**TURBO_AML** is not just a company lookup tool - it's a **professional-grade business intelligence platform** that empowers users to make informed business decisions through:

- **Deep Financial Analysis** with multi-year trend tracking
- **Business Health Scoring** using proprietary algorithms  
- **Investment Risk Assessment** based on comprehensive financial metrics
- **Competitive Intelligence** with industry benchmarking
- **Predictive Analytics** for business performance forecasting

## ✨ Key Features

### 🔍 **Company Discovery & Research**
- Advanced search with intelligent filters (industry, size, location, financial health)
- Comprehensive company profiles with 8+ data sources
- Real-time company status monitoring
- Search history and favorites management

### 📊 **Financial Intelligence Dashboard**
- **Balance Sheet Analysis** - Assets, liabilities, equity trends
- **Income Statement Insights** - Revenue, profitability, expense analysis  
- **Cash Flow Monitoring** - Operating, investing, financing activities
- **Financial Health Score** (0-100) with risk indicators
- **Multi-Year Trends** with visual analytics
- **Industry Benchmarking** and comparative analysis

### ⚡ **Smart Business Insights**
- **Investment Risk Rating** (LOW/MEDIUM/HIGH) 
- **Growth Potential Scoring** based on financial trends
- **Bankruptcy Risk Assessment** using multiple indicators
- **Liquidity Analysis** and solvency ratios
- **Profitability Metrics** with industry comparisons
- **Employee Growth Tracking** and productivity insights

### 🛡️ **Risk Management Tools**
- **Liquidation Process Alerts** with detailed tracking
- **Financial Distress Indicators** early warning system
- **Credit Risk Assessment** based on financial stability
- **Beneficial Ownership Analysis** for transparency
- **Related Companies Network** mapping

## 🏗️ Tech Stack

### **Backend**
- **FastAPI 0.110.0** - High-performance async API
- **Python 3.10+** with comprehensive financial calculation libraries
- **CKAN API Integration** - 12+ government data sources
- **Supabase** - Real-time database with advanced analytics
- **Advanced Financial Algorithms** - Custom scoring and analysis engines

### **Frontend** 
- **React 18** with modern hooks and context
- **Vite 5** - Lightning-fast development and builds
- **Chakra UI** - Professional, accessible component library
- **Recharts/Chart.js** - Advanced financial data visualization
- **Responsive Design** - Mobile-first approach

### **Data Sources Integration**
- **Company Registry** - Basic company information
- **Financial Statements** - Annual reports (2014-present)
- **Balance Sheets** - Assets, liabilities, equity data
- **Income Statements** - Revenue and expense analysis
- **Cash Flow Statements** - Liquidity and cash management
- **Capital Structure** - Investment and ownership data
- **Beneficial Owners** - Transparency and compliance
- **Officers & Members** - Leadership and governance
- **Business Activities** - Industry and operational scope
- **Liquidation Processes** - Distress and closure tracking

## 🎯 Unique Value Propositions

### **For Investors & Lenders**
- Comprehensive due diligence automation
- Risk assessment with quantified metrics
- Portfolio monitoring and alerts
- Competitive landscape analysis

### **For Business Professionals**
- Supplier/partner financial health verification
- Market opportunity identification
- Competitive intelligence gathering
- M&A target screening

### **For Financial Analysts**
- Automated financial ratio calculations
- Industry trend analysis
- Peer group comparisons
- Financial modeling data exports

## 📈 Financial Intelligence Capabilities

### **Core Financial Metrics**
- **Liquidity Ratios**: Current ratio, quick ratio, cash ratio
- **Solvency Ratios**: Debt-to-equity, interest coverage, debt service coverage
- **Profitability Ratios**: ROA, ROE, gross/net profit margins
- **Efficiency Ratios**: Asset turnover, inventory turnover, receivables turnover
- **Growth Metrics**: Revenue CAGR, profit growth, asset growth

### **Advanced Analytics**
- **Altman Z-Score** - Bankruptcy prediction model
- **Piotroski F-Score** - Financial strength assessment
- **Custom Health Score** - Proprietary algorithm combining multiple factors
- **Trend Analysis** - 5-year historical performance tracking
- **Seasonal Patterns** - Business cycle identification

### **Risk Assessment Framework**
- **Financial Distress Indicators** - Early warning signals
- **Industry Risk Factors** - Sector-specific considerations
- **Economic Sensitivity** - Macro-economic impact analysis
- **Operational Risk Metrics** - Business model sustainability

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.10+)
- Git
- Docker (for containerized deployment)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd TURBO_AML
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Access the Application**
   - Frontend: `http://localhost:5173`
   - Backend API: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

## 🐳 Docker Deployment

### **Development Environment**
```bash
docker-compose -f docker-compose.dev.yml up
```

### **Production Environment**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### **Multi-Container Setup for Standalone PC**
- **Database Container**: Supabase local instance
- **Backend Container**: FastAPI with financial calculation engines
- **Frontend Container**: React app with Nginx
- **Analytics Container**: Data processing and ML models
- **Monitoring Container**: Logging and performance metrics

## 🔧 Configuration

### **Environment Variables**

#### Backend (.env)
```bash
# Supabase Configuration
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# CKAN API Configuration
CKAN_BASE_URL=https://data.gov.lv/dati/lv/
CKAN_COMPANY_RESOURCE_ID=25e80bf3-f107-4ab4-89ef-251b5b9374e9
CKAN_FINANCIAL_STATEMENTS_RESOURCE_ID=financial_statements_id
CKAN_BALANCE_SHEETS_RESOURCE_ID=balance_sheets_id
CKAN_INCOME_STATEMENTS_RESOURCE_ID=income_statements_id
CKAN_CASH_FLOW_STATEMENTS_RESOURCE_ID=cash_flow_id

# Financial Analysis Configuration
FINANCIAL_HEALTH_ALGORITHM_VERSION=v2.1
RISK_ASSESSMENT_MODEL=enhanced_2024
ENABLE_PREDICTIVE_ANALYTICS=true
```

#### Frontend (.env)
```bash
VITE_API_URL=http://localhost:8000
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_anon_key
VITE_ENABLE_ADVANCED_CHARTS=true
VITE_FINANCIAL_DATA_CACHE_TTL=3600
```

## 📊 API Endpoints

### **Company Information**
- `GET /api/search` - Advanced company search with filters
- `GET /api/company/{reg_number}` - Comprehensive company profile
- `GET /api/company/{reg_number}/officers` - Leadership information
- `GET /api/company/{reg_number}/shareholders` - Ownership structure

### **Financial Analysis**
- `GET /api/financial/{reg_number}/health-score` - Financial health assessment
- `GET /api/financial/{reg_number}/trends` - Multi-year financial trends
- `GET /api/financial/{reg_number}/ratios` - Financial ratio analysis
- `GET /api/financial/{reg_number}/risk-assessment` - Investment risk evaluation
- `GET /api/financial/{reg_number}/statements` - Annual financial statements
- `GET /api/financial/{reg_number}/cash-flow` - Cash flow analysis
- `GET /api/financial/{reg_number}/comparative` - Industry benchmarking

### **Advanced Analytics**
- `GET /api/analytics/industry/{sector}` - Industry trend analysis
- `GET /api/analytics/market-opportunities` - Investment opportunities
- `GET /api/analytics/risk-alerts` - Portfolio risk monitoring
- `POST /api/analytics/bulk-analysis` - Batch company analysis

## 🚢 Deployment Strategy

### **Standalone PC Deployment**
1. **GitHub Repository** - Source code management
2. **Docker Compose** - Multi-container orchestration
3. **Local Database** - Supabase local instance or PostgreSQL
4. **Nginx Reverse Proxy** - Load balancing and SSL
5. **Automated Backups** - Data persistence and recovery

### **Cloud Deployment Options**
- **Supabase Cloud** - Managed database and authentication
- **Vercel/Netlify** - Frontend hosting with CDN
- **Railway/Render** - Backend API hosting
- **Docker Swarm** - Container orchestration

## 🔮 Roadmap

### **Phase 1: Financial Intelligence Core** (Current)
- [x] Company data integration
- [x] Basic financial statement parsing
- [ ] Financial health scoring algorithm
- [ ] Risk assessment framework
- [ ] Multi-year trend analysis

### **Phase 2: Advanced Analytics** (Q2 2024)
- [ ] Machine learning models for prediction
- [ ] Industry benchmarking system
- [ ] Competitive analysis tools
- [ ] Investment opportunity scoring

### **Phase 3: Professional Features** (Q3 2024)
- [ ] Portfolio management tools
- [ ] Custom alerting system
- [ ] API rate limiting and authentication
- [ ] White-label solutions

### **Phase 4: Enterprise Scale** (Q4 2024)
- [ ] Multi-tenant architecture
- [ ] Advanced reporting and exports
- [ ] Third-party integrations
- [ ] Mobile applications

## 🤝 Contributing

We welcome contributions to make TURBO_AML the best business intelligence platform for Latvian companies!

### **Development Guidelines**
- Follow conventional commit messages
- Maintain 90%+ test coverage
- Document all financial algorithms
- Ensure mobile responsiveness

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Success Metrics

- **Data Coverage**: 95%+ of active Latvian companies
- **Analysis Speed**: <2s for comprehensive company analysis
- **Accuracy**: 98%+ financial calculation accuracy
- **User Adoption**: Target 1000+ active users in first year
- **API Performance**: 99.9% uptime, <500ms response times

---

**TURBO_AML** - *Empowering Business Intelligence Through Advanced Financial Analysis*

For questions, feature requests, or support, please open an issue or contact the development team.