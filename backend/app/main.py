"""
Main FastAPI application entry point.
"""
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.api.endpoints import search, company, financial

# Custom middleware to handle cookies
class CookieMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Check if response has cookies attribute (added by our handlers)
        if hasattr(response, "cookies") and response.cookies:
            for cookie_name, cookie_value in response.cookies.items():
                response.set_cookie(
                    key=cookie_name,
                    value=cookie_value,
                    httponly=False,  # Allow JavaScript access for frontend
                    samesite="lax",
                    max_age=60 * 60 * 24 * 30,  # 30 days
                )
        
        return response

# Create FastAPI app
app = FastAPI(
    title="TURBO_AML API",
    description="API for accessing Latvian company information",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
     allow_origins=["http://localhost:5173", "http://localhost:3000"],  # FIXED
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom cookie middleware
app.add_middleware(CookieMiddleware)

# Import and include API routers
app.include_router(search.router, prefix="/api", tags=["search"])
app.include_router(company.router, prefix="/api", tags=["company"])
app.include_router(financial.router, prefix="/api", tags=["financial"])

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to TURBO_AML API"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"} 