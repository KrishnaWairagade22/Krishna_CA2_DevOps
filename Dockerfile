# ─────────────────────────────────────────────────────────
# Dockerfile for Student Feedback Registration Form
# Aim 6: Containerization using Docker
#
# Base image: nginx:alpine
#   - nginx  = lightweight web server to serve static files
#   - alpine = minimal Linux (only ~5MB), keeps image small
# ─────────────────────────────────────────────────────────

FROM nginx:alpine

# Set working directory label for documentation
LABEL maintainer="KrishnaWairagade22"
LABEL description="Student Feedback Registration Form - Containerized with Docker"
LABEL version="1.0"

# Remove the default nginx welcome page
RUN rm -rf /usr/share/nginx/html/*

# Copy all application files into the nginx web root
COPY index.html  /usr/share/nginx/html/index.html
COPY styles.css  /usr/share/nginx/html/styles.css
COPY script.js   /usr/share/nginx/html/script.js

# Expose port 80 (HTTP) — this is the port nginx listens on inside the container
EXPOSE 80

# Start nginx in the foreground (required for Docker containers)
CMD ["nginx", "-g", "daemon off;"]
