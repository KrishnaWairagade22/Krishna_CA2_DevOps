"""
conftest.py - Pytest configuration and fixtures
================================================
Provides the shared 'driver' fixture for all Selenium test cases.
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that creates a Chrome WebDriver instance.
    Automatically uses headless mode when running inside Jenkins or CI.
    """
    options = webdriver.ChromeOptions()

    # Run headless in Jenkins / CI environments
    if (os.getenv("JENKINS_URL")
            or os.getenv("GITHUB_ACTIONS")
            or os.getenv("HEADLESS") == "true"):
        print("\n[conftest] Running in HEADLESS mode (Jenkins detected)")
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    # Suppress Chrome logging noise
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")

    driver_instance = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver_instance

    # Teardown: quit after every test
    driver_instance.quit()
