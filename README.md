# FastAPI App — DigitalOcean Deployment

A simple FastAPI server ready to deploy on DigitalOcean App Platform.

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Hello world message |
| GET | `/health` | Health check |
| GET | `/items/{item_id}` | Get an item by ID |
| POST | `/echo` | Echo back a JSON body |
| GET | `/docs` | Swagger UI (auto-generated) |

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit: http://localhost:8000

## Deploy to DigitalOcean (Step-by-Step)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial FastAPI app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Deploy on DigitalOcean App Platform
1. Go to https://cloud.digitalocean.com/apps
2. Click **Create App**
3. Connect your **GitHub** account and select your repo
4. DigitalOcean will detect Python — confirm the settings
5. Make sure the **Run Command** is:
   ```
   gunicorn -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --worker-tmp-dir /dev/shm main:app
   ```
6. Choose the **Basic** plan (free tier available)
7. Click **Create Resources**

Your app will be live at a URL like:
`https://your-app-name.ondigitalocean.app`