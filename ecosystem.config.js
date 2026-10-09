module.exports = {
  apps: [
    {
      name: "storage-minio",
      script: "uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 7003",
      interpreter: "./venv/bin/python",
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: "500M",
      
      // Logs
      time: true,
      log_date_format: "YYYY-MM-DD HH:mm:ss",
      error_file: "./logs/pm2-error.log",
      out_file: "./logs/pm2-out.log",
      merge_logs: true,

      env: {
        NODE_ENV: "production",
      }
    }
  ]
};