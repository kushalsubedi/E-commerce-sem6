server {
    listen 8000;
    server_name 0.0.0.0:8000;

    location /static/ {
        alias ../../static/staticfiles/;
    }

    location / {
        proxy_pass http://app:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
