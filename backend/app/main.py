"""
Main FastAPI application entry point.
"""
import os
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

# Dynamic CORS origins based on environment
def get_cors_origins():
    """Get CORS origins from environment variables for dynamic IP support."""
    external_ip = os.getenv("EXTERNAL_IP", "")
    
    origins = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    
    # Add external IP origins if provided
    if external_ip:
        origins.extend([
            f"http://{external_ip}",
            f"http://{external_ip}:5173",
            f"http://{external_ip}:3000",
            f"http://{external_ip}:80",
        ])
    
    # For development/testing, allow all origins if DEBUG is True
    if os.getenv("DEBUG", "False").lower() in ("true", "1", "t"):
        origins.append("*")
    
    return origins

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
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

@app.get("/cors-info")
async def cors_info():
    """Debug endpoint to see current CORS configuration."""
    return {
        "allowed_origins": get_cors_origins(),
        "external_ip": os.getenv("EXTERNAL_IP", "not_set"),
        "debug_mode": os.getenv("DEBUG", "False")
    } 