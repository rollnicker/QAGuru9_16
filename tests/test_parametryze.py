"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have

desktop_only = pytest.mark.parametrize("setup_browser", ["Desktop"], indirect=True)
mobile_only = pytest.mark.parametrize("setup_browser", ["Mobile"], indirect=True)


@pytest.fixture(params=["Desktop", "Mobile"], autouse=True)
def setup_browser(request):
    browser.config.base_url = 'https://github.com/'
    if request.param == "Desktop":
        browser.config.window_height = 1980
        browser.config.window_width = 1280

    elif request.param == "Mobile":
        browser.config.window_height = 720
        browser.config.window_width = 480


@desktop_only
def test_github_desktop():
    browser.open("")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@mobile_only
def test_github_mobile():
    browser.open("")
    browser.element(".Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
