
class FilterPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "assert_page": '(//h2[@class="kt-post-card__title"])[1]',
            "assert_page_label": '//*[text()=" دیوار من "]',
            "vehicles_btn": '//*[@href="/s/tehran/vehicles"]',
            "auto_btn": '//*[@href="/s/tehran/auto" and text()="خودرو"]',
            "price_btn": 'khesht-3',
            "price_max_btn": '(//div[@id="khesht-2"]//button[@class="kt-select-field kt-select-field--small kt-select-field--normal"])[2]',
            "search_input": '//div[contains(@class,"kt-select-search")]//input[@placeholder="جستجو"]',
            "search_result_list": '//ul[@class="kt-select-option-list kt-select-option-list--small"]',
            "immediate_btn": '//div[@class="filter-field--inline-d844c filter-field-c0991 filter-field__urgent"]',

            "filter_box": '//div[@class="browse-sidebar-ec193"]',
            "kilometers_btn": '//span[text()="کارکرد"]',
            # "kilometers_btn": '//*[@id="khesht-9"]',
            "kilometers_max_btn": '(//div[@id="khesht-8"]//button[@class="kt-select-field kt-select-field--small kt-select-field--normal"])[2]',
            # "search_input_kilometers": '//div[contains(@class,"kt-select-search")]//input[@placeholder="جستجو"]',
        }

    def __getitem__(self, index):
        return self.locators[index]