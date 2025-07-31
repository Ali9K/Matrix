# Matrix Stack Deployment with Ansible & Docker

This repository contains an Ansible collection that fully deploys a containerized Matrix stack using Docker.
The included roles and tasks are executed in the following order:

* Two initial tasks in `playbook.yml` to create Docker public and private networks
* **Coturn**, a TURN server for voice and video calls (TCP enabled for better connectivity in restrictive networks such as Iran)
* **PostgreSQL**, used as the database for Synapse
* **Synapse**, the Matrix homeserver backend
* **Element**, the web-based Matrix client
* **NGINX**, serving as a reverse proxy
* **Certbot**, to obtain TLS certificates via Let's Encrypt

All components are deployed in isolated Docker containers and are configured to work seamlessly together out of the box.

---

## Requirements

* Ansible
* Docker
* Python

---

## Getting Started

This project is designed to run Ansible on the local environment by default.
However, you can easily modify the `hosts.yml` file to deploy it on any host or even across multiple hosts.

Each role and task is tagged, allowing you to selectively run parts of the playbook using `--tags`, or skip them using `--skip-tags`.

All major configuration files (such as `homeserver.yaml`) are written as Jinja2 templates, making them easy to customize prior to deployment.
For example, user registration in Synapse is disabled by default to prevent unauthorized access.
You can enable it by editing the following line in `homeserver.yaml`:

```yaml
enable_registration: false
```

To manually register users using shared secret authentication, run:

```bash
docker exec -it synapse register_new_matrix_user \
  -u yourusername -p yourpassword \
  -a http://localhost:8008 \
  --no-admin \
  --shared-secret yoursharedsecret
```

Coturn is also configured to support the TCP protocol.
Ensuring that voice and video calls function reliably even in environments like Iran where UDP traffic may be restricted.

SMTP settings have also been configured in Synapse, enabling email notifications such as password resets and account verification.

After updating the `hosts.yml`, adjusting the configuration template files, and setting the appropriate variables,
 you can run the Ansible playbook with:

```bash
ansible-playbook -i inventories/hosts.yml playbook.yml --ask-become-pass
```

Make sure all required variables are defined in your inventory files, `group_vars`, or `defaults`.

---

## License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it with proper attribution.

---

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

**Email:** [ali99kalbasi82@gmail.com](mailto:ali99kalbasi82@gmail.com)

I'd be happy to hear from you!
