# Smart Task Manager - Deployment Guide

## Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Database backups in place
- [ ] SSL certificate obtained
- [ ] Domain name configured
- [ ] Server provisioned
- [ ] Monitoring setup

## Production Environment Setup

### 1. Server Requirements

**Recommended Specifications:**
- OS: Ubuntu 20.04+ or CentOS 8+
- CPU: 2+ cores
- RAM: 2GB+ 
- Storage: 20GB+ SSD
- Python: 3.8+
- PostgreSQL: 12+

### 2. Initial Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3.10 python3-pip python3-venv git

# Install PostgreSQL
sudo apt install -y postgresql postgresql-contrib

# Install Nginx
sudo apt install -y nginx

# Install Gunicorn
pip3 install gunicorn
```

### 3. Clone and Setup Application

```bash
# Create app directory
sudo mkdir -p /var/www/smart-task-manager
cd /var/www/smart-task-manager

# Clone repository (or upload files)
git clone <repository-url> .
# or: scp -r smart-task-manager/* user@server:/var/www/smart-task-manager/

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

```bash
# Switch to postgres user
sudo -u postgres psql

# Create database and user
CREATE DATABASE smart_task_db;
CREATE USER stm_user WITH PASSWORD 'strong_password_here';
ALTER ROLE stm_user SET client_encoding TO 'utf8';
ALTER ROLE stm_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE stm_user SET default_transaction_deferrable TO on;
ALTER ROLE stm_user SET default_transaction_read_only TO off;
GRANT ALL PRIVILEGES ON DATABASE smart_task_db TO stm_user;
\q
```

### 5. Configure Application

```bash
cd /var/www/smart-task-manager

# Create production .env
nano .env

# Add the following content:
DATABASE_URL=postgresql+psycopg2://stm_user:strong_password_here@localhost:5432/smart_task_db
SECRET_KEY=your-secret-key-generate-one-from-python
FLASK_ENV=production
SOCKETIO_CORS_ALLOWED_ORIGINS=https://yourdomain.com

# Generate secret key:
python3 -c "import secrets; print(secrets.token_hex(32))"

# Initialize database
source venv/bin/activate
python3 app.py
# Press Ctrl+C after seeing tables created
```

### 6. Configure Gunicorn

Create `/etc/systemd/system/smart-task-manager.service`:

```ini
[Unit]
Description=Smart Task Manager Flask Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/smart-task-manager
Environment="PATH=/var/www/smart-task-manager/venv/bin"
ExecStart=/var/www/smart-task-manager/venv/bin/gunicorn \
    --workers 4 \
    --worker-class eventlet \
    --bind unix:/var/www/smart-task-manager/smart_task_manager.sock \
    app:app

[Install]
WantedBy=multi-user.target
```

### 7. Configure Nginx

Create `/etc/nginx/sites-available/smart-task-manager`:

```nginx
upstream smart_task_manager {
    server unix:/var/www/smart-task-manager/smart_task_manager.sock fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css text/javascript 
               application/javascript application/json;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";

    # Client limits
    client_max_body_size 10M;

    location / {
        proxy_pass http://smart_task_manager;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    # WebSocket support
    location /socket.io {
        proxy_pass http://smart_task_manager/socket.io;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Static files caching
    location /static {
        alias /var/www/smart-task-manager/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

### 8. Enable and Start Services

```bash
# Enable Nginx site
sudo ln -s /etc/nginx/sites-available/smart-task-manager \
           /etc/nginx/sites-enabled/

# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Test Nginx config
sudo nginx -t

# Start services
sudo systemctl daemon-reload
sudo systemctl start smart-task-manager
sudo systemctl enable smart-task-manager
sudo systemctl restart nginx

# Verify status
sudo systemctl status smart-task-manager
sudo systemctl status nginx
```

### 9. Set up SSL Certificate (Let's Encrypt)

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Obtain certificate
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo certbot renew --dry-run
```

### 10. Configure Firewall

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

## Monitoring and Maintenance

### 1. Set up Logging

Create `/etc/rsyslog.d/smart-task-manager.conf`:

```
:programname, isequal, "gunicorn" /var/log/smart-task-manager/gunicorn.log
```

### 2. Database Backups

Create `/usr/local/bin/backup-stm-db.sh`:

```bash
#!/bin/bash
BACKUP_DIR="/backups/smart-task-manager"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Backup database
pg_dump smart_task_db | gzip > $BACKUP_DIR/smart_task_db_$DATE.sql.gz

# Keep only last 30 days
find $BACKUP_DIR -name "*.sql.gz" -mtime +30 -delete

# Optional: Upload to S3
# aws s3 cp $BACKUP_DIR/smart_task_db_$DATE.sql.gz s3://your-bucket/backups/
```

Make it executable and add to crontab:

```bash
chmod +x /usr/local/bin/backup-stm-db.sh

# Daily backups at 2 AM
0 2 * * * /usr/local/bin/backup-stm-db.sh
```

### 3. Monitor Application Health

```bash
# Check if service is running
sudo systemctl status smart-task-manager

# View logs
sudo journalctl -u smart-task-manager -f

# Check database connection
psql -U stm_user -d smart_task_db -c "SELECT version();"

# Check disk usage
df -h
du -sh /var/www/smart-task-manager
```

### 4. Performance Monitoring

Install monitoring tools:

```bash
# New Relic (recommended)
pip install newrelic
export NEW_RELIC_CONFIG_FILE=newrelic.ini

# Or use open-source alternatives
pip install prometheus-client
```

### 5. Update Application

```bash
cd /var/www/smart-task-manager

# Pull latest changes
git pull origin main

# Activate venv
source venv/bin/activate

# Install new dependencies
pip install -r requirements.txt

# Restart application
sudo systemctl restart smart-task-manager
```

## Troubleshooting

### Application Won't Start

```bash
# Check logs
sudo journalctl -u smart-task-manager -n 50

# Test Python app directly
cd /var/www/smart-task-manager
source venv/bin/activate
python3 app.py
```

### Database Connection Error

```bash
# Test connection
psql -U stm_user -d smart_task_db -c "SELECT 1"

# Check PostgreSQL logs
sudo tail -f /var/log/postgresql/postgresql.log
```

### WebSocket Not Working

```bash
# Check Nginx logs
sudo tail -f /var/log/nginx/error.log

# Verify WebSocket in Nginx config
grep -A 5 "socket.io" /etc/nginx/sites-available/smart-task-manager
```

### High CPU/Memory Usage

```bash
# Monitor processes
top

# Increase Gunicorn workers cautiously
# Edit /etc/systemd/system/smart-task-manager.service
# Change --workers 4 to --workers 8 (for 4+ CPU cores)
```

## Performance Tuning

### 1. Nginx Optimization

```nginx
# Increase worker processes
worker_processes auto;

# Increase connections
worker_connections 2048;

# Enable caching
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;
```

### 2. PostgreSQL Optimization

```sql
-- Check current settings
SHOW max_connections;
SHOW shared_buffers;

-- Increase connections (in postgresql.conf)
max_connections = 100
shared_buffers = 256MB
effective_cache_size = 1GB
```

### 3. Gunicorn Optimization

Adjust worker count based on CPU cores:
- 2-4 cores: 4-8 workers
- 4+ cores: 8-16 workers
- Formula: (2 × CPU cores) + 1

## Security Hardening

### 1. Fail2Ban

```bash
sudo apt install fail2ban

# Create jail for Flask app
sudo nano /etc/fail2ban/jail.local
```

### 2. Rate Limiting

Add to Nginx config:

```nginx
limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
limit_req zone=general burst=20 nodelay;
```

### 3. Environment Variables

```bash
# Never commit secrets to git
# Use environment variables for all sensitive data
# Rotate secrets regularly
```

## Rollback Procedure

```bash
# Tag versions in git
git tag -a v1.0.0 -m "Production release"
git push origin v1.0.0

# Rollback to previous version
cd /var/www/smart-task-manager
git checkout v0.9.0
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart smart-task-manager
```

## Disaster Recovery

### Database Disaster Recovery

```bash
# Restore from backup
psql -U stm_user -d smart_task_db < backup.sql.gz

# Verify data
psql -U stm_user -d smart_task_db -c "SELECT COUNT(*) FROM users;"
```

### Full Server Recovery

1. Provision new server
2. Follow initial setup steps
3. Restore database from backup
4. Deploy application code
5. Run smoke tests
6. Update DNS records

## Production Checklist

- [ ] SSL certificate installed and valid
- [ ] Database backups automated and tested
- [ ] Monitoring and alerting configured
- [ ] Log aggregation set up
- [ ] Error tracking (Sentry) enabled
- [ ] Rate limiting configured
- [ ] CORS properly configured
- [ ] Secret keys rotated
- [ ] Security headers configured
- [ ] All tests passing
- [ ] Load testing completed
- [ ] Disaster recovery plan documented
- [ ] Team trained on deployment process
- [ ] Documentation updated
