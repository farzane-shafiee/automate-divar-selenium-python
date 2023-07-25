
class FilterPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "assert_page": '(//h2[@class="kt-post-card__title"])[1]',
            "assert_page_label": '//*[text()=" دیوار من "]',

            "search_box": '//form[@class="search-bar__input-form"]//input[@type="text"]',

            "vehicles_btn": '//*[@href="/s/tehran/vehicles"]',
            "auto_btn": '//*[@href="/s/tehran/auto" and text()="خودرو"]',
            "price_btn": 'khesht-3',
            "assert_price_input": '//label[text()="حداکثر"]',
            "price_max_btn": '(//div[@id="khesht-2"]//button[@class="kt-select-field kt-select-field--small kt-select-field--normal"])[2]',
            "search_input": '//div[contains(@class,"kt-select-search")]//input[@placeholder="جستجو"]',
            "search_result_list": '//ul[@class="kt-select-option-list kt-select-option-list--small"]',
            "immediate_btn": '//div[@class="filter-field--inline-d844c filter-field-c0991 filter-field__urgent"]',

            "filter_box": '//div[@class="browse-sidebar-ec193"]',
            "kilometers_btn": 'khesht-11',
            "assert_scroll": '//img[@alt="نشان نماد تجارت الکترونیکی"]',
            "assert_kilometers_input": '(//label[text()="تا"])[2]',
            "kilometers_max_btn": '(//div[@id="khesht-10"]//button[@class="kt-select-field kt-select-field--small kt-select-field--normal"])[2]',
        }

    def __getitem__(self, index):
        return self.locators[index]
