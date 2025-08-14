FROM jenkins/jenkins:lts
USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip wget unzip gnupg curl apt-transport-https ca-certificates

# Google Chrome kurulumu
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# ChromeDriver kurulumu (sabit sürüm)
RUN CHROME_DRIVER_VERSION=128.0.6613.137 && \
    wget -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_DRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /tmp && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver

RUN pip3 install --no-cache-dir --break-system-packages pytest selenium allure-pytest

USER jenkins
