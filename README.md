# TODO: Self-Hosted Matrix Messenger with Ansible + Docker

## Goal:
Deploy a fully self-contained Matrix-based messenger stack (Synapse, Element, Coturn, Nginx) using Ansible and Docker, suitable for use in internal networks even when internet access is restricted.

---

## Pre-requisites

- [ ] VPS or local server (with root or sudo access)
- [ ] A local/internal domain (e.g. `chat.local` or `matrix.mycompany.ir`)
- [ ] Ansible installed on the control machine
- [ ] Python Docker SDK installed (`pip install docker`)
- [ ] SSH access to target machine

---

## 📁 Project Structure

- [ ] Create base project structure:


---

## 🔧 Ansible Setup

- [x] Create inventory file (`hosts.yml`)
- [x] Define all roles:
- [x] `docker` – install Docker
- [ ] `nginx` – deploy Nginx container with proper config
- [ ] `coturn` – configure and run Coturn for VoIP
- [ ] `synapse` – deploy Synapse server using Docker
- [ ] `element` – deploy Element client container

---

## 📦 Role: docker

- [x] Requirements
- [x] Set dns
- [x] Install Docker
- [x] Set registery mirror
- [x] Configuration

---

## 🌐 Role: Nginx

- [ ] Write a `nginx.conf.j2` template
- [ ] Configure reverse proxy for:
- `/_matrix`
- `/.well-known/matrix/client`
- `/element`
- [ ] Set up SSL (optional/self-signed if offline)

---

## 📞 Role: Coturn

- [ ] Create turnserver.conf template
- [ ] Expose port `3478` (UDP & TCP)
- [ ] Run Docker container for coturn

---

## 💬 Role: Synapse

- [x] Generate initial config using Docker (or provide template)
- [x] Set SQLite DB path
- [x] Configure `homeserver.yaml` (via Jinja template)
- [x] Expose port `8008`
- [x] Add support for custom domain and federation disabled

---

## 🧑‍💻 Role: Element

- [x] Download image (`vectorim/element-web`)
- [x] Template `config.json`
- [x] Mount it to `/app/config.json`
- [x] Expose on Nginx as `/element/`

---

## 🔐 TLS & Domains

- [ ] Support for:
- [ ] Self-signed certificates (for internal network)
- [ ] Let’s Encrypt (optional, if public access exists)
- [ ] Add a task for `/etc/hosts` editing (if no DNS)

---

## 🚀 Deployment & Testing

- [ ] Write `site.yml` to include all roles in correct order
- [ ] Run playbook
- [ ] Test access:
- [ ] `https://chat.local/element`
- [ ] Register new user
- [ ] Try chat
- [ ] Test voice/video calls (via Coturn)

---

## 📈 Future Improvements

- [ ] Replace SQLite with PostgreSQL
- [ ] Add monitoring (Prometheus/Grafana)
- [ ] Add backup/restore scripts
- [ ] Add registration token/approval system
