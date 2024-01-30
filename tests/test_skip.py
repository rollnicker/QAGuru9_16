"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selene import browser, have



@pytest.mark.parametrize("device",
                         [
                             pytest.param("Desktop"),
                             pytest.param(("Mobile"), marks=[pytest.mark.skip(reason="Не работает "
                                                                                     "в мобильном разрешении")])
                         ]
                         )
def test_github_desktop(setup_browser, device):
    browser.open("")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize("device",
                         [
                             pytest.param(("Desktop"), marks=[pytest.mark.skip(reason="Не работает в десктопном "
                                                                                      "разрешении")]),
                             pytest.param("Mobile")
                         ]
                         )
def test_github_mobile(setup_browser, device):
    browser.open("")
    browser.element(".Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
