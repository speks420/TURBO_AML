# 🌐 TURBO_AML External Deployment Guide

Quick guide for deploying TURBO_AML for external access and testing.

## 🚀 **Quick Setup (First Time)**

### **1. Create Environment Files**
```cmd
# Copy example to create actual .env files
copy .env.example .env
copy backend\.env.example backend\.env  
copy frontend\.env.example frontend\.env
```

### **2. Update Your IP Address**
```cmd
# Use the IP update script
update-ip.bat 95.68.116.88

# Or manually edit .env files with your IP
```

### **3. Choose Deployment Type**

**For Development/Testing:**
```cmd
docker-compose -f docker-compose.dev.yml up --build -d
```
- Frontend: http://YOUR_IP:5173
- Backend: http://YOUR_IP:8000/docs

**For Production (Recommended for external users):**
```cmd
docker-compose -f docker-compose.prod.yml up --build -d
```
- Application: http://YOUR_IP
- API: http://YOUR_IP/api/docs

## 🔄 **Daily IP Updates**

When your IP changes (e.g., 95.68.116.88 → 96.70.118.90):

```cmd
# Simple one-liner
update-ip.bat 96.70.118.90

# Then choose:
# 1 = Development
# 2 = Production  
# 3 = Just update (no restart)
```

## 🔧 **Environment Variables**

### **Root `.env`**
```bash
EXTERNAL_IP=95.68.116.88        # Your current external IP
DEBUG=true                      # Enable for testing
SUPABASE_URL=https://...        # Your Supabase URL
SUPABASE_ANON_KEY=...          # Your Supabase anon key
# ... other CKAN and config vars
```

### **Backend `.env`**
```bash
EXTERNAL_IP=95.68.116.88        # Same as root
DEBUG=True                      # Enable CORS debugging
SUPABASE_URL=...               # Supabase credentials
# ... other backend config
```

### **Frontend `.env`**
```bash
VITE_API_URL=http://95.68.116.88:8000    # Points to your backend
VITE_SUPABASE_URL=...                    # Supabase URL
VITE_SUPABASE_ANON_KEY=...              # Supabase anon key
```

## 🔥 **Firewall Setup (Windows)**

### **Automatic (Run as Administrator):**
```cmd
netsh advfirewall firewall add rule name="TURBO_AML HTTP" dir=in action=allow protocol=TCP localport=80
netsh advfirewall firewall add rule name="TURBO_AML Dev Frontend" dir=in action=allow protocol=TCP localport=5173
netsh advfirewall firewall add rule name="TURBO_AML API" dir=in action=allow protocol=TCP localport=8000
```

### **Manual:**
1. Open Windows Defender Firewall
2. Add inbound rules for ports: **80**, **5173**, **8000**

## 🌍 **Router Configuration (For Internet Access)**

If you want external internet access:
1. Forward ports **80** and **8000** to your PC's local IP
2. Use your **public IP** instead of local IP
3. Update DNS/domain if needed

## 🧪 **Testing Checklist**

**Local Testing:**
- [ ] http://localhost:5173 (dev) or http://localhost (prod)
- [ ] http://localhost:8000/docs (API)

**Network Testing:**
- [ ] http://YOUR_IP:5173 (dev) or http://YOUR_IP (prod)
- [ ] http://YOUR_IP:8000/docs (API)

**External Testing:**
- [ ] Company search works
- [ ] Health score loads without errors
- [ ] No CORS errors in browser console

## 🐛 **Troubleshooting**

### **CORS Errors:**
```cmd
# Check current CORS configuration
curl http://YOUR_IP:8000/cors-info
```

### **IP Update Issues:**
```cmd
# Manual IP update in files
notepad .env                    # Update EXTERNAL_IP=NEW_IP
notepad backend\.env           # Update EXTERNAL_IP=NEW_IP  
notepad frontend\.env          # Update VITE_API_URL=http://NEW_IP:8000
```

### **Docker Issues:**
```cmd
# Full restart
docker-compose -f docker-compose.prod.yml down
docker system prune -f
docker-compose -f docker-compose.prod.yml up --build -d
```

### **Check Logs:**
```cmd
docker-compose -f docker-compose.prod.yml logs -f
```

## 📋 **Quick Commands Reference**

```cmd
# Update IP and deploy production
update-ip.bat YOUR_NEW_IP

# Start production
docker-compose -f docker-compose.prod.yml up --build -d

# Start development  
docker-compose -f docker-compose.dev.yml up --build -d

# Stop everything
docker-compose -f docker-compose.prod.yml down
docker-compose -f docker-compose.dev.yml down

# Check status
docker ps

# View logs
docker-compose -f docker-compose.prod.yml logs -f
```

## 🎯 **For Testers**

Send testers this URL:
- **Production:** http://YOUR_IP
- **Development:** http://YOUR_IP:5173

They can test:
1. Company search (try "RA Factory")
2. Company details and health scores
3. Financial data loading

---

**Current IP:** 95.68.116.88 (update with `update-ip.bat NEW_IP`) 