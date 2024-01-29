"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selene import browser, have


# @pytest.mark.parametrize("height, width",
#                          [(1980, 1280), (1080, 720)],
#                          ids=["PC", "Mobile"]
#                          )
# def select_browser(device):
#     assert device in [1980, 1080]
#
#
# @pytest.mark.parametrize("device", ["Desktop", "Mobile"])
# def select_browser(device):
#     return device


@pytest.fixture(autouse=True)
def setup_browser(device):
    if device == "Desktop":
        browser.config.window_height = 1980
        browser.config.window_width = 1280
        browser.config.base_url = 'https://github.com/'
    elif device == "Mobile":
        browser.config.window_height = 720
        browser.config.window_width = 480
        browser.config.base_url = 'https://github.com/'


@pytest.mark.parametrize("device",
                         [
                             pytest.param("Desktop"),
                             pytest.param(("Mobile"), marks=[pytest.mark.skip(reason="Запускать только на компе")])
                         ]
                         )
def test_github_desktop(device):
    browser.open("")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize("device",
                         [
                             pytest.param(("Desktop"), marks=[pytest.mark.skip(reason="Запускать только на компе")]),
                             pytest.param("Mobile")
                         ]
                         )
def test_github_desktop(device):
    browser.open("")
    browser.element(".Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
