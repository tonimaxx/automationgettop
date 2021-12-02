from behave import given, when, then
from selenium.webdriver.common.by import By

expected_alt = {
    "ACCESSORIES": "Accessories",
    "IPAD": "iPad",
    "IPHONE": "iPhone",
    "MACBOOK": "MacBook",
}

@then("Verify all correct categories {category_list} are under Browse")
def verify_categories_under_browse(context, category_list):

    category = category_list.split("|")
    results = {}
    error_results = []
    not_found_input = []
    for n in category:
        this_expected_alt = expected_alt.get(n, "Not found")
        if this_expected_alt == "Not found":
            not_found_input.append(n)
        else:
            this_selector = f"[alt='{this_expected_alt}']"
            results[n] = context.app.base_page.find_elements(By.CSS_SELECTOR, this_selector)
            print(f"{n} > {this_selector} Found | ✓ Pass" if len(results[n]) > 0 else "Not Found | ✕ Fail")

    assert len(not_found_input) == 0, f"Expected {len(category)} categories are displayed correctly, but the followings input not found > {not_found_input}"

    # Collects results
    for x, y in results.items():
        if not y:
            error_results.append(x)

    if len(error_results) > 0:
        print(f"{len(error_results)} Error Results > {error_results}")

    assert len(error_results) == 0, f"Expected all categories are displayed correctly, but the {len(error_results)} followings not found > {error_results}"


@then("Verify click on categories {category_list} and correct page opens")
def verify_categories_under_browse(context, category_list):

    category = category_list.split("|")
    results = {}
    error_results = []
    not_found_input = []
    for n in category:
        this_expected_alt = expected_alt.get(n, "Not found")
        if this_expected_alt == "Not found":
            not_found_input.append(n)
        else:
            this_selector = f"[alt='{this_expected_alt}']"
            results[n] = context.app.base_page.find_element(By.CSS_SELECTOR, this_selector)
            results[n].click()
            results[n] = context.app.header.verify_breadcrumb(n)
            context.app.base_page.go_back()

    assert len(not_found_input) == 0, f"Expected {len(category)} input categories are displayed correctly, but the followings not found > {not_found_input}"

    # Collects results
    for x, y in results.items():
        if not y:
            error_results.append(x)

    if len(error_results) > 0:
        print(f"{len(error_results)} Error Results > {error_results}")

    assert len(error_results) == 0, f"Expected all categories are displayed correctly, but the {len(error_results)} followings not found > {error_results}"