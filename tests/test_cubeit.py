from playwright.sync_api import Page, expect
from random import randint

BASE_URL = "http://localhost:8000/"

def test_cube(page: Page):
    page.goto(BASE_URL)

    number_input = page.locator('#numberInput')
    random_int = randint(1, 100)
    
    number_input.fill(str(random_int))

    page.locator("#cubeButton").click()

    result = page.locator('#result')

    expect(result).to_contain_text(f" = {random_int**3}")


def test_blank_input(page: Page):
    page.goto(BASE_URL)

    page.locator("#cubeButton").click()

    result = page.locator('#result')

    expect(result).to_contain_text(f"Put in something")

