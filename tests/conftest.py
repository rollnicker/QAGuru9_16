import pytest
from selene import browser

#
# @pytest.fixture(autouse=True)
# def setup_browser2(device):
#     if device == "Desktop":
#         browser.config.window_height = 1980
#         browser.config.window_width = 1280
#         browser.config.base_url = 'https://github.com/'
#     elif device == "Mobile":
#         browser.config.window_height = 720
#         browser.config.window_width = 480
#         browser.config.base_url = 'https://github.com/'


@pytest.fixture(params=["Desktop", "Mobile"])
def setup_browser(request, device):
    browser.config.base_url = 'https://github.com/'
    if request.param == "Desktop" or device == "Desktop":
        browser.config.window_height = 1980
        browser.config.window_width = 1280
    elif request.param == "Mobile" or device == "Mobile":
        browser.config.window_height = 720
        browser.config.window_width = 480


@pytest.fixture()
def setup_desktop():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_height = 1980
    browser.config.window_width = 1280


@pytest.fixture()
def setup_mobile():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_height = 720
    browser.config.window_width = 480
