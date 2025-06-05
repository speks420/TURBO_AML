# TURBO_AML Frontend - Financial Intelligence Dashboard

Advanced React frontend providing comprehensive financial analysis and business intelligence visualization for Latvian companies.

## 🚀 Overview

The TURBO_AML frontend is a modern, responsive business intelligence dashboard that transforms complex financial data into actionable insights through intuitive visualizations and smart analytics.

## Setup Instructions

1. Install dependencies:
   ```
   npm install
   ```

2. Copy the environment variables:
   ```
   cp .env.example .env
   ```

3. Start the development server:
   ```
   npm run dev
   ```
   The application will be available at `http://localhost:5173`

## 🎯 Key Features

### 📊 **Financial Intelligence Dashboard**
- **Interactive Charts** - Multi-year financial trends and performance
- **Health Score Visualization** - Real-time business health indicators
- **Risk Assessment Display** - Color-coded risk levels and alerts
- **Industry Benchmarking** - Comparative analysis with peer companies

### 🔍 **Advanced Company Analysis**
- **Comprehensive Search** - Smart filters and advanced search options
- **Detailed Company Profiles** - 360° view with all data sources
- **Financial Statement Analysis** - Balance sheets, income statements, cash flow
- **Ownership & Governance** - Beneficial owners, officers, shareholding structure

### ⚡ **User Experience**
- **Real-time Updates** - Live data synchronization
- **Responsive Design** - Optimized for desktop, tablet, and mobile
- **Search History** - Quick access to recent searches
- **Export Capabilities** - PDF reports and data export

## 🛠️ Tech Stack

### **Core Framework**
- **React 18.2.0** - Modern hooks and concurrent features
- **Vite 5.1.4** - Lightning-fast development and builds
- **React Router 6.22.2** - Advanced routing and navigation

### **UI & Visualization**
- **Chakra UI 2.8.2** - Professional component library
- **Recharts** - Advanced financial charts and graphs *(planned)*
- **Framer Motion 11.0.8** - Smooth animations and transitions
- **React Icons 5.0.1** - Comprehensive icon library

### **Data & API**
- **Axios 1.6.7** - HTTP client with interceptors
- **Supabase JS 2.39.7** - Real-time database integration
- **React Query** - Advanced data fetching and caching *(planned)*

### **Development Tools**
- **ESLint 8.57.0** - Code quality and consistency
- **Prettier** - Code formatting *(planned)*
- **TypeScript** - Type safety *(planned migration)*

## 🏗️ Project Structure

```
frontend/
├── public/
│   ├── favicon.ico
│   └── assets/
├── src/
│   ├── components/
│   │   ├── layout/                    # Layout components
│   │   │   ├── Header.jsx            # Main navigation header
│   │   │   ├── Footer.jsx            # Site footer
│   │   │   └── Layout.jsx            # Common page layout
│   │   ├── ui/                       # Reusable UI components
│   │   │   ├── SearchBar.jsx         # Company search component
│   │   │   ├── CompanyCard.jsx       # Company info cards
│   │   │   ├── LoadingSpinner.jsx    # Loading indicators
│   │   │   └── SearchHistoryDrawer.jsx # Search history UI
│   │   ├── financial/                # Financial analysis components (NEW)
│   │   │   ├── HealthScoreCard.jsx   # Health score visualization
│   │   │   ├── FinancialCharts.jsx   # Interactive charts
│   │   │   ├── RiskAssessment.jsx    # Risk level indicators
│   │   │   ├── TrendAnalysis.jsx     # Multi-year trends
│   │   │   ├── RatiosTable.jsx       # Financial ratios display
│   │   │   └── BenchmarkChart.jsx    # Industry comparison
│   │   ├── company/                  # Company-specific components
│   │   │   ├── CompanyProfile.jsx    # Company overview
│   │   │   ├── OwnershipStructure.jsx # Shareholders & ownership
│   │   │   ├── OfficersTable.jsx     # Management team
│   │   │   └── BusinessActivities.jsx # Company activities
│   │   └── common/                   # Common utility components
│   │       ├── DataTable.jsx         # Reusable data tables
│   │       ├── ExportButton.jsx      # Export functionality
│   │       └── FilterPanel.jsx       # Advanced search filters
│   ├── hooks/                        # Custom React hooks
│   │   ├── useSearch.js              # Company search logic
│   │   ├── useCompanyDetails.js      # Company data fetching
│   │   ├── useFinancialAnalysis.js   # Financial data hooks (NEW)
│   │   ├── useHealthScore.js         # Health score calculation (NEW)
│   │   └── useIndustryBenchmarks.js  # Benchmarking data (NEW)
│   ├── pages/                        # Page components
│   │   ├── HomePage.jsx              # Search and discovery page
│   │   ├── CompanyDetailsPage.jsx    # Comprehensive company profile
│   │   ├── FinancialDashboard.jsx    # Financial analysis page (NEW)
│   │   ├── IndustryAnalysisPage.jsx  # Industry insights (NEW)
│   │   └── NotFoundPage.jsx          # 404 error page
│   ├── services/                     # API services
│   │   ├── api.js                    # Base API configuration
│   │   ├── companyService.js         # Company-related API calls
│   │   ├── financialService.js       # Financial analysis APIs (NEW)
│   │   └── analyticsService.js       # Advanced analytics APIs (NEW)
│   ├── utils/                        # Utility functions
│   │   ├── formatters.js             # Data formatting utilities
│   │   ├── calculations.js           # Financial calculations (NEW)
│   │   ├── chartHelpers.js           # Chart configuration helpers (NEW)
│   │   └── exportUtils.js            # Data export utilities (NEW)
│   ├── theme/                        # Chakra UI theme
│   │   └── index.js                  # Custom theme configuration
│   ├── contexts/                     # React contexts (NEW)
│   │   ├── CompanyContext.jsx        # Global company state
│   │   └── AnalyticsContext.jsx      # Analytics state management
│   ├── App.jsx                       # Main application component
│   ├── main.jsx                      # Application entry point
│   └── routes.jsx                    # Route definitions
├── .env.example                      # Example environment variables
├── .env                              # Environment variables (gitignored)
├── index.html                        # HTML entry point
├── vite.config.js                    # Vite configuration
├── package.json                      # Dependencies and scripts
├── Dockerfile                        # Container definition (NEW)
└── README.md                         # This file
```

## 📊 Component Library

### **Financial Analysis Components**
- **`HealthScoreCard`** - Visual health score with color-coded indicators
- **`FinancialCharts`** - Interactive line/bar charts for trends
- **`RiskAssessment`** - Risk level visualization with explanations
- **`TrendAnalysis`** - Multi-year performance comparison
- **`RatiosTable`** - Comprehensive financial ratios display
- **`BenchmarkChart`** - Industry comparison visualizations

### **Company Information Components**
- **`CompanyProfile`** - Comprehensive company overview
- **`OwnershipStructure`** - Shareholder and beneficial owner display
- **`OfficersTable`** - Management team and governance
- **`BusinessActivities`** - Industry sectors and activities

### **UI/UX Components**
- **`SearchBar`** - Advanced search with filters
- **`CompanyCard`** - Company information cards
- **`DataTable`** - Sortable, filterable data tables
- **`ExportButton`** - PDF and Excel export functionality
- **`FilterPanel`** - Advanced search and filtering

### **Layout Components**
- **`Layout`** - Common page structure
- **`Header`** - Navigation with search integration
- **`Footer`** - Site information and links

## 🔌 API Integration

The frontend communicates with the backend using advanced API services with caching and error handling:

### **Company Services**
```javascript
// Company search with advanced filters
export const searchCompanies = async (query, filters = {}) => {
  const params = {
    q: query,
    industry: filters.industry,
    min_employees: filters.minEmployees,
    financial_health_min: filters.minHealthScore,
    ...filters
  };
  return api.get('/api/search', { params });
};

// Get comprehensive company details
export const getCompanyDetails = async (regNumber) => {
  return api.get(`/api/company/${regNumber}`);
};
```

### **Financial Analysis Services**
```javascript
// Get financial health score
export const getHealthScore = async (regNumber) => {
  return api.get(`/api/financial/${regNumber}/health-score`);
};

// Get multi-year financial trends
export const getFinancialTrends = async (regNumber, years = 5) => {
  return api.get(`/api/financial/${regNumber}/trends`, {
    params: { years }
  });
};

// Get financial ratios analysis
export const getFinancialRatios = async (regNumber) => {
  return api.get(`/api/financial/${regNumber}/ratios`);
};

// Get risk assessment
export const getRiskAssessment = async (regNumber) => {
  return api.get(`/api/financial/${regNumber}/risk-assessment`);
};
```

### **Analytics Services**
```javascript
// Get industry benchmarks
export const getIndustryBenchmarks = async (regNumber) => {
  return api.get(`/api/analytics/benchmarks/${regNumber}`);
};

// Bulk company analysis
export const bulkAnalysis = async (companyList) => {
  return api.post('/api/analytics/bulk-analysis', { companies: companyList });
};
```

## 🔧 Environment Variables

### **Required Configuration**
```bash
# API Configuration
VITE_API_URL=http://localhost:8000              # Backend API URL
VITE_SUPABASE_URL=your_supabase_url            # Supabase project URL
VITE_SUPABASE_ANON_KEY=your_anon_key           # Supabase anonymous key

# Feature Flags
VITE_ENABLE_ADVANCED_CHARTS=true               # Enable advanced chart features
VITE_ENABLE_EXPORT_FEATURES=true               # Enable PDF/Excel export
VITE_ENABLE_REAL_TIME_UPDATES=true             # Enable real-time data updates

# Performance Configuration
VITE_FINANCIAL_DATA_CACHE_TTL=3600             # Cache TTL for financial data (seconds)
VITE_API_REQUEST_TIMEOUT=30000                 # API request timeout (milliseconds)
VITE_MAX_SEARCH_RESULTS=50                     # Maximum search results per page

# Analytics Configuration
VITE_GOOGLE_ANALYTICS_ID=your_ga_id            # Google Analytics tracking (optional)
VITE_ENABLE_USER_ANALYTICS=false               # User behavior tracking
```

## 🚀 Development Workflow

### **Start Development Server**
```bash
npm run dev                    # Start development server
npm run build                  # Build for production
npm run preview               # Preview production build
npm run lint                  # Run ESLint
```

### **Testing**
```bash
npm run test                  # Run unit tests (planned)
npm run test:e2e              # Run end-to-end tests (planned)
npm run test:coverage         # Generate coverage report (planned)
```

## 🎨 Theming & Customization

### **Chakra UI Theme**
```javascript
// theme/index.js
export const theme = {
  colors: {
    brand: {
      50: '#E6F7FF',
      500: '#1890FF',
      900: '#003A8C'
    },
    success: '#52C41A',
    warning: '#FAAD14',
    error: '#FF4D4F'
  },
  components: {
    Button: {
      // Custom button styles
    },
    Card: {
      // Custom card styles
    }
  }
};
```

## 📱 Responsive Design

### **Breakpoints**
- **Mobile**: 320px - 767px
- **Tablet**: 768px - 1023px  
- **Desktop**: 1024px+

### **Component Responsiveness**
- **Charts**: Adaptive sizing based on screen width
- **Tables**: Horizontal scrolling on mobile
- **Navigation**: Collapsible menu for mobile
- **Cards**: Stack vertically on smaller screens

## 🔒 Security Features

### **Data Protection**
- **Input Sanitization** - All user inputs sanitized
- **XSS Prevention** - React's built-in XSS protection
- **HTTPS Only** - Secure data transmission
- **API Rate Limiting** - Frontend respects backend rate limits

### **Access Control**
- **Environment Variables** - Secure configuration
- **API Key Management** - Secure external service access
- **CORS Handling** - Proper cross-origin request handling

## 📊 Performance Optimization

### **Optimization Strategies**
- **Code Splitting** - Route-based lazy loading
- **Image Optimization** - WebP format with fallbacks
- **Bundle Analysis** - Regular bundle size monitoring
- **Caching Strategy** - Intelligent data caching

### **Performance Metrics**
- **First Contentful Paint**: <1.5s
- **Largest Contentful Paint**: <2.5s
- **Cumulative Layout Shift**: <0.1
- **First Input Delay**: <100ms

---

**TURBO_AML Frontend** - *Intuitive Financial Intelligence at Your Fingertips* 