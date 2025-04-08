FROM openjdk:11-slim

RUN apt-get update && apt-get install -y wget unzip python3

RUN wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.zip && \
    unzip allure-2.25.0.zip && \
    mv allure-2.25.0 /opt/allure && \
    rm allure-2.25.0.zip

ENV PATH="/opt/allure/bin:${PATH}"

WORKDIR /app

# Create empty folder in case allure-results is not copied
RUN mkdir -p /app/allure-results

# Copy test results (replace this step in CI with real test results)
COPY allure-results/ /app/allure-results

CMD allure generate /app/allure-results -o /app/allure-report --clean && \
    cd /app/allure-report && \
    python3 -m http.server 8080