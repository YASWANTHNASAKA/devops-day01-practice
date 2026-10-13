import http.server
import socketserver

PORT = 8080

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>DevOps Capstone Application</title>
        </head>
        <body style='font-family: Arial, sans-serif; text-align: center; margin-top: 50px;'>
            <h1>DevOps Microservice Portal</h1>
            <p>Running on Python 3 Standard HTTP Server</p>
            <p>Ready for Docker Containerization (Day 02)</p>
        </body>
        </html>
        """

exit
cat << 'EOF' > README.md
# DevOps Capstone Project

## Description
This repository contains the baseline code for the CDAC PGCP-ITISS DevOps curriculum.

## Module Milestones
* **Day 01:** Git & GitHub Version Control (Windows Workstation)
* **Day 02:** Docker Containerization & Dockerfile packaging
* **Day 03:** Multi-Container Stacks (Compose) & Swarm Orchestration
* **Day 04:** Kubernetes Deployment Manifests & Prometheus Monitoring
* **Day 05:** Jenkins Automated CI/CD Pipelines
* **Day 06-10:** Infrastructure Automation (Terraform, Ansible, Chef, Puppet)
