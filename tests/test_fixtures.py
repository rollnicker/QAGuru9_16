"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


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


def test_github_desktop(setup_desktop):
    browser.open("")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


def test_github_mobile(setup_mobile):
    browser.open("")
    browser.element(".Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
