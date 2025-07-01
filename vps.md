# 🛣️ Matrix Server Deployment Roadmap

This roadmap guides the deployment of a self-hosted Matrix server stack with Synapse, Element, Coturn, and NGINX on a VPS using Docker.

---

## ✅ Phase 1: Prepare the VPS

- [ ] Purchase and provision a VPS (Ubuntu 22.04 or Debian 12)
- [ ] Set up SSH access
- [ ] Update and secure the system:
  - [ ] `sudo apt update && sudo apt upgrade`
  - [ ] Enable UFW or firewall
  - [ ] Set up fail2ban (optional)

---

## 🐳 Phase 2: Install Dependencies

- [ ] Install Docker
- [ ] Install Docker Compose (or set up Ansible for orchestration)
- [ ] Install NGINX
- [ ] Install Certbot (`sudo apt install certbot python3-certbot-nginx`)

---

## 🌐 Phase 3: Domain & SSL

- [ ] Point domain (e.g., `matrix.example.com`) to VPS IP
- [ ] Open ports `80`, `443`, `3478` (TURN), and `5349` (TURN TLS)
- [ ] Obtain and install SSL certificate with Certbot:
  - [ ] `sudo certbot --nginx -d matrix.example.com`

---
<!-- 
## ⚙️ Phase 4: Synapse Setup

- [ ] Create `synapse/` folder
- [ ] Generate `homeserver.yaml` (or use Jinja template)
- [ ] Configure:
  - [ ] `server_name`
  - [ ] `public_baseurl`
  - [ ] `database` (SQLite or PostgreSQL)
  - [ ] `listeners`
  - [ ] `registration`, `media`, and `turn`
- [ ] Create `docker-compose.yml` for Synapse
- [ ] Verify Synapse starts correctly on port 8008 -->

---
<!-- 
## 🧊 Phase 5: Coturn (TURN server)

- [ ] Install and configure Coturn
  - [ ] Shared secret
  - [ ] Allowed peer IPs
  - [ ] TLS (optional)
- [ ] Open ports `3478`/`5349`
- [ ] Connect Coturn to Synapse config (`turn_uris`, `turn_shared_secret`)
- [ ] Test TURN functionality (optional) -->

---

## 🧱 Phase 6: NGINX Reverse Proxy

- [ ] Configure NGINX to proxy:
  - [ ] `/` → Element
  - [ ] `/_matrix` and `/_synapse/client` → Synapse
- [ ] Enable HTTPS using Let’s Encrypt certs
- [ ] Reload and test proxy routes

---

<!-- ## 💻 Phase 7: Deploy Element

- [ ] Clone or build Element Web
- [ ] Configure `config.json`:
  - [ ] `default_server_config` matches your Synapse server
- [ ] Serve via NGINX or Docker
- [ ] Test login, registration, room creation -->

---

## 🔄 Phase 8: Automation & Production Readiness

- [ ] Set up cron or systemd for:
  - [ ] Certbot renewal
  - [ ] Docker restarts
- [ ] Set up log rotation and monitoring (Prometheus/Grafana optional)
- [ ] Secure registration (disable open registration or add tokens)

---

## 🧪 Phase 9: Testing

- [ ] Test Synapse login via Element
- [ ] Test federation (connect to matrix.org)
- [ ] Test media upload
- [ ] Test voice/video calls (via Coturn)
- [ ] Test mobile app connection

---

## 📦 Optional Improvements

- [ ] Use PostgreSQL for production database
- [ ] Deploy bridges (Slack, Telegram, Discord, etc.)
- [ ] Integrate with LDAP or SSO
- [ ] Enable message retention policies

---

## 🧹 Maintenance Checklist

- [ ] Monitor logs and usage (`docker logs`, `journalctl`)
- [ ] Regularly update Docker images and security patches
- [ ] Backup database and media files
