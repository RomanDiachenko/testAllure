# Use OpenJDK base image (required for Allure)
FROM openjdk:11-slim

# Install required packages
RUN apt-get update && apt-get install -y wget unzip python3

# Download and install Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.zip && \
    unzip allure-2.25.0.zip && \
    mv allure-2.25.0 /opt/allure && \
    rm allure-2.25.0.zip

# Add Allure to system PATH
ENV PATH="/opt/allure/bin:${PATH}"

# Set working directory inside the container
WORKDIR /app

# Copy test results (from local machine)
COPY allure-results/ /app/allure-results

# On container start:
# 1. Generate static Allure Report
# 2. Serve it via simple HTTP server (Python built-in)
CMD allure generate /app/allure-results -o /app/allure-report --clean && \
    cd /app/allure-report && \
    python3 -m http.server 8080
