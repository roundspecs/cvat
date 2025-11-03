# 🧭 Deploying CVAT and Accessing It via Pinggy Tunnel (Developer Guide)

## 📋 Prerequisites

| Requirement | Version / Notes |
|--------------|----------------|
| Docker & Docker Compose | 20 + |
| Git | latest |
| Linux terminal | — |
| Pinggy account (free) | https://pinggy.io |


## 🧱 1. Clone the CVAT repository

```bash
cd ~
git clone https://github.com/roundspecs/cvat
cd cvat
```

## 🚀 2. Start CVAT with the overlay compose files

```bash
docker compose -f docker-compose.yml \
               -f docker-compose.settings_overlay.local.yml up -d
```

✳️ Wait about a minute for containers to initialize (Postgres, Redis, Traefik, etc.).

Check containers:

```bash
docker ps
```

You should see `cvat_server`, `cvat_ui`, and `traefik` running.

---

## 🧠 3. Verify the CSRF domains inside Django (optional)

```bash
docker exec -it cvat_server bash -ic \
"python3 ~/manage.py shell -c 'from django.conf import settings; print(settings.CSRF_TRUSTED_ORIGINS)'"
```

✅ Output should contain `['https://*.pinggy.link']`.

---

## 👑 4. Create a superuser (admin account)

```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```

Enter a username and password when prompted.
You’ll use these to log in to CVAT later.

---

## 🌐 5. Start a Pinggy tunnel to port 8080
See the dashboard in https://pinggy.io for details.

## 🧪 6. Access CVAT

1. Open the URL printed by Pinggy (e.g. `https://<random>.a.free.pinggy.link`).
2. You’ll see the CVAT login screen.
3. Log in with the credentials created in step 4.
4. Create projects and tasks normally — no “CSRF Failed” errors.

---

## 🔄 7. Restart later sessions

If you close/reboot, just run:

```bash
cd ~/cvat
docker compose -f docker-compose.yml \
               -f docker-compose.settings_overlay.local.yml up -d
ssh -p 443 -R0:localhost:8080 a.pinggy.io
```

That’s it — no need to edit settings again.

---

## 🧼 8. Shut down CVAT (when done)

```bash
docker compose down
```

To remove stored data completely (Postgres / Redis volumes):

```bash
docker compose down -v
```


# Resources
- https://epidemiology.tech/virtualization-containers/docker/cvat-install-behind-nginx-reverse-proxy/
- https://www.reddit.com/r/computervision/comments/1j4qzwl/issue_while_exposing_cvat_publically/